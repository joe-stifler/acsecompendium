"""Setup script for acse_compendium package."""

import os
from setuptools import setup


def read(fname):
    """Read a file and return its contents as a string."""
    path = os.path.join(os.path.dirname(__file__), fname)
    with open(path) as f:
        return f.read()


setup(
    name="acse_compendium",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    license="MIT",
    long_description=read("README.md"),
    url="https://github.com/joe-stifler/acse_compendium",
    description="""Essential best practices and techniques from Imperial College London's MSc in ACSE.""",
    author="Joe",
    author_email="joseribeiro1017@gmail.com",
    packages=["acse_compendium"],
)
