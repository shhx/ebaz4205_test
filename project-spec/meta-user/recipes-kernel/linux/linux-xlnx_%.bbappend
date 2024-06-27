FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI:append = " file://bsp.cfg"
KERNEL_FEATURES:append = " bsp.cfg"
SRC_URI += "file://user_2023-12-17-19-25-00.cfg \
            file://user_2023-12-18-23-15-00.cfg \
            file://user_2023-12-19-22-21-00.cfg \
            file://user_2024-04-06-16-44-00.cfg \
            file://user_2024-04-06-17-19-00.cfg \
            file://user_2024-04-06-17-27-00.cfg \
            file://user_2024-04-06-17-34-00.cfg \
            "

