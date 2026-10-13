from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

setup(
    name="mLproject",
    version="0.0.1",
    author="charith",
    author_email="<charithkasthala@gmail.com>",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")           
)