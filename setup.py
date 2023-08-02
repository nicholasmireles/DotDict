import os
from setuptools import setup

HERE = os.path.dirname(os.path.realpath(__file__))
README = open(os.path.join(HERE, "README.md")).read()
setup(
    name="dotdict",
    version="0.0.1",
    description="dotdict package.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Nick Mireles",
    author_email="nick.mireles@dave.com",
    license="GPT GPL v3",
)
