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
        print("__1__")
        subprocess.call(args)
    except:
        print("error")
        sys.exit(sys.exc_info()[0])

def timestamp():
    return datetime.now().isoformat()


class Updater(object):
    def __init__(self, path, name):
        self.path = path # Currently unused.
        self.name = name
        print("__AAA__")

    def push(self):
        cmd = "git push origin master"
        print("__2__")
        execute(cmd)

    def commits(self, count=1):
        add = "git add ."
        commit = "git commit -m %s" % timestamp()
        for i in range(count):
            self.__modify()
            print("__3__")
            execute(add)
            execute(commit)

    def __modify(self):
        print("__4__")
        with open(self.name, 'w') as f:
            f.write("Datetime: %s" % timestamp())
            f.close()


if __name__ == '__main__':
    # Sample usage
    print("__5__")
    path = '/Users/satoneyamanami/workdir/isaax_tester/app.py'
    name = 'template.py'
    print("__6__")

    # Update twice.
    app = Updater(name, path)
    print("__7__")
    app.commits(2)
    print("__8__")
    app.push()
