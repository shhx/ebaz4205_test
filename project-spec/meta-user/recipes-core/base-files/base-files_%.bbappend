#base-files_%.bbappend content
  
dirs755 += "/media/card"
  
do_install:append() {
    sed -i '/mmcblk0p1/s/^#//g' ${D}${sysconfdir}/fstab
}
