import os
import pathlib
from setuptools import setup, find_packages

# python setup.py sdist bdist_wheel
# twine upload --skip-existing dist/*

# get __version__ from _version.py
ver_file = os.path.join("skpipes", "_version.py")
with open(ver_file) as f:
    exec(f.read())

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.rst").read_text()
setup(
    name="scikit-pipes",
    version=__version__,
    description="Scikit-Learn useful pre-defined Pipelines Hub",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/rodrigo-arenas/scikit-pipes",
    author="Rodrigo Arenas",
    author_email="rodrigo.arenas456@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        "Documentation": "https://scikit-pipes.readthedocs.io/en/stable/",
        "Source Code": "https://github.com/rodrigo-arenas/scikit-pipes",
        "Bug Tracker": "https://github.com/rodrigo-arenas/scikit-pipes/issues",
    },
    packages=find_packages(
        include=["skpipes", "skpipes.*"], exclude=["*tests*"]
    ),
    install_requires=[
        "scikit-learn>=0.21.3",
        "numpy>=1.14.5",
    ],
    python_requires=">=3.7",
    include_package_data=True,
)
