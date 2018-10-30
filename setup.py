from setuptools import setup

setup(
    name='RasPiTape',
    version='1',
    packages=['RasPiTape',
              'RasPiTape.main_window'],
    url='https://github.com/Logout22/RasPiTape',
    license='GPL v3',
    author='Martin Unzner',
    author_email='martin.u@posteo.de',
    description='The posh alternative to ArduiTape',
    install_requires=[
        'pygobject'
    ]
)
