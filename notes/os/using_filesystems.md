# [How Do I Use Filesystems on Linux? | Into the Terminal 112](https://www.youtube.com/watch?v=SccVI8zWpkA&t=84s)

## Creating a filesystem

How to make a partition and put a file system in it.

``` bash
root@linux:/home/shad# lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda       8:0    0   30G  0 disk 
├─sda1    8:1    0   29G  0 part /
├─sda14   8:14   0    4M  0 part 
├─sda15   8:15   0  106M  0 part /boot/efi
└─sda16 259:0    0  913M  0 part /boot
sdb       8:16   0   16G  0 disk 
└─sdb1    8:17   0   16G  0 part /mnt

root@linux:/home/shad# parted /dev/sdb p
Model: Msft Virtual Disk (scsi)
Disk /dev/sdb: 17.2GB
Sector size (logical/physical): 512B/4096B
Partition Table: msdos
Disk Flags: 

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  17.2GB  17.2GB  primary  ext4

```

- msdos: Old style partition table.
- gpt: New style partition table. Can have larger partitions and more of them.
- Let's reset sdb.

``` bash

root@linux:/home/shad# umount /mnt/
root@linux:/home/shad# lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda       8:0    0   30G  0 disk 
├─sda1    8:1    0   29G  0 part /
├─sda14   8:14   0    4M  0 part 
├─sda15   8:15   0  106M  0 part /boot/efi
└─sda16 259:0    0  913M  0 part /boot
sdb       8:16   0   16G  0 disk 
└─sdb1    8:17   0   16G  0 part

# Let's wipe the partition table on /dev/sdb. Also needed to wipe /dev/sdb1 to remove the ext4 signature (see below).
root@linux:/home/shad# wipefs -a /dev/sdb
/dev/sdb: 2 bytes were erased at offset 0x000001fe (dos): 55 aa
/dev/sdb: calling ioctl to re-read partition table: Success

root@linux:/home/shad# lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda       8:0    0   30G  0 disk 
├─sda1    8:1    0   29G  0 part /
├─sda14   8:14   0    4M  0 part 
├─sda15   8:15   0  106M  0 part /boot/efi
└─sda16 259:0    0  913M  0 part /boot
sdb       8:16   0   16G  0 disk 

root@linux:/home/shad# parted /dev/sdb p
Error: /dev/sdb: unrecognised disk label
Model: Msft Virtual Disk (scsi)                                           
Disk /dev/sdb: 17.2GB
Sector size (logical/physical): 512B/4096B
Partition Table: unknown
Disk Flags:

root@linux:/home/shad# parted /dev/sdb mklabel gpt
Information: You may need to update /etc/fstab.

root@linux:/home/shad# parted /dev/sdb p
Model: Msft Virtual Disk (scsi)
Disk /dev/sdb: 17.2GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags: 

Number  Start  End  Size  File system  Name  Flags

root@linux:/home/shad# parted /dev/sdb mkpart part1 1 1001
Information: You may need to update /etc/fstab.

# Created a partition part1 of size 1000MB (from 1MB to 1001MB)
root@linux:/home/shad# parted /dev/sdb p
Model: Msft Virtual Disk (scsi)
Disk /dev/sdb: 17.2GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name   Flags
 1      1049kB  1001MB  1000MB  ext4         part1

# Hm, I didn't want ext4 there. Let's delete and try again.
root@linux:/home/shad# wipefs -a /dev/sdb1

# Better.
root@linux:/home/shad# parted /dev/sdb p
Model: Msft Virtual Disk (scsi)
Disk /dev/sdb: 17.2GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name   Flags
 1      1049kB  1001MB  1000MB               part1

# Adding another partition part2 of size 1000MB (from 1001MB to 2001MB)
root@linux:/home/shad# parted /dev/sdb mkpart part2 1001 2001
Information: You may need to update /etc/fstab.

root@linux:/home/shad# parted /dev/sdb p
Model: Msft Virtual Disk (scsi)
Disk /dev/sdb: 17.2GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name   Flags
 1      1049kB  1001MB  1000MB               part1
 2      1001MB  2001MB  999MB                part2

root@linux:/home/shad# lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda       8:0    0   30G  0 disk 
├─sda1    8:1    0   29G  0 part /
├─sda14   8:14   0    4M  0 part 
├─sda15   8:15   0  106M  0 part /boot/efi
└─sda16 259:0    0  913M  0 part /boot
sdb       8:16   0   16G  0 disk 
├─sdb1    8:17   0  954M  0 part 
└─sdb2    8:18   0  953M  0 part 

# Now let's create filesystems on the partitions.

root@linux:/home/shad# mkfs.xfs /dev/sdb1
meta-data=/dev/sdb1              isize=512    agcount=4, agsize=61056 blks
         =                       sectsz=4096  attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=1
         =                       reflink=1    bigtime=1 inobtcount=1 nrext64=0
data     =                       bsize=4096   blocks=244224, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=16384, version=2
         =                       sectsz=4096  sunit=1 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
Discarding blocks...Done.

root@linux:/home/shad# mkfs.ext4 /dev/sdb2
mke2fs 1.47.0 (5-Feb-2023)
Discarding device blocks: done                            
Creating filesystem with 243968 4k blocks and 61056 inodes
Filesystem UUID: fee03ce4-82dc-47b3-ab36-24459547b16f
Superblock backups stored on blocks: 
        32768, 98304, 163840, 229376

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (4096 blocks): done
Writing superblocks and filesystem accounting information: done

root@linux:/home/shad# parted /dev/sdb p
Model: Msft Virtual Disk (scsi)
Disk /dev/sdb: 17.2GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name   Flags
 1      1049kB  1001MB  1000MB  xfs          part1
 2      1001MB  2001MB  999MB   ext4         part2
```

