import shutil, os, re

#TO-DO: 1)Add better folder naming
#       2)Add better error catching
#       3)Add ability to change directory
#       4)Make modular

#Grab file extension to organize
userInput = input("Please put the file extension you would like to search for: ")

#Make search pattern out of input
filePattern = re.compile(r'^(.*?).' + re.escape(userInput.lower()))

#Make new folder for files
absWorkingDir = os.path.abspath('.')
newFolder = os.path.join(absWorkingDir, userInput.upper() + 's')

#If folder already exists exit
try:
    os.mkdir(newFolder)
    
except FileExistsError:
    print('The folder name %ss already exists, exiting...' % userInput.upper())
    exit()

#Run through every file in the directory
for files in os.listdir('.'):
    mo = filePattern.search(files)

    if mo == None:
        continue
    
    #Make a new path for found files
    newPath = os.path.join(absWorkingDir, mo.group())

    #Display found files and move them to folder                     
    print("Found %s moving to %s..." % (mo.group(), newFolder))
    shutil.move(newPath, newFolder)
