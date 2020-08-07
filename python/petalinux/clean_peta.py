import os
import subprocess
import argparse
from terminal_control import subprocess_cmd

def main(options):
    aux_env_variables = "export TERM=xterm; printenv; "
    src_vivado = "source " +  options.vivado_env_settings_path + "; "
    src_petalinux = "source " +  options.petalinux_env_settings_path + "; "

    proj_dir = os.getcwd() + options.project_path
    os.chdir(proj_dir)

    peta_clean = aux_env_variables + src_vivado + src_petalinux + "petalinux-build -x mrproper; rm -R components/bootloader "
    subprocess_cmd(peta_clean)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "Flash FPGA after petalinux build")
    parser.add_argument('--project_path', default= '/pwm_project/', help= 'path to petalinux project')
    parser.add_argument('--petalinux_env_settings_path', default= '/opt/pkg/petalinux/settings.sh', help= 'path to petalinux settings.sh')
    parser.add_argument('--vivado_env_settings_path', default= '/opt/Xilinx/Vivado/2017.4/settings64.sh', help= 'path to vivado settings.sh')
    main(parser.parse_args())
