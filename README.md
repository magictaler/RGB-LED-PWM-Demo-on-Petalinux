# README #

RGB PWM LED Demo Petalinux project running on ARTY Z7-20 hardware

Copyright (C) 2020 Magictale Electronics
http://magictale.com

Getting started:

* Build the rgb_pwm_led_demo_top.hdf file and copy it to Petalinux folder (please refer to https://github.com/magictaler/RGB-LED-PWM-Demo-for-Arty-Z7-20 project);

The following must be ran on a Linux machine with Petalinux SDK 2017.3 installed:

* Execute the following command in the RGB-LED-PWM-Demo-on-Petalinux directory:
    + python python/petalinux/clean_peta.py 

* Execute the following command in the RGB-LED-PWM-Demo-on-Petalinux directory:
    + python python/petalinux/create_peta.py 

* The result of the build should be BOOT.bin located in RGB-LED-PWM-Demo-on-Petalinux/images/linux
