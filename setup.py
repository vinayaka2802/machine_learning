from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the given file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='vinayaka',
    author_email='vinayakakm28@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


