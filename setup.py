
from setuptools import setup, find_packages

setup(
    name='hierarchy',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'gitignore-parser',
    ],
    entry_points={
        'console_scripts': [
            'hierarchy=hierarchy.main:main',
        ],
    },
    description='A tool to print directory hierarchy and create a zip file, respecting .gitignore rules.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/hierarchy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
