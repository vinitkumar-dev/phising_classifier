from setuptools import find_packages,setup





def get_requirements(file_path):
    requirements = []
    with open(file_path,'r') as f :
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]

    return requirements

setup(
    name='phishingClassifier',
    version='0.0.1',
    author='vinit kumar',
    author_email='vinit@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)