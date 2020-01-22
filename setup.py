import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis-python-souravdlboy",
    version="0.0.1",
    author="sourav kumar",
    author_email="sauravkumarsct@gmail.com",
    description="Python package for TOPSIS algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/souravs17031999/topsis-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
