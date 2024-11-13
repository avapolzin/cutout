import os
import matplotlib.pyplot as plt
from astropy.visualization import make_lupton_rgb
from cutout.tools import objloc
from astropy.io import fits
from astropy.wcs import WCS
from unagi.task import hsc_cutout



def decals(obj, wcsgrid = False, scalebar = False, labelimg = False, savepath = None, savefits = False):
	"""
	Return RGB DECaLS cutout from g, r, and z band imaging.

	Parameters:
		obj (str): Name or coordinates for object of interest. If coordinates, should be in
			HH:MM:SS DD:MM:SS or degree formats. Names must be resolvable in SIMBAD.
		wcsgrid (bool): If True, show WCS grid on RGB image.
		scalebar (float): Length of scalebar in arcseconds. If specified, shown on image.
		labelimg (bool): If True, show obj string on image.
		savepath (str): Path specifying where to save image. If not specified, image is not saved.
		savefits (bool): If True, retain downloaded .fits file.

	Returns:
		If savepath, saves image to specified location. If savepath not specified, just displays image.
	"""

	coords = objloc(obj)
	fname = obj.replace(' ', '')+'.fits'
	lspath = '"https://www.legacysurvey.org/viewer/cutout.fits?ra='+str(coords.ra.deg)+'&dec='+str(coords.dec.deg)+'&layer=ls-dr9&pixscale=0.26&size=512"'
	os.system('curl -L '+lspath+' > "'+fname+'"')

	fig = plt.figure(figsize = (5, 5))

	img = fits.open(fname)

	g = img[0].data[0, :, :]
	r = img[0].data[1, :, :]
	z = img[0].data[2, :, :]

	rgb = make_lupton_rgb(0.75*z, 1.1*r, 1.75*g, stretch=0.1, Q=5)

	if wcsgrid:
		lswcs = WCS(img[0].header, img)
		plt.subplot(projection=lswcs.slice(view = [1]))
		plt.grid(color='gray', ls='dashed')
		plt.xlabel('RA')
		plt.ylabel('Dec')

	plt.imshow(rgb, origin = 'lower', interpolation = 'none')
	plt.gca().invert_xaxis()

	if not wcsgrid:
		plt.axis('off')

	if scalebar:
		x, y = g.shape
		npix = scalebar/0.26 #arcsec
		plt.plot([512/2 - npix/2, 512/2 + npix/2], [512/8]*2, color = 'white')
		plt.text(512/2 - 40, 512/8 + 5, s = '%i arcsec'%scalebar, color = 'white')

	if labelimg:
		plt.text(10, 480, s = obj, color = 'white')

	if savepath:
		fig.savefig(savepath, bbox_inches = 'tight', dpi = 200)

	plt.show()


	if not savefits:
		os.system('rm '+fname)



def hscssp(obj, wcsgrid = False, scalebar = False, savepath = None, savefits = False):
	"""
	Return RGB HSC SSP cutout.

	Parameters:
		obj (str): Name or coordinates for object of interest. If coordinates, should be in
			HH:MM:SS DD:MM:SS or degree formats. Names must be resolvable in SIMBAD.
		wcsgrid (bool): If True, show WCS grid on RGB image.
		scalebar (float): Length of scalebar in arcseconds. If specified, shown on image.
		labelimg (bool): If True, show obj string on image.
		savepath (str): Path specifying where to save image. If not specified, image is not saved.
		savefits (bool): If True, retain downloaded .fits file.

	Returns:
		If savepath, saves image to specified location. If savepath not specified, just displays image.
	"""

	coords = objloc(obj)
	fname = obj.replace(' ', '')+'.fits'
	
	## USING UNAGI

	fig = plt.figure(figsize = (5, 5))

	img = fits.open(fname)

	g = img[0].data[0, :, :]
	r = img[0].data[1, :, :]
	i = img[0].data[2, :, :]

	rgb = make_lupton_rgb(0.75*z, 1.1*r, 1.75*g, stretch=0.1, Q=5)

	if wcsgrid:
		lswcs = WCS(img[0].header, img)
		plt.subplot(projection=lswcs.slice(view = [1]))
		plt.grid(color='gray', ls='dashed')
		plt.xlabel('RA')
		plt.ylabel('Dec')

	plt.imshow(rgb, origin = 'lower', interpolation = 'none')
	plt.gca().invert_xaxis()

	if not wcsgrid:
		plt.axis('off')

	if scalebar:
		x, y = g.shape
		npix = scalebar/0.26 #arcsec
		plt.plot([512/2 - npix/2, 512/2 + npix/2], [512/8]*2, color = 'white')
		plt.text(512/2 - 40, 512/8 + 5, s = '%i arcsec'%scalebar, color = 'white')

	if labelimg:
		plt.text(10, 480, s = obj, color = 'white')

	if savepath:
		fig.savefig(savepath, bbox_inches = 'tight', dpi = 200)

	plt.show()


	if not savefits:
		os.system('rm '+fname)


def panstarrs():

	## could do gri or grz
	## might take a bit more work, but will do this too
	# https://ps1images.stsci.edu/ps1image.html
	# https://outerspace.stsci.edu/display/PANSTARRS/PS1+Image+Cutout+Service#PS1ImageCutoutService-Scriptedimagedownloadsandimagecutoutextractions





