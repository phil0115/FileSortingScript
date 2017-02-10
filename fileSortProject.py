import shutil, os, re

#TO-DO: 1)Make modular
#       2)Find way to do relative path

#Grab file extension to organize

while True:
    dirInput = input("What is the absolute path to the folder you would like to organize?: ")
    os.chdir(dirInput)
   
    while True:
        fileList = os.listdir('.')
        extList = [ ]
        for file in fileList:
            try:
                name, ext = file.split('.')
            except ValueError:
                continue
        
            if not (ext in extList):
                extList.append(ext)
    
        print("The available file extensions are: " + str(extList))
        userInput = input("Please put the file extension you would like to search for: ")

        #Make search pattern out of input
        filePattern = re.compile(r'^(.*?).' + re.escape(userInput.lower()))

        #Make new folder for files
        absWorkingDir = os.path.abspath('.')
        newFolder = os.path.join(absWorkingDir, userInput.upper() + 's')
        
        #If folder already exists exit
        if (userInput in extList):
            try:
                os.mkdir(newFolder)
                
            except FileExistsError:
                print('The folder name %ss already exists, exiting...' % userInput.upper())
                exit()
        else:
            print("No files with that extension...")
            break

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

        exitInput = input("Would you like to choose another file extension? Y/N: ")

        if exitInput.lower() == 'n':
            break
        else:
            continue

    dirExit = input("Would you like to choose another directory? Y/N: ")
    if dirExit.lower() == 'n':
        break
    else:
        continue
