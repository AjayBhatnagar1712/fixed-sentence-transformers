from setuptools import setup, find_packages

setup(
    name="sentence-transformers",
    version="2.2.2",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Ajay Bhatnagar",
    description="Custom fixed version of sentence-transformers without sentencepiece.",
)
