from distutils.core import setup

setup(
    name='commute',
    version='0.1dev',
    packages=['src',],
    install_requires=['googlemaps==2.5.1',
                      'peewee==2.10.0']
)
