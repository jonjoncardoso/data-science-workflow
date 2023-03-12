from setuptools import setup, find_packages

setup(
    name="pkg_name",
    description="WIP",
    long_description=(
        "WIP"
    ),
    version="0.0.999",
    py_modules=["pkg_name"],
    author="",
    keywords=[""],
    install_requires=[
        "numpy",
        "pandas"
    ],
    packages=find_packages(),
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)