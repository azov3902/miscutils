from __future__ import division
from miscutils import *

############################################################################################
def colourbar(plot=None):
	""" Makes a nicely-sized colorbar. """
	if plot:
		plt.colorbar(plot,fraction=COLORBAR_FRACTION, pad=COLORBAR_PAD)
	else:
		plt.colorbar(fraction=COLORBAR_FRACTION, pad=COLORBAR_PAD)

############################################################################################
def newfigure(height=1,width=1):
	""" Makes a nicely-sized figure with width:height ratio = x:y. """
	return plt.figure(figsize=(width*FIGSIZE,height*FIGSIZE))

############################################################################################
def astroimshow(im, 
	title=None,
	plate_scale_as_px=1, 
	subplot=None):
	""" Displays an input image given a plate scale. """
	h, w = im.shape
	if plt.is_numlike(subplot):
		plt.subplot(subplot)	
	if title:
		plt.title(title)
	if plate_scale_as_px != 1:
		plt.xlabel('arcsec')
		plt.ylabel('arcsec')
	plt.imshow(im, extent = np.array([-w/2, w/2, -h/2, h/2]) * plate_scale_as_px)
	plt.show()

