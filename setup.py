from setuptools import setup

setup(
    name = 'PStock',
    version = '0.0.1',
    packages = ['base'],
    install_requires=['click','requests','plotille'],
    entry_points = {
        'console_scripts': [
            'PStock = base.__main__:main'
        ]
    })
