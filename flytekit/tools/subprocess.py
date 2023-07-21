import logging
import shlex as _schlex
import subprocess as _subprocess
import tempfile as _tempfile


def check_call(cmd_args, **kwargs):
    if not isinstance(cmd_args, list):
        cmd_args = _schlex.split(cmd_args)
    print("Running {cmd_args}")
    
    p = _subprocess.Popen(cmd_args, **kwargs)
    _, _ = p.communicate()

    # Dump sub-process' std out into current std out

    if p.returncode != 0:
        logging.error("Error from command '{}':\n{}\n".format(cmd_args, ret_code))

        raise Exception(
            "Called process exited with error code: {}.  Stderr dump:\n\n{}".format(ret_code, err_str)
        )

    return 0
