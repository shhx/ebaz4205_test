# Petalinux useful commands
```bash
petalinux-config --get-hw-description ../ebaz4205_dma_test/ --silentconfig
petalinux-build -c u-boot-zynq-scr  # Rebuild only boot.scr
``` 

petalinux-build
source make_boot.sh 
./copy_boot.sh 
source copy_to_sd.sh /dev/sda

# TFTP BOOT

The boot.cmd that generates the boot.scr is the following:

```bash
fitimage_name=image.ub
kernel_name=zImage
dtb_name=system.dtb
ramdisk_name=ramdisk.cpio.gz.u-boot
rootfs_name=rootfs.cpio.gz.u-boot

dhcp 0x200000 ${kernel_name}
dhcp 0x100000 ${dtb_name}
bootz 0x200000 - 0x100000
``` 

# Manual boot from sd
```bash
setenv bootargs console=ttyPS1,115200 root=/dev/mmcblk0p2 rw earlyprintk rootfstype=ext4 rootwait
fatload mmc 0:1 0x2000000 image.ub; bootm 0x2000000
fatload mmc 0:1 0x1000000 image.ub; fatload mmc 0:1 0x3000000 system.dtb; bootm 0x1000000 - 0x3000000
fatload mmc 0:1 0x1000000 uImage; fatload mmc 0:1 0x3000000 system.dtb; bootm 0x1000000 - 0x3000000
```

# Manual boot from tftp
```bash
dhcp 0x200000 zImage; dhcp 0x100000 system.dtb; bootz 0x200000 - 0x100000
```

## Useful device tree commands
```bash
dtc -I dtb system.dtb > system.dts
dtc -I dts system.dts -O dtb -o system.dtb system.dts
dtc -I fs /sys/firmware/devicetree/base

```
### FIT images
https://www.gibbard.me/linux_fit_images/
```bash
mkimage -f image.its image.ub
dumpimage -l image.ub  # List the contents of the FIT image
dumpimage -T multi image.ub  # List the contents of the FIT image
dumpimage -T flat_dt -p 0 -o temp/Image image.ub # p is the index of the image in the FIT image
dumpimage -T flat_dt -p 1 -o ex_system.dtb image.ub # Extract the device tree
```

# NFS boot
https://developer.toradex.com/linux-bsp/os-development/boot/boot-from-a-tftpnfs-server/
