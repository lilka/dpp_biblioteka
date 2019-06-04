from setuptools import setup, find_packages

setup(
    name='FourSquare',
    version='0.4',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    url='https://github.com/lilka/dpp_biblioteka',
    author='Lilla Lomnicka',
    author_email='238306@student.pwr.edu.pl',
    include_package_data = True
)