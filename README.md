# Swap Wallpaper in Windows Terminal 
Simple Script for swapping wallpapers in Windows Terminal
Working only with WSL

**NO FURTHER IMPROVEMENTS**  
I do not plan to improve this script in the future. 



  
**Dependencies**  
export PATH=$PATH:/mnt/c/Windows/System32
   
Have fun with it!


  
**HOW TO USE IT:**  
  4 Variables have to be set.  
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
  backgoundImage variable set.  
  
  

**For those who like to send me feedback**  
I'm active on Reddit(u/Qyez) just write me a message.  
For those who do not like my script. You can also write me a message,  
but stay decent and write me a real critism, not "it's shit". Thanks.


  ***Thanks to***  
case_O_The_Mondays
