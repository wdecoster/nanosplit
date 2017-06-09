# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='NanoSplit',
    version='0.1.0',
    description='Perform splitting of Oxford Nanopore sequencing data in a fail and pass dataset.',
    long_description='Perform splitting of Oxford Nanopore sequencing data in a fail and pass dataset using a user defined quality cutoff. The script can read compressed input and will write to gzip compressed files.',
    url='https://github.com/wdecoster/nanosplit',
    author='Wouter De Coster',
    author_email='decosterwouter@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='nanopore sequencing processing trimming filtering',
    packages=find_packages(),
    install_requires=['biopython', 'nanomath', 'nanoget', 'gzip'],
    package_data={'nanosplit': []},
        package_dir={'nanosplit': 'nanosplit'},
        include_package_data=True,
        entry_points={
            'console_scripts': ['NanoSplit=nanosplit.NanoSplit:main',]}
)
