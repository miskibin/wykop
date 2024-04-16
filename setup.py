from setuptools import setup, find_packages

setup(
    name="wykop",
    version="1.0.0",
    description="Python client for interacting with the Wykop API v3.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Michal Skibinski",
    author_email="michalskibinski109@gmail.com",
    url="https://github.com/michalskibinski109/wykop",
    packages=find_packages(),
    install_requires=["httpx>=0.23.0"],
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
    ],
    python_requires=">=3.8",
)
