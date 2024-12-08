from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

exec(open('sonderPyvis/_version.py').read())
setup(
    name="sonderPyvis",
    version="1.0.0",
    description="A customized version of Python network graph visualization(pyvis) library for Sonder",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/yeabb/sonderPyvis",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "jinja2 >= 2.9.6",
        "networkx >= 1.11",
        "ipython >= 5.3.0",
        "jsonpickle >= 1.4.1"
    ],
    python_requires=">3.6",
)
