from jarvis import Jarvis
import wikipedia
import webbrowser
import os
from random import  randrange
import smtplib
import tkinter
import math


print(f"initializing jarvis....")

jarvis=Jarvis(master="ahmed")




if __name__=="__main__":
   root=tkinter.Tk()
   jarvis.speak(f"initalizing {jarvis.Name}")
   jarvis.Grating()
   jarvis.speak("how can i help you....")
   while True:
       order = jarvis.orders().lower()

       if order != None:
           if "wikipedia" in order:
                jarvis.speak("searching wikipedia...")
                order=order.replace("wikipedia","")
                results=wikipedia.summary(order,sentences=2)
                print(results)
                jarvis.speak(results)
           elif "open youtube" in order:
               webbrowser.open("youtube.com")
           elif "open whatsapp" in order:
               webbrowser.open("https://web.whatsapp.com")

           elif "music" in order:
               media="C:/Users/21263/Downloads/Video"
               songs=os.listdir(media)
               print(media)
               os.startfile(os.path.join(media,songs[randrange(0,len(songs))]))
           elif "volume down" in order:
               jarvis.ControleSoundVolume("down")
           elif "volume up" in order:
               jarvis.ControleSoundVolume("up")


       else:
           print("Errore we can not dedect your voisce ")
           jarvis.speak("Errore we can not detect your voice ")

   root.mainloop()
