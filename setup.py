from setuptools import setup, find_packages

setup(
    name='bangladesh-railway-cli',
    version='0.1.0',
    author='Md Minhazul Haque',
    author_email='mdminhazulhaque@gmail.com',
    description='A Python module for Bangladesh Railway\'s Ticketing System',
    packages=["bangladeshrailway"],
    install_requires=[
        'requests',
        'tabulate',
        'click',
    ],
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