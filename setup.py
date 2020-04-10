from setuptools import setup, find_packages
import codecs
import os
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="FF_APP_automation_core", # Replace with your own username
    version="0.0.2",
    author="Sunny Yu",
    author_email="sunny.yu@farfetch.com",
    description="foundation tech layer for the appium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="test",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    )
    
    
