from setuptools import setup, find_packages
from pathlib import Path

__version__ = "1.0.4"
__author__ = "Michał Skibiński"

this_directory = Path(__file__).parent

with open(this_directory / "readme.md") as f:
    readme = f.read()

setup(
    name="wykop",
    install_requires=["httpx", "loguru"],
    version=__version__,
    author=__author__,
    description="Python client for interacting with the Wykop API v3.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="michalskibinski109@gmail.com",
    url="https://github.com/michalskibinski109/wykop",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
)
