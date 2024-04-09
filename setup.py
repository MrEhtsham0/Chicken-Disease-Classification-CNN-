import setuptools

with open('README.md','r',encoding='utf-8') as file:
    long_description = file.read()


__version__ = '0.0.0'

REPO_NAME = "Chicken-Disease-Classification-CNN-"
SRC_REPO = "Chicken_classifier_CNN"
AUTHOR_USER_NAME ="MrEhtsham0",
AUTHOR_EMAIL = "mr_ehtsham@yahoo.com",

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description="CNN model for chicken",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={
    'Bug Tracker':f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")


)