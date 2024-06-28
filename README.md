#Configurar el proyecto de petalinux sin abrir menus de configuración
```bash
petalinux-config --get-hw-description ../ebaz4205_dma_test/ --silentconfig
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
