from setuptools import setup, find_packages

page_description = open("README.md", "r").read()
requirements = open("requirements.txt", "r").read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author='Luiz F C Pereira',
    description="Image processing using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Moskbr/image-processing-package",
    packages=find_packages(),
    requires=requirements
)