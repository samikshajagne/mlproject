from setuptools import find_packages,setup
from typing import List

HYPHEN_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_e_dot in requirements:
            requirements.remove(HYPHEN_e_dot)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='samiksha',
    author_email='samikshajagne2@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)