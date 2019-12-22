#!/usr/bin/env python3
#Change Wallpaper(CWP) is a small script to change the wallpaper
#in Windows Terminal

#SETUP
#CHANGE PATH VARIABLE
#CHANGE PATHTOIMAGE VARIABLE
#CHANGE WindowsTerminalID VARIABLE


#!IMPORTANT!
# In Line 47: Change Microsoft Package Identification 
# E.g: Microsoft.WindowsTerminal_7Hj8dn290kd
# This ID can be found here: C:/Users/<USERNAME>/AppData/Local/Packages/Microsoft.WindowsTerminal_<ID>
# Set WindowsTerminalID = <ID>

import os
import sys
import time
import signal

#PATH TO YOUR PICTURE LIBLARY 
# E.g: path = "/mnt/c/Users/<USERNAME>/Pictures/linux/"
# E.g: pathToImage = "\"backgroundImage\": \"C:\\/Users\\/<USERNAME>\\/Pictures\\/linux\\/"

path = ""
pathToImage = ""
WindowsTerminalID = ""

def NoArgument():
    print("USAGE: cwp <arg> <...>\nHelp: -h")

def showHelp():
    print("HELP:\n")
    print("swap <wallpaper> - Swap current Wallpaper to another")
    print("list - List all current Wallpapers in directory\n")

def listWallpaper():
    
    files = os.listdir(path)

    #lists all files in path. 
    for name in files:
        if name.endswith('.jpg') or name.endswith('.png'):
        #    showWithoutExtension = ('').join(name.split('.')[0])
        #    print(showWithoutExtension)
            print(name)
def swap():
    #change Image Name to current. Where current is the backgoround Image Setting in Windows Terminal
    #.* to change what ever extension it is to jpg. 
    if  os.path.exists("%s%s"%(path,sys.argv[2])):
        pathCompletion = pathToImage+sys.argv[2]+"\""+","
        os.system("sed -i '37s/.*/%s/' /mnt/c/Users/Jakub/AppData/Local/Packages/Microsoft.WindowsTerminal_%s/LocalState/profiles.json"%(pathCompletion,WindowsTerminalID))
    else:
        print("%s do not exists"%sys.argv[2])

def main():
    if len(sys.argv) < 2:
        NoArgument()
    else:
        if sys.argv[1] == "-h":
            showHelp()
        elif sys.argv[1] == "swap":
            try:
                swap()
            except IndexError:
                print("[*] No Image selected")
                exit()
        elif sys.argv[1] == "list":
            listWallpaper()
        else:
            showHelp()

main()

