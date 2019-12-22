# Swap Wallpaper in Windows Terminal 
Simple Script for swapping wallpapers in Windows Terminal
Working only with WSL

**IMPROVEMENTS IN 2020**  
- case-sensitive comparison
- auto-completion
- easy path setup
- config file
  - with path to image directory
  
**Dependencies**  
export PATH=$PATH:/mnt/c/Windows/System32
   
Have fun with it!


  
**HOW TO USE IT:**  
  3 Variables have to be set.  
  Do not worry, I explained those in the Source code.  
  sudo chmod +x cwp.py  
  copy cwp.py to /usr/local/bin    
  USAGE:  
  cwp swap <img>  
  &nbsp;&nbsp;will change your wallpaper  
  cwp list  
  &nbsp;&nbsp;will list all your images in your path    
  cwp -h  
  &nbsp;&nbsp;will show the help page  
  Example:  
  cwp swap wallpaper.jpg  
  **Important**  
  This script search for backgoroundImage string 
  in your profiles.json and overwrites it with  
  the new wallpaper. Do not have more than one  
  backgoundImage setting.  
  
  

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
