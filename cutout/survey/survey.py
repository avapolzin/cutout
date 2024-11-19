import os
import matplotlib.pyplot as plt
from astropy.visualization import make_lupton_rgb
from cutout.tools import objloc, getpanstarrsurl
from astropy.io import fits
from astropy.wcs import WCS
from unagi.task import hsc_cutout
from unagi import hsc



def decals(obj, wcsgrid = False, scalebar = False, labelimg = False, savepath = None, savefits = False):
	"""
	Return RGB DECaLS cutout from g, r, and z band imaging.
	Pixel scale is 0.26"/pix.

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
	fname = obj.replace(' ', '').replace(':','')+'.fits'
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



def hscssp(obj, wcsgrid = False, scalebar = False, labelimg = False, savepath = None, savefits = False):
	"""
	Return RGB HSC SSP cutout from g, r, and i band imaging.
	Pixel scale is 0.168"/pix.

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
	fname = obj.replace(' ', '').replace(':', '')

	pdr = hsc.Hsc(dr='pdr2', rerun='any',config_file=None)

	g = hsc_cutout(coords, cutout_size=256*0.168*u.arcsec, filters='g', archive=pdr, save_output=savefits)
	r = hsc_cutout(coords, cutout_size=256*0.168*u.arcsec, filters='r', archive=pdr, save_output=savefits)
	i = hsc_cutout(coords, cutout_size=256*0.168*u.arcsec, filters='i', archive=pdr, save_output=savefits)
	

	fig = plt.figure(figsize = (5, 5))

	rgb = make_lupton_rgb(0.75*i[1].data, 1.*r[1].data, 1.5*g[1].data, stretch=0.5, Q=5)

	if wcsgrid:
		hscwcs = WCS(g[1].header)
		plt.subplot(projection=hscwcs)
		plt.grid(color='gray', ls='dashed')
		plt.xlabel('RA')
		plt.ylabel('Dec')

	plt.imshow(rgb, origin = 'lower', interpolation = 'none')

	if not wcsgrid:
		plt.axis('off')

	if scalebar:
		x, y = g[1].data.shape
		npix = scalebar/0.168 #arcsec
		plt.plot([512/2 - npix/2, 512/2 + npix/2], [512/8]*2, color = 'white')
		plt.text(512/2 - 40, 512/8 + 5, s = '%i arcsec'%scalebar, color = 'white')

	if labelimg:
		plt.text(10, 480, s = obj, color = 'white')

	if savepath:
		fig.savefig(savepath, bbox_inches = 'tight', dpi = 200)

	plt.show()

	if savefits:
		os.system('mv pdr2*_g.fits '+fname+'_g.fits')
		os.system('mv pdr2*_r.fits '+fname+'_r.fits')
		os.system('mv pdr2*_i.fits '+fname+'_i.fits')


def panstarrs(obj, wcsgrid = False, scalebar = False, labelimg = False, savepath = None, savefits = False):
	"""
	Return RGB Pan-STARRS1 cutout from g, r, and i band imaging.
	Pixel scale is 0.25"/pix.

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
	fname = obj.replace(' ', '').replace(':','')
	psurl = getpanstarrsurl(coords.ra.deg, coords.dec.deg)

	if savefits:
		for i, f in enumerate(['i', 'r', 'g']):
			os.system('wget -O '+fname+'_%s.fits'%f + ' "'+psurl[i]+'"')

	fig = plt.figure(figsize = (5, 5))

	g_ = fits.open(psurl[2])
	r_ = fits.open(psurl[1])
	i_ = fits.open(psurl[0])

	rgb = make_lupton_rgb(0.5*i_[0].data, 0.65*r_[0].data, 1.*g_[0].data, stretch=500, Q=8)

	if wcsgrid:
		pswcs = WCS(g_[0].header, g_)
		plt.subplot(projection=pswcs)
		plt.grid(color='gray', ls='dashed')
		plt.xlabel('RA')
		plt.ylabel('Dec')

	plt.imshow(rgb, origin = 'lower', interpolation = 'none')

	if not wcsgrid:
		plt.axis('off')

	if scalebar:
		x, y = g_[0].data.shape
		npix = scalebar/0.25 #arcsec
		plt.plot([512/2 - npix/2, 512/2 + npix/2], [512/8]*2, color = 'white')
		plt.text(512/2 - 40, 512/8 + 5, s = '%i arcsec'%scalebar, color = 'white')

	if labelimg:
		plt.text(10, 480, s = obj, color = 'white')

	if savepath:
		fig.savefig(savepath, bbox_inches = 'tight', dpi = 200)

	plt.show()












