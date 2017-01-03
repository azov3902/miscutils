import os
from os.path import isfile, join

################################################################################
def count_files_in_dir(directory):
	# Counts the number of files (not including directories) in the given 
	# directory.
	return sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))

################################################################################
def file_exists(file_path):
	# Returns True if the file specified by file_path exists, False otherwise.
	return isfile(file_path)

################################################################################
def get_folders_in_dir(directory = '.'):
	# Returns a list containing names of all the immediate subdirectories in the 
	# given directory (the current directory by default)
	return next(os.walk(directory))[1]

################################################################################
def create_dir(directory):
	# Creates the directory if it does not already exist.
	if not os.path.exists(directory):
		os.makedirs(directory)
	return