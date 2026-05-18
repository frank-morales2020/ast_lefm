from setuptools import setup, find_packages

setup(
    name="ast_lefm",
    version="1.0.0",
    author="Frank Morales Aguilera",
    author_email="frank.morales@sovereignml.ai",
    description="Arithmetic Spectral Theory and L-EFM Operator for Prime Quantification, RH Proof, and AI Safety",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/frank-morales2020/ast_lefm",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "mpmath>=1.3.0",
        "pytest>=7.0.0",
    ],
)