# Swap Wallpaper in Windows Terminal 
Simple Script for swapping wallpapers in Windows Terminal
Working only with WSL

**IMPROVEMENTS IN 2020**  
- case-sensitive comparison
- auto-completion
- config file
  - with path to image directory



**SETUP YOUR WINDOWS TERMINAL PROFILES.JSON CONFIG:**  
change "backgroundImage" to /path/to/your/pictures/current.jpg  
you also might do this:   export PATH=$PATH:/mnt/c/Windows/System32
   
Why current.jpg? It's because this script copy your selected Image to current.jpg  
MyWallpaper.jpg is going to be current.jpg  
You can rename it in whatever you want.
Your .png images will also "converted" to .jpg.   
Everytime you change your wallpaper it also overwrites the current.jpg image.  
As i said, it's an easy script.
Change it, write a whole new script, just do what you want.
I like to share my ideas.  

Have fun with it!

  
**HOW TO USE IT:**  
  sudo chmod +x cwp.py  
  copy cwp.py to /usr/local/bin    
  USAGE:  
  cwp swap <img>  
  &nbsp;&nbsp;will change your wallpaper  
  cwp list  
  &nbsp;&nbsp;will list all your images in your path    
  cwp -h  
  &nbsp;&nbsp;will show the help page  
  
  just write the name without the extension  
  e.g. if you have wallpaper.png  
  write: cwp swap wallpaper

**For those who like to send me feedback**  
I'm active on Reddit(u/Qyez) just write me a message.  
For those who do not like my script. You can also write me a message,  
but stay decent and write me a real critism, not "it's shit". Thanks.

**About me**  
I'm 19 years old  
Still a student  
I write only in C and C++  
Python is new to me  
I love to share all my ideas with the world
  



  ***Thanks to***  
case_O_The_Mondays
