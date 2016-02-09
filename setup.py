import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = ''

with open('cronwatch.py', 'r') as fd:
    regex = re.compile(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = regex.match(line)
        if m:
            version = m.group(1)
            break

setup(
    name='cronwatch',
    scripts=['cronwatch.py'],
    package_data={'': ['LICENSE']},
    version=version,
    description='Cron\'s runner with integrated Sentry monitor',
    author='Andrey Gubarev',
    author_email='mylokin@me.com',
    url='https://github.com/mylokin/cronwatch',
    keywords=['cron'],
    license='MIT',
    platforms='any',
    install_requires=[
        'Raven>=5.0',
    ],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
