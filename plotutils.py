from __future__ import division
from miscutils import *
from matplotlib.ticker import FormatStrFormatter
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import ticker
# import ipdb

################################################################################
def colorbar(plot=None,nticks=5):
	""" Makes a nicely-sized colorbar. """
	if plot:
		cb = plt.colorbar(plot,fraction=COLORBAR_FRACTION, pad=COLORBAR_PAD)
	else:
		cb = plt.colorbar(fraction=COLORBAR_FRACTION, pad=COLORBAR_PAD)
	# Set the number of ticks on the colorbar.
	tick_locator = ticker.MaxNLocator(nbins=nticks)
	cb.locator = tick_locator
	cb.ax.yaxis.set_major_locator(ticker.AutoLocator())
	cb.update_ticks()
	plt.show()

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
	generate_cmap=False,
	N=+15,
	M=-5,
	vmin=None,
	vmax=None,
	cmap='cubehelix',
	nticks=5,
	colorbar_on=True):
	""" Displays an input image given a plate scale. """
	if generate_cmap:
		cmap, vmax, vmin = scale_colorbar(im, N, M)
	if newwindow:
		newfigure()
	h, w = im.shape
	plt.subplot(subplot)	
	if title:
		plt.title(title)
	if plate_scale_as_px != 1:
		plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%g\"'))
		plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%g\"'))
	plt.imshow(
		im, 
		extent = np.array([-w/2, w/2, -h/2, h/2]) * plate_scale_as_px,
		vmin=vmin,
		vmax=vmax,
		cmap=cmap
		)
	if colorbar_on:
		colorbar(nticks=nticks)
	plt.show()

	return cmap, vmax, vmin

################################################################################
def scale_colorbar(im,
	N=+15,
	M=-5):
	"""
		Create a colormap which scales an image such that the maximum value is 
		N * sigma and the minimum is -M * sigma with the colourmap centred 
		about the median value of the pixel values in the image.
	"""
	N=np.abs(N)
	M=np.abs(M)
	sigma = np.std(im)
	median = np.median(im)
	vmax = median + N * sigma
	vmin = median - M * sigma
	midpoint_pc = M / (M + N)

	cdict = {
	         'red':  ((0.0, 0.0, 0.0),
	                   (midpoint_pc, 70/255, 70/255),
	                   (1.0, 1.0, 1.0)),
			'green': ((0.0, 0.0, 0.0),
	                   (midpoint_pc, 0/255, 0/255),
	                   (1.0, 1.0, 1.0)),
	         'blue':   ((0.0, 0.0, 0.0),
	                   (midpoint_pc, 130/255, 130/255),
	                   (1.0, 1.0, 1.0))
	        }


	cmap = LinearSegmentedColormap('this_cmap', cdict)

	return cmap, vmax, vmin

################################################################################
def azel_plot(az_rad, el_rad,
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


