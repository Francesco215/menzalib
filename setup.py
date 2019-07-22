import setuptools

with open("README.md", "r", encoding="latin1") as fh:
    long_description = fh.read()

setuptools.setup(
    name="texpy",
    version="1.0.0",
    author=["Lorenzo Cavuoti", "Francesco Sacco"],
    author_email="francesco215@live.it",
    description="Funzioni utili per lab3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Francesco215/menzalib",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
