#auto_render.py
#Renders all blender files in the current directory as animations. Saves animation sequences to separate folders.
#David Schommer 2015

#IMPROVEMENTS:
#1)Make a parent folder titled 'renders' (make sure this file doesn't already exist, if so, name it 'renders-2', check, and keep iterating up until a correct file name is given)
#put each blender file's render folder in this 'renders' parent folder

import os
import subprocess

#os.path.abspath(__file__) gives the directory of the python file + file name 
#os.path.dirname normalizes this (takes out the auto_render.py)
currentPath = os.path.dirname(os.path.abspath(__file__))

#path for the Blender application
blenderPath = r'/Applications/blender.app/Contents/MacOS'

#create directory for render files and return renderPath directory
def makeRenderDirectory(blenderFile):
	#save current directory + file name
	filePath = os.path.abspath(blenderFile)

	#create new directory for this blender file's render
	#.split: maxsplit = 1 (only split once); [0]: take the front portion
	nameOfBlenderFile = blenderFile.split('.blend', 1)[0]
	#CHECK IF FILE EXISTS BEFORE CREATING?
	renderPath = currentPath + r'/' + nameOfBlenderFile + '_Render' 

	#this one is not necessary (delete?):
	#os.makedirs(renderPath)

	return renderPath + r'/'

#def createRendersParentDirectory():
	#check if file name already exists
	#then, 
	#rendersParentPath = currentPath + r'/renders'
	#os.makedirs(rendersParentPath)

#createRendersParentDirectory()

for blenderFile in os.listdir(currentPath):
	#make sure file extension is .blend
	if blenderFile.lower().endswith('.blend'):
		renderPath = makeRenderDirectory(blenderFile)
		filePath = os.path.abspath(blenderFile)
		subprocess.Popen(r'./blender -b ' + filePath + r' -x 1 -o ' + renderPath + r' -F MOVIE -a', cwd = blenderPath, shell=True)
		


		


