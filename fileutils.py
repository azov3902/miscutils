import os
from os.path import isfile, join

################################################################################
def countFilesInDirectory(directory):
	# Counts the number of files (not including directories) in the given directory.
	return sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))

################################################################################
def fileExists(file_path):
	# Returns True if the file specified by file_path exists, False otherwise.
	return isfile(file_path)

################################################################################
def getFoldersInDirectory(directory = '.'):
	# Returns a list containing names of all the immediate subdirectories in the given directory (the current directory by default)
	return next(os.walk(directory))[1]