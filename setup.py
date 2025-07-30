from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    :return: List of dependencies
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            # Process each line 
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and lines starting with -e
                if requirement and not requirement.startswith('-e'):
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")
    return requirement_lst
print(get_requirements())
setup(
    name='NetworkSecuritySystem',
    version='0.0.1',
    author='Akula Shreyas',
    author_email='shreyasakula97@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)