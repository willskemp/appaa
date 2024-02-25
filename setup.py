"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup

setup(
    name="Appa",
    version="1.0.0",
    description="A Python package for analysing randomised experiments.",
    author="Will Kemp",
    author_email="",
    install_requires=[
        "numpy",
        "pandas",
    ],
)
