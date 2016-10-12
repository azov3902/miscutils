from __future__ import division
from miscutils import *
from matplotlib.ticker import FormatStrFormatter

############################################################################################
def colorbar(plot=None):
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
	subplot=None,
	colorbar_on=False):
	""" Displays an input image given a plate scale. """
	h, w = im.shape
	if plt.is_numlike(subplot):
		plt.subplot(subplot)	
	if title:
		plt.title(title)
	if plate_scale_as_px != 1:
		# plt.xlabel('arcsec')
		# plt.ylabel('arcsec')
		plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%d\"'))
		plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d\"'))
	plt.imshow(im, extent = np.array([-w/2, w/2, -h/2, h/2]) * plate_scale_as_px)
	if colorbar_on:
		colorbar()
	plt.show()

############################################################################################
def azElPlot(az_rad, el_rad,
	linespec='ro'):
	""" Generates a polar plot of azimuth and elevation. """
	el_deg = np.rad2deg(el_rad)
	zenith_deg = 90 - el_deg
	
	newfigure(1,1)
	ax = plt.subplot(111, projection='polar')
	ax.plot(az_rad, zenith_deg, linespec)
	ax.set_yticks(range(0, 90, 10))
	ax.set_yticklabels(map(str, range(90, 0, -10)))

	return ax


