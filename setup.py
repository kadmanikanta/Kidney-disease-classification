import setuptools

with open("README.md", "r",encoding =" utf-8" ) as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Kidney-disease-classification"
AUTHOR_NAME = "kadManikanta"
SRC_REPO = "CNN_CLAASIFICER"
AUTHOR_EMAIL = "kadambamanikanta311@gmail.com"


setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email= AUTHOR_EMAIL,
    description="A classifier for kidney disease using Convolutional Neural Networks (CNN) ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    license="MIT License",
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where =" src ")
)
