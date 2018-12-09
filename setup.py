from setuptools import setup

setup(
    name = 'PStock',
    version = '0.0.1',
    packages = ['base'],
    install_requires=['click','requests','json','drawille'],
    entry_points = {
        'console_scripts': [
            'PStock = base.__main__:main'
        ]
    })
