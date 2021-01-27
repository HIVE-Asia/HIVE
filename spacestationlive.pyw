import requests
import os
from PIL import Image
from socket import socket
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from tkinter import *
import datetime
import os
import speech_recognition
import pyttsx3
import sys
import time
import threading
from playsound import playsound
from tkinter import Frame
from tkinter import PhotoImage
import tkinter.messagebox as tmsg

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.runAndWait()


class GUI():
    def __init__(self, parent):
        self.parent = parent
        self.Sat=Label(text="INTERNATIONAL SPACE STATION",bg="black",fg="white")
        self.Sat.config(font=("Arial", 10))
        self.Sat.grid(sticky="N")
        self.parent.title("ISS LIVE")
        self.parent.iconbitmap(os.path.join(sys.path[0], r"\Logo\hive_logo_1_rotation.ico"))

    def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()


    def get_iss_location(self):
        s = requests.get(url='http://api.open-notify.org/iss-now.json')
        isslocation = s.json()
        isslongitude = float(isslocation['iss_position']['longitude'])
        isslatitude = float(isslocation['iss_position']['latitude'])
        
        hemspos = Label(text="HEMISPHERICAL POSITION:")
        hemspos.config(font=("Arial", 10))
        hemspos.grid(row=18)
        hemlt=Label(text='ACCORDING TO LATITUDE:')
        hemlt.grid(row=19)

        if isslatitude>0:
            hemsn=Label(text="Northern Hemisphere")
            hemsn.grid(row=20)
        elif isslatitude==0:
            hemsn=Label(text="On The Equator")
            hemsn.grid(row=20)
        else:
            hemsn=Label(text="Southern Hemisphere")
            hemsn.grid(row=20)

        hemlo=Label(text='ACCORDING TO LONGITUDE:')
        hemlo.grid(row=21)

        if isslongitude>0:
            hemse=Label(text="Eastern Hemisphere")
            hemse.grid(row=22)
        elif isslongitude==0:
            hemse=Label(text="On The Prime Meridian")
            hemse.grid(row=22)
        else:
            hemse=Label(text="Western Hemisphere")
            hemse.grid(row=22)
        diffline3 = Label(text="___________________________________")
        diffline3.grid(row=23)
        
        timezone = Label(text="Indian Standard Time (IST):")
        timezone.config(font=("Arial", 10))
        timezone.grid(row=24)
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        timelab = Label(text=strTime,bg="black",fg="white")
        timelab.grid(row=25)

        


        lat=Label(text='Latitude:')
        lat.config(font=("Arial", 10))
        lat.grid(row=11,column=0)
        lati=Label(text=isslatitude,bg="black",fg="white")
        lati.grid(row=12)
        lon=Label(text='Longitude:')
        lon.config(font=("Arial", 10))
        lon.grid(row=13,column=0)
        longi=Label(text=isslongitude,bg="black",fg="white")
        longi.grid(row=14)
        diffline2 = Label(text="___________________________________")
        diffline2.grid(row=15)
        
        #ispeed=Label(text="Current Speed:")
        #ispeed.grid(row=16)
        #issspeed = Label(text='~7.66 km/s')
        #issspeed.grid(row=17)
                

        


    def get_iss_data(self):
        r = requests.get(url='http://api.open-notify.org/astros.json')
        fulljson = r.json()
        #print(fulljson)
        print()
        message_json = fulljson['message']
        print("ISS RESPONSE:",message_json)
        number_json = fulljson['number']
        print("HUMANS CURRENTLY ON THE ISS:",number_json)
        people_json = fulljson['people']
       
        print()
        print("NAMES OF PEOPLE CURRENTLY ON THE INTERNATIONAL SPACE STATION:")
        
        sheading = Label(text="LIVES ON BOARD:")
        sheading.config(font=("Arial", 10))
        sheading.grid()
        
        i=0
        while i<len(people_json):
            name_json = fulljson['people'][i]['name']
            print(name_json)
            sname=Label(text=name_json)
            sname.grid()
            i=i+1
        diffline0 = Label(text="___________________________________")
        diffline0.grid()

        sattrack = Label(text="ISS LIVE COORDINATES:")
        sattrack.grid()
        sattrack.config(font=("Arial", 10,))
        while 1==1:
            self.get_iss_location()
        

root = Tk()
app = GUI(root)
root.geometry("212x750")
root.minsize(212,750)
root.maxsize(212,750)
thread = threading.Thread(target=app.get_iss_data)
#make test_loop terminate when the user exits the window
thread.daemon = True 
thread.start()
root.mainloop()
