"""Quack setup script."""

from setuptools import setup

setup(
    name='quack',
    version='0.1.1.post3',
    packages=['quack'],

    # dependencies
    install_requires=[
        'argparse',
        'gitpython',
        'pyyaml'
    ],

    # metadata for upload to PyPI
    author='Love Sharma',
    author_email='contact@lovesharma.com',
    description=('Insert specific module / folder from given '
                 'repositories in yaml configurations.'),
    license='MIT',
    keywords='quack build submodule module dependencies'.split(),
    url='https://github.com/roxiemobile-forks/quack',  # project homepage
    download_url='https://github.com/roxiemobile-forks/quack/archive/0.1.1.post3.tar.gz',

    entry_points={
        'console_scripts': [
            'quack=quack.quack:main'
        ]
    }
)
