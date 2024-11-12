import urllib.request
import os
import matplotlib.pyplot as plt
from astropy.visualization import make_lupton_rgb
import astropy.units as u
from matplotlib import transforms
from cutout.tools import objloc




def decals(obj, rotation = None, wcsgrid = False, scalebar = False, savepath = None):
	"""
	Return DECaLS cutout. 
	"""

	coords = objloc(obj)
	lspath = '"https://www.legacysurvey.org/viewer/cutout.fits?ra='+coords.ra.deg+'&dec='+coords.dec.deg+'&layer=ls-dr9&pixscale=0.50"'
	os.system('curl -L '+lspath+' > "'+obj+'.fits"')

