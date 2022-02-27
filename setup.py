from setuptools import setup, find_packages

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Shelegia_Motta_2021',
    packages=find_packages(exclude=["Shelegia_Motta_2021_Test"]),
    version='1.0.1',  # change with new version
    license='MIT',
    description='Implements the model presented in Shelegia and Motta (2021)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Manuel Bieri',
    author_email='manuel.bieri@outlook.com',
    url='https://github.com/manuelbieri/shelegia_motta_2021',
    download_url='https://github.com/manuelbieri/Shelegia_Motta_2021/archive/refs/tags/v1.0.0.tar.gz',  # change with new version
    keywords=['Acquisition', 'Kill Zone'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # "3 - Alpha" / "4 - Beta" / "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        "matplotlib>=3.5.1",  # change with new version
    ],
)
