from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path: str)->List[str]:
    '''
    A function to read the requirements from requirements.txt file and 
    return them as a list of strings
    '''
    requirements = []
    with open (file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    c = "-e ." # THis line connects the setup.py file to the requirements,txt
    if c in requirements:
        requirements.remove(c)



setup(
    name = "mlproject",
    version= "0.0.1",
    # author="",
    packages = find_packages(),
    # install_requires = ["pandas", "numpy"],
    install_requires = get_requirements("requirements.txt")
)