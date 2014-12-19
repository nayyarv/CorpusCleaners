import os
import shutil
from helper import deleter, listdir
# print os.listdir(os.getcwd())

os.chdir("..")
currdir = os.getcwd()




def extraneousRemoval():
	"""
	Get rid of the shit that we have inside the IEMOCAP database
	"""

	for sesh in os.listdir(currdir):
		if not sesh.startswith("Session"): continue
		print sesh

		# "as".

		for folder in olistdir(os.path.join(currdir, sesh, "dialog")):
			if not folder.startswith("EmoEvaluation"):
				deletePath = os.path.join(currdir, sesh, "dialog", folder)
				deleter(deletePath)

		for folder in listdir(os.path.join(currdir, sesh, "sentences")):
			if not folder.startswith("wav"):
				deletePath = os.path.join(currdir, sesh, "sentences", folder)
				deleter(deletePath)
				

def minorRefactor():
	"""
	Put everything together, remove extra folders
	"""
	for sesh in os.listdir(currdir):
		if not sesh.startswith("Session"): continue
		try:
			shutil.move(os.path.join(currdir, sesh, "sentences", "wav"), 
						os.path.join(currdir, sesh, "wav"))
			shutil.move(os.path.join(currdir, sesh, "dialog", "EmoEvaluation"), 
						os.path.join(currdir, sesh, "Eval"))
		except IOError:
			pass # it's been clceaned

		try:
			shutil.rmtree(os.path.join(currdir, sesh, "sentences"))
			shutil.rmtree(os.path.join(currdir, sesh, "dialog"))
		except OSError:
			pass
			




if __name__ == '__main__':
	extraneousRemoval() # remove extraneous files
	minorRefactor()