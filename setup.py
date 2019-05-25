from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent

with (here / 'README.rst').open() as f:
    long_description = f.read()

setup(
    name='pyconweb-2019-workshop',
    version='2019.05.26',
    description="Material for my PyConWeb 2019 workshop.",
    long_description=long_description,
    author="Alexandre Figura",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'flask>=1.0',
        'flask-sqlalchemy>=2.4',
        'factory-boy>=2.12',
        'psycopg2>=2.8',
        'sqlalchemy>=1.3',
    ],
    entry_points={
        'console_scripts': [
            'workshop-server = workshop.demo:server',
        ],
    },
)
