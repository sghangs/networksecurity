"""
The setup.py file is an essential part of packaging and distributing python
project.It is used by setuptools to define the configuration of your project 
such as its meta data, dependencies and more.
"""

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                #Ignore empty line and .e 
                if requirement and requirement!= "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found")
    
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sunny Ghangas",
    author_email="sunnyghangas098@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
