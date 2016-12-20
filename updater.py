#python
#!/usr/bin/env python
#-*-coding:utf-8-*-
from datetime import datetime
import shlex
import subprocess
import sys


def execute(cmd):
    args = shlex.split(cmd)
    try:
        subprocess.call(args)
    except:
        sys.exit(sys.exc_info()[0])

def timestamp():
    return datetime.now().isoformat()


class Updater(object):
    def __init__(self, path, name):
        self.path = path # Currently unused.
        self.name = name

    def push(self):
        cmd = "git push origin master"
        execute(cmd)

    def commits(self, count=1):
        add = "git add ."
        commit = "git commit -m %s" % timestamp()
        for i in range(count):
            self.__modify()
            execute(add)
            execute(commit)

    def __modify(self):
        with open(self.name, 'w') as f:
            f.write("Datetime: %s" % timestamp())
            f.close()


if __name__ == '__main__':
    # Sample usage
    path = '/Users/satoneyamanami/workdir/isaax_tester/app.py'
    name = 'template.py'

    # Update twice.
    app = Updater(name, path)
    app.commits(2)
    app.push()
