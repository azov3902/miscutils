import os
from os.path import isfile, join, splitext
import pdb

################################################################################
def countFilesInDirectory(directory):
	# Counts the number of files (not including directories) in the given directory.
	return sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))

################################################################################
def file_exists(file_path):
	# Returns True if the file specified by file_path exists, False otherwise.
	return isfile(file_path)

################################################################################
def getFoldersInDirectory(directory = '.'):
	# Returns a list containing names of all the immediate subdirectories in the given directory (the current directory by default)
	return next(os.walk(directory))[1]

############################################################################################
def appendNumberToFilename(path):
	# Appends a number (e.g. '001' or '002' etc.) if there is an existing file in the given directory. 
 	
 	try:
 		path.index('.')
 	except:
 		print("WARNING: fname must contain an extension, otherwise I cannot change it! Instead I will save over file '{}'...".format(path))
		return path
	
	# Get the extension and the filename.
	fname, ext = splitext(path)

	# If the file doesn't exist and does not end in a number, then we append a number before returning the path.
	if not isfile(path):
		if not fname[-1].isdigit():
			fname = fname + '_001'
	else:
		while isfile(path):
			# Then append a number to the file.
			endchar = fname[-1]
			if endchar.isdigit():
				s = list(fname)
				s[-1] = str(int(endchar) + 1)
				fname = "".join(s)
			else:
				fname = fname + '_001'
			path = fname + ext
	path = fname + ext
	print("Saving to file '{}'...".format(path))
	return path
	
