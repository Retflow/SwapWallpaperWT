#!/usr/bin/env python3
#Change Wallpaper(CWP) is a small script to change the wallpaper
#for Windows Terminal

#License Stuff
#
#Copyright (C) 2017 by Gynvael Coldwind
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

#SETUP
#CHANGE PATH VARIABLE
#CHANGE PATHTOIMAGE VARIABLE
#CHANGE WindowsTerminalID VARIABLE
#CHANGE user VARIABLE


#!IMPORTANT!
# Windows Terminal ID are unique. 
# E.g: Microsoft.WindowsTerminal_7Hj8dn290kd
# This ID can be found here: C:/Users/<USERNAME>/AppData/Local/Packages/Microsoft.WindowsTerminal_<ID>
# Set WindowsTerminalID = <ID>

import os
import sys
import time
import signal
import subprocess


#PATH TO YOUR PICTURE LIBLARY 
# E.g: path = "/mnt/c/Users/<USERNAME>/Pictures/linux/"
# E.g: pathToImage = "\"backgroundImage\": \"C:\\/Users\\/<USERNAME>\\/Pictures\\/linux\\/"
# In the future I'm going to create an easy setup for paths. But for now use this. 
# I think you're familiar with Linux, so this should't be hard.

#set user variable to your windows user name. C:\Users\<user>

path = ""
pathToImage = ""
WindowsTerminalID = ""
user = ""

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
        if name.endswith('.jpg') or name.endswith('.png') or name.endswith('.gif'):
        #    showWithoutExtension = ('').join(name.split('.')[0])
        #    print(showWithoutExtension)
            print(name)
def swap():
    #change Image Name to current. Where current is the backgoround Image Setting in Windows Terminal
    #.* to change what ever extension it is to jpg. 
    if  os.path.exists("%s%s"%(path,sys.argv[2])):
        pathCompletion = pathToImage+sys.argv[2]+"\""+","
        #Looks for backgroundImage string in config, and then save the numberline
        #This way, it isn't neccessary to open the profiles.json
        #Warning! Only one can exist. It searches for one numberline, 
        #if you have to backgroundImage variables set, the closer
        #will only be overwritten. 
        backgroundLine = os.popen("cat /mnt/c/Users/%s/AppData/Local/Packages/Microsoft.WindowsTerminal_%s/LocalState/profiles.json | grep -n -m 1 backgroundImage | cut -f1 -d:"%(user,WindowsTerminalID)).read().split('\n')
        os.system("sed -i '%ds/.*/%s/' /mnt/c/Users/%s/AppData/Local/Packages/Microsoft.WindowsTerminal_%s/LocalState/profiles.json"%(int(backgroundLine[0]),pathCompletion,user,WindowsTerminalID))
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