## fdisk

Stands for fixed disk.

``` bash

root@linux:/home/shad# fdisk /dev/sdb

Welcome to fdisk (util-linux 2.39.3).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): m

Help:

  GPT
   M   enter protective/hybrid MBR

  Generic
   d   delete a partition
   F   list free unpartitioned space
   l   list known partition types
   n   add a new partition
   p   print the partition table
   t   change a partition type
   v   verify the partition table
   i   print information about a partition

  Misc
   m   print this menu
   x   extra functionality (experts only)

  Script
   I   load disk layout from sfdisk script file
   O   dump disk layout to sfdisk script file

  Save & Exit
   w   write table to disk and exit
   q   quit without saving changes

  Create a new label
   g   create a new empty GPT partition table
   G   create a new empty SGI (IRIX) partition table
   o   create a new empty MBR (DOS) partition table
   s   create a new empty Sun partition table


Command (m for help): p
Disk /dev/sdb: 16 GiB, 17179869184 bytes, 33554432 sectors
Disk model: Virtual Disk    
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: gpt
Disk identifier: 8735D6CE-E204-44DC-AC66-2C486F6937F0

Device       Start     End Sectors  Size Type
/dev/sdb1     2048 1955839 1953792  954M Linux filesystem
/dev/sdb2  1955840 3907583 1951744  953M Linux filesystem

Command (m for help): n

# So msdos partition tables only support up to 4 primary partitions. To create more, make number 4 an extended partition that can hold more partitions within it.

# GPT doesn't have that limitation.
Partition number (3-128, default 3): 3
First sector (3907584-33554398, default 3907584): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (3907584-33554398, default 33552383): 

Created a new partition 3 of type 'Linux filesystem' and of size 14.1 GiB.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

root@linux:/home/shad# fdisk -l /dev/sdb
Disk /dev/sdb: 16 GiB, 17179869184 bytes, 33554432 sectors
Disk model: Virtual Disk    
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: gpt
Disk identifier: 8735D6CE-E204-44DC-AC66-2C486F6937F0

Device       Start      End  Sectors  Size Type
/dev/sdb1     2048  1955839  1953792  954M Linux filesystem
/dev/sdb2  1955840  3907583  1951744  953M Linux filesystem
/dev/sdb3  3907584 33552383 29644800 14.1G Linux filesystem

root@linux:/home/shad# parted /dev/sdb p
Model: Msft Virtual Disk (scsi)
Disk /dev/sdb: 17.2GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name   Flags
 1      1049kB  1001MB  1000MB  xfs          part1
 2      1001MB  2001MB  999MB   ext4         part2
 3      2001MB  17.2GB  15.2GB

# lsblk -f also shows filesystem types and UUIDs, like parted does above.
root@linux:/home/shad# lsblk -f
NAME    FSTYPE FSVER LABEL           UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
sda                                                                                      
├─sda1  ext4   1.0   cloudimg-rootfs fad0ebd7-fc6c-42fe-a34d-4e8d2f07946f   24.7G    12% /
├─sda14                                                                                  
├─sda15 vfat   FAT32 UEFI            B0C0-7511                              98.2M     6% /boot/efi
└─sda16 ext4   1.0   BOOT            4e0b0f7d-f018-493d-b384-d56a4d4661bd  709.2M    12% /boot
sdb                                                                                      
├─sdb1  xfs                          52970836-a4af-4efe-a95c-f61d80bad000                
├─sdb2  ext4   1.0                   fee03ce4-82dc-47b3-ab36-24459547b16f                
└─sdb3                                                                                   

# Listing available mkfs types (tab completion)
root@linux:/home/shad# mkfs.
mkfs.bfs     mkfs.cramfs  mkfs.ext3    mkfs.fat     mkfs.msdos   mkfs.vfat    
mkfs.btrfs   mkfs.ext2    mkfs.ext4    mkfs.minix   mkfs.ntfs    mkfs.xfs
```

