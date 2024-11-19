from astropy.coordinates import SkyCoord, name_resolve
from astropy.table import Table
import numpy as np

def objloc(obj):
	"""
	Get object location.

	Parameters:
		obj (str): Name or coordinates for object of interest. If coordinates, should be in
			HH:MM:SS DD:MM:SS or degree formats.
	Outputs:
		coords (astropy coordinates object)
	"""
	isname = False #check if obj is name or coordinates
	for s in obj:
		if s.isalpha():
			isname = True
			break

	if isname:
		coords = name_resolve.get_icrs_coordinates(obj)

	if not isname:
		if ':' in obj:
			coords = SkyCoord(obj, unit = [u.hour, u.deg])
		if not ':' in obj:
			coords = SkyCoord(obj, unit = u.deg)

	return coords


def getpanstarrsimages(ra,dec,filters="gri"):
	### COPIED FROM https://ps1images.stsci.edu/ps1image.html

	"""Query ps1filenames.py service to get a list of images

	ra, dec = position in degrees
	size = image size in pixels (0.25 arcsec/pixel)
	filters = string with filters to include
	Returns a table with the results
	"""

	service = "https://ps1images.stsci.edu/cgi-bin/ps1filenames.py"
	url = f"{service}?ra={ra}&dec={dec}&filters={filters}"
	table = Table.read(url, format='ascii')
	return table


def getpanstarrsurl(ra, dec, size=512, output_size=None, filters="gri", format="fits", color=False):
	### COPIED FROM https://ps1images.stsci.edu/ps1image.html
	
	"""Get URL for images in the table
	
	ra, dec = position in degrees
	size = extracted image size in pixels (0.25 arcsec/pixel)
	output_size = output (display) image size in pixels (default = size).
					output_size has no effect for fits format images.
	filters = string with filters to include
	format = data format (options are "jpg", "png" or "fits")
	color = if True, creates a color image (only for jpg or png format).
			Default is return a list of URLs for single-filter grayscale images.
	Returns a string with the URL
	"""
	
	if color and format == "fits":
		raise ValueError("color images are available only for jpg or png formats")
	if format not in ("jpg","png","fits"):
		raise ValueError("format must be one of jpg, png, fits")
	table = getpanstarrsimages(ra,dec,filters=filters)
	url = (f"https://ps1images.stsci.edu/cgi-bin/fitscut.cgi?"
		   f"ra={ra}&dec={dec}&size={size}&format={format}")
	if output_size:
		url = url + "&output_size={}".format(output_size)
	# sort filters from red to blue
	flist = ["yzirg".find(x) for x in table['filter']]
	table = table[np.argsort(flist)]
	if color:
		if len(table) > 3:
			# pick 3 filters
			table = table[[0,len(table)//2,len(table)-1]]
		for i, param in enumerate(["red","green","blue"]):
			url = url + "&{}={}".format(param,table['filename'][i])
	else:
		urlbase = url + "&red="
		url = []
		for filename in table['filename']:
			url.append(urlbase+filename)
	return url
