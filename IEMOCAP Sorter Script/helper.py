import os

def mkdir(filename):
	try:
		os.mkdir(filename)
	except OSError: #file already exists
		pass

def listdir(filePath):
	for files in os.listdir(filePath):
		if files.startswith('.'): continue
		yield files


def deleter(deletePath):
	"""
	deal with the fact that we don't have a one purpose function for deletion
	"""
	try:
		os.listdir(deletePath)
	except OSError: #it's not a folder
		os.remove(deletePath)
	except IOError: #it doesn't exist
		print "No such folder: ", deletePath
	else:  
		shutil.rmtree(deletePath)




def mix(filePath):
	for files in os.listdir(filePath):
		if not files.endswith(".txt"): continue
		fileID = files[:-4]
		print fileID
		fileParser(os.path.join(filePath, files))
		exit()
