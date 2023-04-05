import subprocess


# +-- Raw data request and parsing gcp cli data --+
# command execute
# - shell: '/bin/bash'
def execute_command(command, input_param=None):
    if isinstance(input_param, str):
        input_param = bytes(input_param, encoding='utf-8')

    result = subprocess.run(
        command,
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT,
        shell = True,
        input = input_param,
        executable = "/bin/bash"
    )
    returncode = result.returncode
    stdout = result.stdout.decode('utf-8').strip("\n")

    return stdout
