import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='MatterPy',
    version='0.0.1',
    author='Siddhu Pendyala',
    author_email='elcientifico.pendyala@gmail.com',
    description='A Python library that deals with properties of matter.',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/PyndyalaCoder/MatterPy',
    project_urls = {
        "Bug Tracker": "https://github.com/PyndyalaCoder/MatterPy/issues"
    },
    license='MIT',
    packages=['MatterPy'],
    install_requires=['requests'],
)
