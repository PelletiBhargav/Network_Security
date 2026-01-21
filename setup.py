'''
The setup.pyfile is an essential part of packaging and distributing python projects.
it is used by setuptools(or distutils in older python versions)
to define the configuration of your project,such as its metadata,dependencies and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirement.txt",'r')as file:
            #Read lines from the file
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                #ignore empty lines  and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found")
        
    return requirement_lst


setup(
    name='networksecurity',
    version='0.0.1',
    author='Bhargav',
    author_email='pelletivenkatabhargav03@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
    
)