# Python program to organize files of a directory
import os
import sys
import shutil


def OrganizeDirectory(sourcePath, extensionToDir):
    if(not os.path.exists(sourcePath)):
        print(f"The source directory {sourcePath} does not exist !!\n")
    else:
        for file in os.listdir(sourcePath):
            file = os.path.join(sourcePath, file)

            #ignore if its not a file but a dir
            if os.path.isdir(file):
                continue

            rootPath, fileExtension = os.path.splitext(file) #splits root path to file and extension
            #eg: C://witcher//mods//settings.txt to  C://witcher//mods//settings and .txt
            fileExtension = fileExtension[1:] #remove the dot

            #if the given file extension is in the dictionary
            if(fileExtension in extensionToDir):

                # store the corresponding destination dir name
                destinationName = extensionToDir[fileExtension]
                destinationPath = os.path.join(sourcePath, destinationName)

                #if destination does not exist already, create it
                if(not os.path.exists(destinationPath)):
                    print(f"Creating new directory for {destinationName}!!")

                    #create new directory
                    os.makedirs(destinationPath)
                
                #move the file
                shutil.move(file, destinationPath)

def main():

    if(len(sys.argv) != 2): #if number of command line arguements != 2
        print("Usage: <program><source path directory>")
        return
    
    sourcePath = sys.argv[1]

    extensionToDir = {}
    extensionToDir["mp3"] = "Audio"
    extensionToDir["jpg"] = "Images"
    extensionToDir["zip"] = "Archives"
    extensionToDir["exe"] = "Softwares"
    extensionToDir["pdf"] = "Docs"
    extensionToDir["epub"] = 'Docs'
    extensionToDir["ipynb"] = "Python Notebooks"


    print("")
    OrganizeDirectory(sourcePath, extensionToDir)


if __name__ == "__main__":
    main()
