from setuptools import setup, find_packages

setup(
    name='FourSquare',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    install_requires=['re'],
    url='https://git.e-science.pl/llomnicka238306/bibliotekaPython',
    author='Lilla Lomnicka',
    author_email='238306@student.pwr.edu.pl',
    include_package_data = True
)