from setuptools import find_packages,setup
from typing import List


def get_requirments()-> List[str]:
    """
    this function will return list of requirments
    """
    requirment_list=[]
    try:
        with open('requirements.txt', 'r') as f:
            lines=f.readlines()
            for line in lines:
                requirment=line.strip()
                # ignore empty lines and -e .
                if requirment and requirment!='-e .':
                   requirment_list.append(requirment)
                
            
    except FileNotFoundError:
        print('requirements.txt not found')
        
    return requirment_list

setup(
    name="Network Security",
    version="0.0.1",
    author="Vivek Nair",
    author_email="vivekh2004@gmail.com",
    packages=find_packages(),
    install_packages=get_requirments(),
)
    