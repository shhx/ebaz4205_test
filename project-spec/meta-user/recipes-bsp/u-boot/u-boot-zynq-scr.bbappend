FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"
# Add custom boot.cmd file
SRC_URI += "file://boot.cmd.generic"

# Manual geneartion
# mkimage -c none -A arm -T script -d boot.cmd boot.scr