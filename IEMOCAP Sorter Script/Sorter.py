#Sorter.py
import os
import shutil
from helper import mkdir, listdir

os.chdir("..")
currdir  = os.getcwd()
print currdir



def fileParser(filePath):

	emotionDict = {}
	
	with open(filePath, 'r') as f:
		for line in f:
			tokens = line.split("\t")
			
			if len(tokens) == 4:
				utteranceID, emotion = line.split("\t")[1:3]
				emotionDict[utteranceID] = emotion

	return emotionDict

def mover(filePath, emotion):
	filename = filePath.rsplit("/",1)[1]
	speakerID = filename.split("_",1)[0]
	print filename, speakerID, emotion
	if not emotion == "xxx": 
		mkdir(os.path.join("CleanedIEMOCAP", emotion))
		mkdir(os.path.join("CleanedIEMOCAP", emotion, speakerID))
		shutil.move(filePath, os.path.join("CleanedIEMOCAP", emotion, speakerID, filename))




def refactor():
	mkdir("CleanedIEMOCAP")

	for i in range(1,6):
		sesh = "Session{}".format(i)
		for convos in listdir(os.path.join(currdir, sesh, "wav")):
			speakerID = convos.split("_")[0]
			
			transcriptionLoc = os.path.join(currdir, sesh, "Eval", convos+".txt")
			emotionDict = fileParser(transcriptionLoc)
			
			currLoc = os.path.join(currdir, sesh, "wav", convos)
			for utteranceWav in listdir(currLoc):	
				utteranceID = utteranceWav.rstrip(".wav")
				mover(os.path.join(currLoc, utteranceWav), emotionDict[utteranceID])



def stats():
	statEmotions = {}
	for i in range(1,6):
		sesh = "Session{}".format(i)
		for convos in listdir(os.path.join(currdir, sesh, "Eval")):
			if not convos.endswith(".txt"): continue
			emotionDict = fileParser(os.path.join(currdir, sesh, "Eval", convos))
			for emotions in emotionDict.values():
				try:
					statEmotions[emotions]+=1
				except KeyError:
					statEmotions[emotions] = 1

	for k,v in statEmotions.iteritems():
		print "{}: {}".format(k,v)


if __name__ == '__main__':
	
	refactor()
	stats()