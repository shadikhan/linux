# Filesystem Troubleshooting

## [Troubleshoot Linux Filesystem & Mount Problems | Into the Terminal 111
](https://www.youtube.com/live/-qKV2o9R0XI?si=GHTvxGkBuDrX5o-E)

### File System Tools

``` bash
# What disks and partitions are available on the system?
# "List Block Devices"
shad@linux:~/linux/notes/networking$ lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda       8:0    0   30G  0 disk 
├─sda1    8:1    0   29G  0 part /
├─sda14   8:14   0    4M  0 part 
├─sda15   8:15   0  106M  0 part /boot/efi
└─sda16 259:0    0  913M  0 part /boot
sdb       8:16   0   16G  0 disk 
└─sdb1    8:17   0   16G  0 part /mnt

# Show detailed information about available block devices
shad@linux:~/linux/notes/networking$ blkid
/dev/sdb1: LABEL="Temporary Storage" BLOCK_SIZE="512" UUID="9490151C90150680" TYPE="ntfs" PARTUUID="76ec78d5-01"
/dev/sda16: LABEL="BOOT" UUID="4e0b0f7d-f018-493d-b384-d56a4d4661bd" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="bc888243-c7df-4555-b820-0fa1621cf3e0"
/dev/sda15: LABEL_FATBOOT="UEFI" LABEL="UEFI" UUID="B0C0-7511" BLOCK_SIZE="512" TYPE="vfat" PARTUUID="d403963f-6b02-4be2-96ef-428181705f25"
/dev/sda1: LABEL="cloudimg-rootfs" UUID="fad0ebd7-fc6c-42fe-a34d-4e8d2f07946f" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="625cad27-7b63-4e5e-8bbd-6efc33b38415"

# Shows you all mounted filesystems and their mount options
shad@linux:~/linux/notes/networking$ mount
/dev/sda1 on / type ext4 (rw,relatime,discard,errors=remount-ro,commit=30)
devtmpfs on /dev type devtmpfs (rw,nosuid,noexec,relatime,size=4036848k,nr_inodes=1009212,mode=755,inode64)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev,inode64)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,nodev,size=1616532k,nr_inodes=819200,mode=755,inode64)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k,inode64)
cgroup2 on /sys/fs/cgroup type cgroup2 (rw,nosuid,nodev,noexec,relatime,nsdelegate,memory_recursiveprot)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
efivarfs on /sys/firmware/efi/efivars type efivarfs (rw,nosuid,nodev,noexec,relatime)
bpf on /sys/fs/bpf type bpf (rw,nosuid,nodev,noexec,relatime,mode=700)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=32,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=1639)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,nosuid,nodev,relatime,pagesize=2M)
mqueue on /dev/mqueue type mqueue (rw,nosuid,nodev,noexec,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,nosuid,nodev,noexec,relatime)
tracefs on /sys/kernel/tracing type tracefs (rw,nosuid,nodev,noexec,relatime)
fusectl on /sys/fs/fuse/connections type fusectl (rw,nosuid,nodev,noexec,relatime)
configfs on /sys/kernel/config type configfs (rw,nosuid,nodev,noexec,relatime)
/dev/sda16 on /boot type ext4 (rw,relatime,discard)
/dev/sda15 on /boot/efi type vfat (rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro)
binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,nosuid,nodev,noexec,relatime)
/dev/sdb1 on /mnt type ext4 (rw,relatime,x-systemd.after=cloud-init.service,_netdev)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=808264k,nr_inodes=202066,mode=700,uid=1000,gid=1000,inode64)

# Human readable output to space available
shad@linux:~/linux/notes/networking$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        29G  3.3G   25G  12% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           1.6G 1016K  1.6G   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
efivarfs        128K   37K   87K  30% /sys/firmware/efi/efivars
/dev/sda16      881M  110M  710M  14% /boot
/dev/sda15      105M  6.2M   99M   6% /boot/efi
/dev/sdb1        16G   28K   15G   1% /mnt
tmpfs           790M   12K  790M   1% /run/user/1000

# Human readable output to inode usage
shad@linux:~/linux/notes/networking$ df -hi
Filesystem     Inodes IUsed IFree IUse% Mounted on
/dev/root        3.7M  116K  3.6M    4% /
tmpfs            987K     1  987K    1% /dev/shm
tmpfs            800K   788  800K    1% /run
tmpfs            987K     3  987K    1% /run/lock
efivarfs            0     0     0     - /sys/firmware/efi/efivars
/dev/sda16        58K   604   57K    2% /boot
/dev/sda15          0     0     0     - /boot/efi
/dev/sdb1        1.0M    12  1.0M    1% /mnt
tmpfs            198K    36  198K    1% /run/user/1000

# Human readable output to directory size
shad@linux:~$ du -hs /home/shad
754M    /home/shad

# Human readable output to directory size, max depth 1
shad@linux:~$ du -h --max-depth 1 /home/shad
12K     /home/shad/.local
24K     /home/shad/folder1
677M    /home/shad/.vscode-server
16K     /home/shad/.cache
24K     /home/shad/.ssh
16K     /home/shad/root
228K    /home/shad/.dotnet
77M     /home/shad/linux
16K     /home/shad/.config
754M    /home/shad

# List open file handles
shad@linux:~$ sudo lsof | grep /var/log/auth.log
rsyslogd    882                          syslog    9w      REG                8,1    252846      34523 /var/log/auth.log
rsyslogd    882   933 in:imuxso          syslog    9w      REG                8,1    252846      34523 /var/log/auth.log
rsyslogd    882   934 in:imklog          syslog    9w      REG                8,1    252846      34523 /var/log/auth.log
rsyslogd    882   935 rs:main            syslog    9w      REG                8,1    252846      34523 /var/log/auth.log
```

### What is a filesystem?

![Filesystem Diagram](../images/filesystem.png)

- This directory structure is built out of component devices.
- So `/var/` could be on a disk partition `/dev/sdb4`. Inside here, we've applied a file system format, like ext4, so that we can store files and directories.
- Within `/dev/sdb4`, there's data, file metadata, etc.
- Note that the partition `/dev/sdb4` has finite size (ex. 15 GB). So when we put things in `/var/`, we're using that size.
- Within the filesystem format in `/dev/sdb4`, there are data blocks (file contents) and inodes (file pointer, tracking metadata: data block locations, permissions, timestamps, etc).

### Accessing my files

![Filesystem Structure](../images/filesystem_structure.png)

``` bash
shad@linux:/var/log$ ls -li
total 12172
 84397 lrwxrwxrwx  1 root      root                 39 Oct  1 04:13 README -> ../../usr/share/doc/systemd/README.logs
 34594 -rw-r--r--  1 root      root               1000 Nov  7 20:56 alternatives.log
 34191 -rw-r--r--  1 root      root               1662 Oct 22 21:03 alternatives.log.1
266230 drwxr-x---  2 root      adm                4096 Nov 10 00:00 apache2
 34094 -rw-r-----  1 root      adm                   0 Oct 17 23:14 apport.log
 84398 drwxr-xr-x  2 root      root               4096 Nov 21 01:51 apt
 ```

 - Within our filesystem, we have an inode table (stores file metadata).
 - Each entry has an inode number (first column in `ls -i` output), permissions, owner, etc. At the very end, we have pointers to data blocks (file contents).
 - Bunch of I/O requests to these data blocks when we read these files.
 - Deletion marks the inode entry and data blocks as free to re-use.

 ### Troubleshooting inodes

 - `touch testfile` results in `No space left on device` error, on `/mnt/dir`
 - `df -h` shows that the filesystem on `/dev/sda3` mounted at `/mnt` has only 3% used.
 - Why can't I make a file then?
 - Two aspects of a filesystem:
    - Data blocks (file contents): Not causing out of space error as we see from `df -h` (only 3% used).
    - Another component which is a limited quantity: inodes.
- Running `df -i` shows us that IUse% is at 100% for `/dev/sda3` mounted at `/mnt`.
- If you have a file system that has a ton of tiny files, you can run out of inodes even if you have free data blocks.
- If we remove a file, we see that the IUsed count goes down by one (every file takes up one inode). 
- Every file only uses one inode. If you expand the number of data blocks included in the inode data, it takes data blocks from file system and converts them to additional data block pointers. Concept: Indirect file pointing. Inode points to indirect pointer (block of additional pointers) that then point to data blocks. Can go several layers deep to store large fiels.
- Some FS are smart enough (XFS) to dynamically allocate inodes.
- For this demo, EXT4 was chosen, because XFS wouldn't even allowed us to make a FS this small, plus it would convert data blocks to inodes dynamically.
- Solution:
    - Allocate more inodes ahead of time if you know if you're going to have a lot of tiny files.
    - Could also use XFS.
    - Make a new filesystem and migrate to it, or delete some files.
    - If we used an extensible device, like Logical Volume Manager (LVM), we could expand the size of the filesystem, which would also give us more inodes.

 ### Troubleshooting deleted files

- `df -h` shows that the file system on `/dev/sda2` mounted at `/` is 99% used.
- So we're almost out of space on this filesystem.
- We could do a filesystem extension like we were talking about with inodes.
- What if this is the only node that's like this?
- Let's use `du` to figure out what's consuming this 20GB of space.

``` bash
# sort -hr : sort human readable numbers in reverse order
shad@linux:~$ du -h / | sort -hr | head
3.5G    /
1.9G    /usr
985M    /usr/lib
762M    /home/shad
762M    /home
754M    /var
682M    /home/shad/.vscode-server
346M    /var/log
334M    /var/log/journal/aa9e0761fad9437b96177cffcbf41daa
334M    /var/log/journal
```

- Assume that `/var` and `/var/log` are looking a bit large (16 GB).
- `ls -lS /var/log` to sort files by size.
- We see a `bigfile.log` that is 16 GB.
- We delete it with `rm /var/log/bigfile.log`.
- But `df -h` still shows that the filesystem is 99% used. Huhhh? And `du / 2>/dev/null | head` shows that `/var/log` isn't there any more. What's going on???
- Remember that when we delete a file, we mark the inode and data blocks as free to re-use. **But that only happens when no processes have the file open.** Note that this could mean we could restore the file if we wanted to.
- `lsof | grep bigfile.log` to see which processes have this file open. **But also, if you forgot the name of the file, you could do `lsof | grep deleted` to see all deleted files that are still open by some process.**
- We see that the `less` command on PID 2464 has the file open. `kill -9 2464` to kill the process. The `-9` is a SIGKILL, which forcefully kills the process.
- Now if we do `df -h`, we see that the filesystem usage has dropped down to 19%.
- So we werent' able to mark all of those data blocks and inode for re-use until the process that had the file open released it (by exiting).

### Overmounted filesystems

- `ssh user@linuxserver` to log into a remote server.
- We get `Could not chdir to home directory /home/user: No such file or directory`.

``` bash
shad@linux:~/linux/notes/os$ grep shad /etc/passwd
shad:x:1000:1000:Ubuntu:/home/shad:/bin/bash
```

- But, as root, when we do `ls -l /home`, we don't see a `shad` directory. Bruh who deleted my home directory???
- We do see a `lost+found` directory in `/home`, which tells me that `/home` is a mount point for another filesystem.
- When we run `df -h`, we see that `/dev/sda3` is mounted at `/home`. However, when we did that, there was already data in `/home`. Did we erase all the data in `/home` when we mounted `/dev/sda3` there???
- It's not there anymore because it's obscured by the new filesystem that we mounted at `/home`. When we mount a new device on top of directory, when application go into that directory, they see the most recently mounted filesystem on that directory location.
- If we run `umount /home`, we see that our `shad` directory is back.
- There is a place where we could temporarily attach things in the system. `mount /dev/sda3/mnt /mnt` is a good place to mount things temporarily.
- Assuming we want their home directory to be on `/dev/sda3`:
    - `mount /dev/sda3 /mnt`
    - `cp -a /home/shad /mnt` to copy the contents of our home directory to the new filesystem. Which results in `/mnt/shad`.
    - `umount /mnt`
    - `mount /dev/sda3 /home`
- Now when we `ssh user@linuxserver`, we can access our home directory again, which is on `/dev/sda3`.
- And running `mount` will show us that `/dev/sda3` is mounted at `/home`.
- `lsblk, blkid, mount` will give you insight as to what's mounted where.

### Readonly filesystems

- `mount -o remount,rw /home` to remount `/home` as read-write.
- Can't reduce XFS filesystems, but can with EXT4.
