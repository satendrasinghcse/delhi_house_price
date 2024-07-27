from setuptools import setup, find_packages
import os
from typing import List

HYPEN_E_DOT = "-e ."


# Function to read requirements from the requirements.txt file
def read_requirements(file_path: str) -> List[str]:
    requirement = []
    with open(file_path, "r") as f:
        requirement = f.readlines()
        requirement = [req.replace("\n", "") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

    return requirement


# Setup function
setup(
    name="delhi_house_price",
    version="0.1.0",
    description="A machine learning project for the delhi house price dataset",
    author="Satendra Singh",
    author_email="satendrasinghcse@gmail.com",
    packages=find_packages(),
    install_requires=read_requirements("requirements.txt"),
)
