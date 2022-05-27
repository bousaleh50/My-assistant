import pyttsx3
import speech_recognition as sr
import datetime
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

engine=pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",150)

class Jarvis:
    def __init__(self,name="jarvis",master="sir"):
        self.__name=name
        self.__master=master

    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,name:str):
        self.__name=name

    @property
    def Master(self):
        return self.__master
    @Master.setter
    def Master(self,master:str):
        return self.__master

    def speak(self,text):
        engine.say(text)
        engine.runAndWait()


#greating function
    def Grating(self):
        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour < 12:
            Jarvis.speak(self,"good Morning sir")
        elif hour >= 12 and hour < 18:
            Jarvis.speak(self,"good Afternoon sir")
        else:
            Jarvis.speak(self,"good Evening sir")


    #Takes order from micro
    def orders(self):
        r=sr.Recognizer()

        with sr.Microphone() as source:
            #wait for a second to let the recognizer adjust the
            #energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source)
            print ("listining...")
            #listens for the user's input
            audio = r.listen(source)

        try:
            order = r.recognize_google(audio,language="en-US")
            print( "you said: " + order)

        except Exception as e:
            print(e)
            order=""

        return order

    def ControleSoundVolume(self,level:str):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
         # Get current volume
        currentVolumeDb = volume.GetMasterVolumeLevel()

        if(level == "down"):
                volume.SetMasterVolumeLevel(currentVolumeDb - 6.0, None)
        else:
            volume.SetMasterVolumeLevel(currentVolumeDb+6.0,None)





