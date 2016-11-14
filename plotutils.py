from __future__ import division
from miscutils import *
from matplotlib.ticker import FormatStrFormatter

################################################################################
def colorbar(plot=None):
	""" Makes a nicely-sized colorbar. """
	if plot:
		plt.colorbar(plot,fraction=COLORBAR_FRACTION, pad=COLORBAR_PAD)
	else:
		plt.colorbar(fraction=COLORBAR_FRACTION, pad=COLORBAR_PAD)

################################################################################
def newfigure(height=1,width=1):
	""" Makes a nicely-sized figure with width:height ratio = x:y. """
	return plt.figure(figsize=(width*FIGSIZE,height*FIGSIZE))

################################################################################
def astroimshow(im, 
	newwindow=False,
	title=None,
	plate_scale_as_px=1, 
	subplot=111,
	vmin=None,
	vmax=None,
	colorbar_on=False):
	""" Displays an input image given a plate scale. """
	if newwindow:
		newfigure()
	h, w = im.shape
	plt.subplot(subplot)	
	if title:
		plt.title(title)
	if plate_scale_as_px != 1:
		plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f\"'))
		plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f\"'))
	plt.imshow(
		im, 
		extent = np.array([-w/2, w/2, -h/2, h/2]) * plate_scale_as_px,
		vmin=vmin,
		vmax=vmax,
		cmap='cubehelix'
		)
	if colorbar_on:
		colorbar()
	plt.show()

################################################################################
def azElPlot(az_rad, el_rad,
	title='',
	linespec='ro',
	label='',
	subplot=111):
	""" Generates a polar plot of azimuth and elevation. """
	el_deg = np.rad2deg(el_rad)
	zenith_deg = -el_deg
	
	# newfigure(1,1)
	ax = plt.subplot(subplot, projection='polar')
	ax.plot(az_rad, zenith_deg, linespec, label=label)
	ax.plot(np.linspace(0, 2*np.pi, 360), np.zeros(360), 'k')
	ax.set_yticks(range(-90, 90, 10))
	ax.set_yticklabels(map(str, range(90, -90, -10)))
	ax.set_title(title)
	
	return ax


