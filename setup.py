from setuptools import find_packages, setup

setup(
    name="textSummarizer",
    version="0.0.0",
    author="Bharathikannan",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)