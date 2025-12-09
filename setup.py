from setuptools import setup, find_packages

setup(
    name='task-cli',
    version='0.1.0',
    description='A command-line interface (CLI) application built in Python for managing a simple to-do list, storing data in a local JSON file.',
    author='outnova',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'task-cli=src.cli:main',
        ],
    },
)