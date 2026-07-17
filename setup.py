from setuptools import find_packages, setup
from typing import List
def get_requirements() -> List[str]:
    '''
    this function will return list of requirements

    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read  lines from the file
            lines=file.readlines()
            #processing each line:
            for line in lines:
                #stripping extra spaces
                requirement=line.strip()
                # ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="network_security",
    version="0.0.1",
    author="Atul Tewari",
    author_email="atul26tewari@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)