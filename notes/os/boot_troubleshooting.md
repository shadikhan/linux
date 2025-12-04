# Boot Troubleshooting

## Boot Tools

- A lot of the times, when troubleshooting boot, there commonly is file system problems.
- Tools we've used to debug file systems:
    - `df -h`: Disk free, but shows us which filesystems are mounted.
    - `fdisk -l`: List the file systems on your attached devices.
    - `lsblk`: List block devices in tree format.
    - `blkid`: Will show you the UUIDs of your partitions.
    - `mount`: Show currently mounted file systems. Shad: `findmnt` helps to see what's mounted.
- Covering some new tools today.

### fsck (filesystem check)

``` bash

# fsck must be run on unmounted file systems.
root@linux:/home/shad# umount /mnt

root@linux:/home/shad# fsck /mnt
fsck from util-linux 2.39.3
e2fsck 1.47.0 (5-Feb-2023)
/dev/sdb1: clean, 12/1048576 files, 93480/4193792 blocks

# undo
root@linux:/home/shad# mount /dev/sdb1 /mnt
```

- Checks the FS state, if it's a dirty state (not unmounted cleanly), will be able to fix it.

### grub-install

- bootloader is important for booting.

``` bash

oot@linux:/home/shad# grub-install /dev/sda
Installing for x86_64-efi platform.
Installation finished. No error reported.
```

- Will take our grub config file that is in boot and translate it into a master boot record or UEFI BIOS stored boot record for our machine.

