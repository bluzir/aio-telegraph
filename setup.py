import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aio_telegraph",
    version="1.0.0",
    author="Vladislav Kooklev",
    author_email="kouklevv@gmail.com",
    description="A tiny aio library for telegra.ph API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bluzir/aio-telegraph",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

