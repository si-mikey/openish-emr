from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="openish-emr",
    version="0.0.1",
    author="Luis Lopez",
    author_email="mikeylopez@gmail.com",
    description="A semi open source electronic medical records application",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/si-mikey/openish-emr/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: GNU General Public License v3 (GPLv3)",
    ],
)
