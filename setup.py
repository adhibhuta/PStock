from setuptools import setup

setup(
    name = 'PStock',
    version = '0.0.1',
    packages = ['base'],
    description = 'Commandline utility to check stock details',
    author = 'lladhibhutall',
    author_email = 'debjyoti.biswas@outlook.com',
    url = 'https://github.com/lladhibhutall',
    install_requires=['click','requests','plotille'],
    license='Apache2',
    classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3'
      ],
    entry_points = {
        'console_scripts': [
            'PStock = base.__main__:main'
        ]
    })
