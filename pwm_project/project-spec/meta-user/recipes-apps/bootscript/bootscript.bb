#
# This file is the bootscript recipe.
#

SUMMARY = "Simple bootscript application"
SECTION = "PETALINUX/apps"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://bootscript \
	file://web/cgi-bin \
        file://web/images \
        file://web/Stylesheets \
        file://web/Javascript \
        file://web \
	"

# we add files here that we want to be packaged in the target file system 
FILES_${PN} =" \
  /home/root/httpd/cgi-bin/rgb-led-pwm \
  /home/root/httpd/images/MagictaleLogo.png \
  /home/root/httpd/Javascript/config.js \
  /home/root/httpd/Javascript/jquery-1.12.4.min.js \
  /home/root/httpd/Stylesheets/magictale.css \
  /home/root/httpd/Stylesheets/slider.css \
  /home/root/httpd/Stylesheets/tabs.css \
  /home/root/httpd/A-Calling-Font_D-by-7NTypes.woff \
  /home/root/httpd/footer.html \
  /home/root/httpd/header.html \
  /home/root/httpd/index.html \
  ${sysconfdir}/* \
"


S = "${WORKDIR}"

inherit update-rc.d
INITSCRIPT_NAME = "bootscript"
INITSCRIPT_PARAMS = "start 99 S ."

do_install() {
	install -d ${D}${sysconfdir}/init.d 
	install -m 0755 ${S}/bootscript ${D}${sysconfdir}/init.d

	install -d ${D}/home/root/httpd/cgi-bin
	install -m 0755 web/cgi-bin/rgb-led-pwm ${D}/home/root/httpd/cgi-bin

	install -d ${D}/home/root/httpd/images
	install -m 0644 web/images/MagictaleLogo.png ${D}/home/root/httpd/images
        
	install -d ${D}/home/root/httpd/Javascript
	install -m 0644 web/Javascript/config.js ${D}/home/root/httpd/Javascript
	install -m 0644 web/Javascript/jquery-1.12.4.min.js ${D}/home/root/httpd/Javascript

	install -d ${D}/home/root/httpd/Stylesheets
	install -m 0644 web/Stylesheets/magictale.css ${D}/home/root/httpd/Stylesheets
	install -m 0644 web/Stylesheets/slider.css ${D}/home/root/httpd/Stylesheets
	install -m 0644 web/Stylesheets/tabs.css ${D}/home/root/httpd/Stylesheets

	install -d ${D}/home/root/httpd
	install -m 0644 web/A-Calling-Font_D-by-7NTypes.woff ${D}/home/root/httpd/
	install -m 0644 web/footer.html ${D}/home/root/httpd/
	install -m 0644 web/header.html ${D}/home/root/httpd/
	install -m 0644 web/index.html ${D}/home/root/httpd/
}
