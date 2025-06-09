
from setuptools import setup

setup(
    name="sentence-transformers",
    version="2.2.2",
    install_requires=[
        "torch",
        "transformers>=4.6.0",
        "scikit-learn",
        "numpy",
        "scipy",
        "tqdm",
        "Pillow",
        "requests",
        "tokenizers>=0.10.3",
    ],
)
