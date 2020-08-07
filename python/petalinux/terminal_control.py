import subprocess
import sys

def subprocess_cmd(commands):
    print("Executing shell commands:")
    print(commands)
    sys.stdout.flush()

    process = subprocess.Popen(commands,stdout=subprocess.PIPE, shell=True)
    for line in iter(process.stdout.readline,''):
        print line,
    process.kill()
