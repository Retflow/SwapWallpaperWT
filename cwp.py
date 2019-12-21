#!/usr/bin/env python3
#Author: Retflow
#Change Wallpaper(CWP) is a small script to change the wallpaper
#in Windows Terminal

#SETUP
#IN YOUR WINDOWS TERMINAL PROFILES.JSON SET "backgroundImage" to /path/current.jpg
#CHANGE PATH VARIABLE

import os
import sys
import time
import signal

#PATH TO YOUR PICTURE LIBLARY 
#E.g: path = "/mnt/c/Users/*/Pictures/linux/"

path =

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
            showWithoutExtension = ('').join(name.split('.')[0])
            print(showWithoutExtension)

def swap():
    #It change Image Name to current. Where current is the backgoround Image Setting in Windows Terminal
    #.* to change what ever extension it is to jpg. 
    if  os.path.exists("%s%s.jpg"%(path,sys.argv[2])) or os.path.exists("%s%s.png"%(path,sys.argv[2])):
        os.system("cp %s%s.* %scurrent.jpg"%(path,sys.argv[2],path))
        #start new Windows Terminal. Only then it'll change the background
        os.system("cmd.exe /c start wt.exe")
        #killing the proccess of the terminal. Otherwise two terminals would be running
        #It will also kill all your backgorund proccesses. Save all your projects before running this script!
        os.kill(os.getppid(), signal.SIGHUP)
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

