import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="posts",
    version="0.0.1",
    author="Jamie Omondi",
    author_email="cruiseomondi90@gmail.com",
    description="A simple post api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[]  # add any additional packages that
)
