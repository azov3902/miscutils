from __future__ import division, print_function
from miscutils import *

############################################################################################
def println():
	print("------------------------------------------------")

############################################################################################
def pause():
	raw_input("Hit a key to continue...")
	return

############################################################################################
def printHeader(str):
	println()
	print(str)
	println()

############################################################################################
def hhmmss(t):
	""" Return the hours, minutes and seconds corresponding to an input period specified in seconds. """
	hh = (t - np.remainder(t, 3600)) / 3600
	mmss = np.remainder(t, 3600)

	mm = (mmss - np.remainder(mmss, 60)) / 60
	ss = np.remainder(mmss, 60)

	return hh, mm, ss