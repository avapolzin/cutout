import setuptools

setuptools.setup(
	name = "cutout",
	version = "0.2",
	author = "Ava Polzin",
	author_email = "apolzin@uchicago.edu",
	description = "Survey cutouts plotted directly; no user choices, just plotting!",
	packages = ["cutout", "cutout/survey", "cutout/tools"],
	url = "https://github.com/avapolzin/cutout",
	license = 'MIT',
	classifiers = [
		"Development Status :: 4 - Beta",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Topic :: Scientific/Engineering :: Astronomy",
		"Topic :: Scientific/Engineering :: Physics"],
	python_requires = ">=3",
	install_requires = ["astropy", "matplotlib", "numpy", "unagi"]
)

#more updated (development version of) unagi can be installed by replacing
# "unagi" with "unagi @ git+https://github.com/dr-guangtou/unagi"