#python

import shlex
import subprocess

test = shlex.split("ls")
subprocess.call(test)
