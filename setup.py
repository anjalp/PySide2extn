import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PySide2extn", # Replace with your own username
    version="1.0.0",
    author="ANJAL.P",
    author_email="opensource.anj.official@gmail.com",
    description="PySide2extn is an Open Source Python Programming language extension for PySide2, which greatly enhances the capability of the PySide2 library with extra widgets and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anjalp/PySide2extn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["PySide2"],
)