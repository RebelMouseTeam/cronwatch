'''
Cron's runner with integrated Sentry monitor
'''

__version__ = '0.2.1'

import os
import sys
import contextlib

import raven
client = raven.Client(
    dsn=(os.getenv('SENTRY_DSN') or None),
    transport=raven.transport.http.HTTPTransport)


@contextlib.contextmanager
def args():
    sys.argv, _ = sys.argv[1:], sys.argv[:]
    yield
    sys.argv = _


def main():
    path = os.path.abspath(sys.argv[1])
    try:
        with args():
            execfile(path, {'__file__': path})
    except:
        client.captureException()
        raise

if __name__ == '__main__':
    main()
