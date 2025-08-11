from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="friendlyetl",
    version="1.0.4",  # Use a new version for each upload
    author="Divith Raju",
    author_email="divithraju@gmail.com",
    description="A simple and lightweight ETL package for data pipelines using Python, Pandas, PySpark, and Hadoop",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Use your license here
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Database :: Front-Ends",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "sqlalchemy",
        "openpyxl"
    ],
)
