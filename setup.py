from setuptools import setup, find_packages

setup(
    name="cool-logging",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "termcolor"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
