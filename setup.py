from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mayur/__init__.py
from mayur import __version__ as version

setup(
	name="mayur",
	version=version,
	description="Mayur ",
	author="Mayur",
	author_email="mayur@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
