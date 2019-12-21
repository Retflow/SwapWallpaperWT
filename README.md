# Swap Wallpaper in Windows Terminal 
Simple Script for swapping wallpapers in Windows Terminal
Working only with WSL

**SETUP YOUR WINDOWS TERMINAL PROFILES.JSON CONFIG:**  
change "backgroundImage" to /path/to/your/pictures/1.jpg  
you also might to do this:   export PATH=$PATH:/mnt/c/Windows/System32
   
Why 1.jpg? It's because this script copy your Image to 1.jpg
Even if your file is a .png.   
Everytime you change your wallpaper it also overwrites 1.jpg.
As i said, it's an easy script and also a bad one.
Change it, write a whole new idea, just do what you want.
I just want to share my idea with you. 

Have fun with it!
  
**HOW TO USE IT:**  
  copy cwp.py to /usr/local/bin  
  USAGE:  
  cwp swap <img> will change your wallpaper
  cwp list will list all your images in your path
  cwp -h will show the help page
  