## mount

``` bash
root@linux:/home/shad# mount -t xfs /dev/sdb1 /mnt/
root@linux:/home/shad# ls -l /mnt
total 0

root@linux:/home/shad# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdb1       890M   50M  841M   6% /mnt
```

## fstab

``` bash

# Tell the system how to mount volumes at boot time.
root@linux:/home/shad# cat /etc/fstab
# CLOUD_IMG: This file was created/modified by the Cloud Image build process
UUID=fad0ebd7-fc6c-42fe-a34d-4e8d2f07946f       /        ext4   discard,commit=30,errors=remount-ro     0 1
LABEL=BOOT      /boot   ext4    defaults,discard        0 2
UUID=B0C0-7511  /boot/efi       vfat    umask=0077      0 1
/dev/disk/cloud/azure_resource-part1    /mnt    auto    defaults,nofail,x-systemd.after=cloud-init.service,_netdev,comment=cloudconfig 0       2

# Added line to mount /dev/sdb1 to /mnt at boot (edited with nano)

# CLOUD_IMG: This file was created/modified by the Cloud Image build process
# Note: to prevent boot issues in case /dev/sdb disappears, we use 'nofail' option.
UUID=fad0ebd7-fc6c-42fe-a34d-4e8d2f07946f       /        ext4   discard,commit=30,errors=remount-ro     0 1
LABEL=BOOT      /boot   ext4    defaults,discard        0 2
UUID=B0C0-7511  /boot/efi       vfat    umask=0077      0 1
# /dev/disk/cloud/azure_resource-part1  /mnt    auto    defaults,nofail,x-systemd.after=cloud-init.service,_netdev,comment=cloudconfig  0       2
/dev/sdb1       /mnt    xfs     defaults,ro,nofail      0       0

root@linux:/home/shad# umount /mnt

root@linux:/home/shad# mount /mnt

root@linux:/home/shad# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdb1       890M  320K  890M   1% /mnt

```

- We expect that if we reboot, /dev/sdb1 will be mounted to /mnt automatically because of the fstab entry, with no issues because of the 'nofail' option.