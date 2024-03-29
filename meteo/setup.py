from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
 

setup(
    name="meteo",
    version="1.0.0",
    description="A Python package to get weather reports for any location.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/oumar90/meteo",
    author="Oumar Djimé Ratou",
    author_email="oudjira90@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["meteo"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "meteo=meteo.cli:main",
        ]
    },
)