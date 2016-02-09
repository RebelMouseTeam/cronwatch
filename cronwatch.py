'''
Cron's runner with integrated Sentry monitor
'''

__version__ = '0.1.0'

import sys
import contextlib


@contextlib.contextmanager
def args():
    sys_argv = sys.argv[:]
    sys.argv = sys.argv[1:]
    yield
    sys.argv = sys_argv


def execute(fname):
    try:
        execfile(fname)
    except:
        print 'catch'
        raise


def main():
    fname = sys.argv[1]
    with args():
        execute(fname)

if __name__ == '__main__':
    main()
