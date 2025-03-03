import os
from setuptools import setup, find_packages

# Get the current directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Read the README file
with open(os.path.join(current_directory, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the requirements file
requirements_path = os.path.join(current_directory, 'requirements.txt')
if os.path.isfile(requirements_path):
    with open(requirements_path, 'r') as f:
        install_requires = [line.strip() for line in f if line.strip() and not line.startswith('#')]
else:
    install_requires = []

setup(
    name='bangladesh-railway-cli',
    version='0.1.1',
    author='Md Minhazul Haque',
    author_email='mdminhazulhaque@gmail.com',
    description='A Python module for Bangladesh Railway\'s Ticketing System',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["bangladeshrailway"],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'bangladesh-railway-cli=bangladeshrailway.main:app',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)