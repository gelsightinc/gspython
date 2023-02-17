from setuptools import setup, find_packages

packages = [package for package in find_packages() if package.startswith("gspython")]
setup(name="gspython",
	packages=packages
	)