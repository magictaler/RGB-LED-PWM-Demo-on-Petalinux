
import subprocess
import argparse
from terminal_control import subprocess_cmd
import os
import sys

def main(options):
    aux_env_variables = "export TERM=xterm; export PATH=/home/ubuntu/bin:/home/ubuntu/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin;"
    aux_env_variables_2 = "export XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop;"
    src_vivado = "source " +  options.vivado_env_settings_path + ";"
    src_petalinux = "source " +  options.petalinux_env_settings_path + "; printenv;"

    proj_dir = os.getcwd() + options.project_path
    os.chdir(proj_dir)

    petalinux_config = aux_env_variables + aux_env_variables_2 + src_vivado + src_petalinux + "echo ^e^e | petalinux-config --get-hw-description ../Petalinux/;"
    petalinux_build = aux_env_variables + aux_env_variables_2 + src_vivado + src_petalinux + "petalinux-build"
    petalinux_bootgen = aux_env_variables + aux_env_variables_2 + src_vivado + src_petalinux + "petalinux-package --boot --fsbl zynq_fsbl.elf --fpga " + options.bitstream_name + " --u-boot --kernel --force"

    # Variable will be used later when versioning is added
    # pylint: disable=unused-variable
    if 'BUILD_NUMBER' in os.environ:
        build_number = int(os.environ['BUILD_NUMBER'])
    else:
        build_number = 0

    print("Setting the FW build number to %s" % build_number)
    sys.stdout.flush()
    subprocess_cmd("sed -i \'/CONFIG_SUBSYSTEM_FW_VERSION=/c\CONFIG_SUBSYSTEM_FW_VERSION=\"%s\"\' project-spec/configs/config" % build_number)

    print("Petalinux config")
    sys.stdout.flush()
    subprocess_cmd(petalinux_config)

    print("Petalinux build")
    sys.stdout.flush()
    subprocess_cmd(petalinux_build)

    os.chdir("images/linux")

    print("Petalinux bootgen")
    sys.stdout.flush()
    subprocess_cmd(petalinux_bootgen)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "Builds Petalinux project")
    parser.add_argument('--project_path', default= '/pwm_project/', help= 'path to petalinux project')
    parser.add_argument('--petalinux_env_settings_path', default= '/opt/pkg/petalinux/settings.sh', help= 'path to petalinux settings.sh')
    parser.add_argument('--vivado_env_settings_path', default= '/opt/Xilinx/Vivado/2017.4/settings64.sh', help= 'path to vivado settings.sh')
    parser.add_argument('--bitstream_name', default= 'design_1_wrapper.bit', help= 'name of the bitstream file')
    main(parser.parse_args())
    