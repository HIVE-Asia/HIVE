from tkinter import *
import tkinter
import datetime
import os
import speech_recognition
import pyttsx3
import HIVE_GUI
import pyglet
import winsound
import sys
import time
import threading
from playsound import playsound
from tkinter import Frame
from tkinter import PhotoImage
import tkinter.messagebox as tmsg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageSequence
from colorama import Fore, Back, Style
import cpuinfo
import requests
import psutil
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.runAndWait()


class GUI():
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=1400, height=780)
        self.canvas.grid(row=0,column=0)
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'\Logo\hive_advanced_v3.gif'))]
        self.image = self.canvas.create_image(700,390, image=self.sequence[0])
        self.animate(1)
        self.parent.title("HIVE ADVANCED")
        self.parent.iconbitmap(os.path.join(sys.path[0], r"\Logo\hive_logo_1_rotation.ico"))
        self.parent.mymenu = Menu(self.parent)
        self.parent.mymenu.add_command(label="Help",command=self.helpmen)
        self.parent.mymenu.add_command(label="Quit",command=quit)
        self.parent.config(menu=self.parent.mymenu)
        
        #self.window = self.canvas.create_window(200, 200, window=self.hiveai, anchor="w")
        #self.code = StringVar()
        #self.text1 = Label(text='CODE:',fg="blue",bg="black")
        #self.text1.pack(side=TOP)
        #self.parent.codeent = Entry(root, textvariable = self.code, width=4, show='*')
        #self.parent.codeent.pack(side=TOP)
        #b1 = Button(root, bg="black", fg="white", text="START")
        #b1.pack()
    
    def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

    def cpuuser(self):
        self.cpuinfo=cpuinfo.get_cpu_info()['brand_raw']
        #self.strTime = datetime.datetime.now().strftime("%H:%M")
        self.labeltext= Label(text=self.cpuinfo,bg="black",fg="blue",font="courier 14")
        self.labeltext.grid(row=0,column=0, padx=(50, 900),pady=(140, 0))

    def batterystatus(self):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        plugged = "Plugged In" if plugged else "Not Plugged In"
        self.labelbatteryperc= Label(text=percent,bg="black",fg="blue",font="courier 40")
        self.labelbatteryperc.grid(row=0,column=0, padx=(550, 0),pady=(0, 0))
        self.batterypercsym= Label(text="%",bg="black",fg="blue",font="courier 40")
        self.batterypercsym.grid(row=0,column=0, padx=(650, 0),pady=(0, 0))
        self.plugged= Label(text=plugged,bg="black",fg="blue",font="courier 15")
        self.plugged.grid(row=0,column=0, padx=(590, 0),pady=(100, 0))


    def curday(self):
        self.dtrdate=datetime.datetime.now().strftime("%d")
        print(self.dtrdate)
        self.dtrmon=datetime.datetime.now().strftime("%m")
        if self.dtrmon=='1':
            self.dtrmon='January'
        elif self.dtrmon=='2':
            self.dtrmon='February'
        elif self.dtrmon=='3':
            self.dtrmon='March'
        elif self.dtrmon=='4':
            self.dtrmon='April'
        elif self.dtrmon=='5':
            self.dtrmon='May'
        elif self.dtrmon=='6':
            self.dtrmon='June'
        elif self.dtrmon=='7':
            self.dtrmon='July'
        elif self.dtrmon=='8':
            self.dtrmon='August'
        elif self.dtrmon=='9':
            self.dtrmon='September'
        elif self.dtrmon=='10':
            self.dtrmon='October'
        elif self.dtrmon=='11':
            self.dtrmon='November'
        elif self.dtrmon=='12':
            self.dtrmon='December'
        print(self.dtrmon)
        self.dtrday=datetime.datetime.now().strftime("%a")
        print(self.dtrday)
        self.dtryear=datetime.datetime.now().strftime("%y")
        if self.dtryear=='20':
            self.dtryear=2020
        print(self.dtryear)
        self.labeldate= Label(text=self.dtrdate,bg="black",fg="blue",font="courier 40")
        self.labeldate.grid(row=0,column=0, padx=(0, 1225),pady=(0, 224))
        self.labelmon= Label(text=self.dtrmon,bg="black",fg="blue",font="courier 15")
        self.labelmon.grid(row=0,column=0, padx=(0, 1050),pady=(0, 250))
        self.labelyear= Label(text=self.dtryear,bg="black",fg="blue",font="courier 15")
        self.labelyear.grid(row=0,column=0, padx=(0, 1100),pady=(0, 210))
        self.labelday= Label(text=self.dtrday,bg="black",fg="blue",font="courier 15")
        self.labelday.grid(row=0,column=0, padx=(0, 1225),pady=(0, 160))


    def weatherrn(self):
        r = requests.get(url='http://api.openweathermap.org/data/2.5/weather?q=#LOCATION#&appid=api key')
        fulljson = r.json()
        weather_json = fulljson['weather']
        self.condition=weather_json[0]['main']
        self.labelconditionw= Label(text="Weather:",bg="black",fg="blue",font="courier 15")
        self.labelconditionw.grid(row=0,column=0, padx=(0, 698),pady=(300, 0))
        self.labelcondition= Label(text=self.condition,bg="black",fg="blue",font="courier 15")
        self.labelcondition.grid(row=0,column=0, padx=(0, 530),pady=(300, 0))
        temp_json = fulljson['main']
        maintemp = temp_json['temp']
        finalmtemp=int((maintemp-273.5)+1)
        self.labeltempw= Label(text="Temperature:",bg="black",fg="blue",font="courier 15")
        self.labeltempw.grid(row=0,column=0, padx=(0, 651),pady=(350, 0))
        self.labeltemp= Label(text=finalmtemp,bg="black",fg="blue",font="courier 15")
        self.labeltemp.grid(row=0,column=0, padx=(0, 481),pady=(350, 0))
        self.labelcelc= Label(text="°C",bg="black",fg="blue",font="courier 15")
        self.labelcelc.grid(row=0,column=0, padx=(0, 426),pady=(350, 0))
            
        feelstemp = temp_json['feels_like']
        finalfeelstemp=int((maintemp-273.5)+1)
        self.labelfeelsw= Label(text="Feels Like:",bg="black",fg="blue",font="courier 15")
        self.labelfeelsw.grid(row=0,column=0, padx=(0, 663),pady=(400, 0))
        self.labelfeels= Label(text=finalfeelstemp,bg="black",fg="blue",font="courier 15")
        self.labelfeels.grid(row=0,column=0, padx=(0, 493),pady=(400, 0))
        self.labelcelc= Label(text="°C",bg="black",fg="blue",font="courier 15")
        self.labelcelc.grid(row=0,column=0, padx=(0, 439),pady=(400, 0))

        maxtemp = temp_json['temp_max']
        finalmaxtemp=int((maintemp-273.5)+2)
        self.labelmaxw= Label(text="Maximum:",bg="black",fg="blue",font="courier 15")
        self.labelmaxw.grid(row=0,column=0, padx=(0, 698),pady=(450, 0))
        self.labelmax= Label(text=finalmaxtemp,bg="black",fg="blue",font="courier 15")
        self.labelmax.grid(row=0,column=0, padx=(0, 563),pady=(450, 0))
        self.labelcelc= Label(text="°C",bg="black",fg="blue",font="courier 15")
        self.labelcelc.grid(row=0,column=0, padx=(0, 509),pady=(450, 0))


        mintemp = temp_json['temp_min']
        finalmintemp=int((maintemp-273.5))
        self.labelminw= Label(text="Minimum:",bg="black",fg="blue",font="courier 15")
        self.labelminw.grid(row=0,column=0, padx=(0, 698),pady=(500, 0))
        self.labelmin= Label(text=finalmintemp,bg="black",fg="blue",font="courier 15")
        self.labelmin.grid(row=0,column=0, padx=(0, 563),pady=(500, 0))
        self.labelcelc= Label(text="°C",bg="black",fg="blue",font="courier 15")
        self.labelcelc.grid(row=0,column=0, padx=(0, 509),pady=(500, 0))


        humidityrn = temp_json['humidity']
        self.labelhumidityw= Label(text="Humidity:",bg="black",fg="blue",font="courier 15")
        self.labelhumidityw.grid(row=0,column=0, padx=(0, 687),pady=(550, 0))
        self.labelhumidity= Label(text=humidityrn,bg="black",fg="blue",font="courier 15")
        self.labelhumidity.grid(row=0,column=0, padx=(0, 548),pady=(550, 0))
        self.labelper= Label(text="%",bg="black",fg="blue",font="courier 15")
        self.labelper.grid(row=0,column=0, padx=(0, 499),pady=(550, 0))


        atmosph = temp_json['pressure']
        self.labelatmw= Label(text="Pressure:",bg="black",fg="blue",font="courier 15")
        self.labelatmw.grid(row=0,column=0, padx=(0, 690),pady=(600, 0))
        self.labelatm= Label(text=atmosph,bg="black",fg="blue",font="courier 15")
        self.labelatm.grid(row=0,column=0, padx=(0, 528),pady=(600, 0))
        self.labelmbar= Label(text="mbar",bg="black",fg="blue",font="courier 15")
        self.labelmbar.grid(row=0,column=0, padx=(0, 409),pady=(600, 0))

    def alarmopener(self):
        codePath = r'\Alarm_GUI_Trial2.pyw'
        os.startfile(codePath)

    def issopener(self):
        codePath = r'\ISS_LIVE.pyw'
        os.startfile(codePath)

    def newsopener(self):
        codePath = r'\newsheadlines.pyw'
        os.startfile(codePath)
    
    def nasadataopener(self):
        codePath = r'\nasadatasbdb.pyw'
        os.startfile(codePath)

    def emailopener(self):
        codePath = r'\emailwrite.pyw'
        os.startfile(codePath)

    def googlesearcheng(self):
        querytosearch=self.searchongoogle.get()
        webbrowser.open('https://google.com/?#q=' + querytosearch)
        qtsearch = "Searching for {}".format(querytosearch)
        self.speak(qtsearch)
    
    def musicplayeropener(self):
        codePath = r'\hivemusicplayer.pyw'
        os.startfile(codePath)

    def buttonsonside(self):
        self.alarm_btn1 = PhotoImage(file=r'\Graphics\alarm_button.png')
    
        alarmbutt = Button(image=self.alarm_btn1, bg="black", fg="blue", borderwidth=0, activebackground="black", command=self.alarmopener)
        alarmbutt.grid(row=0,column=0, padx=(450, 0),pady=(0, 200))

        self.iss_btn2 = PhotoImage(file=r'\Graphics\iss_button.png')
    
        issbutt = Button(image=self.iss_btn2, bg="black", fg="blue", borderwidth=0, activebackground="black", command=self.issopener)
        issbutt.grid(row=0,column=0, padx=(450, 0),pady=(0, 0))

        self.news_btn3 = PhotoImage(file=r'\Graphics\news_button.png')
    
        newsbutt = Button(image=self.news_btn3, bg="black", fg="blue", borderwidth=0, activebackground="black", command=self.newsopener)
        newsbutt.grid(row=0,column=0, padx=(450, 0),pady=(200, 0))

        self.nasa_btn4 = PhotoImage(file=r'\Graphics\nasa_button.png')
    
        nasabutt = Button(image=self.nasa_btn4, bg="black", fg="blue", borderwidth=0, activebackground="black", command=self.nasadataopener)
        nasabutt.grid(row=0,column=0, padx=(600, 0),pady=(200, 0))

        self.email_btn5 = PhotoImage(file=r'\Graphics\email_button.png')
    
        emailbutt = Button(image=self.email_btn5, bg="black", fg="blue", borderwidth=0, activebackground="black", command=self.emailopener)
        emailbutt.grid(row=0,column=0, padx=(600, 0),pady=(0, 0))

        self.searchongoogle = StringVar()
        searchgoogle_inp = Entry(root,bg="black",fg="white",width=25, textvariable=self.searchongoogle)
        searchgoogle_inp.grid(row=0,column=0, padx=(1050, 0),pady=(650, 0))
        searchgooglebutt_inp = Button(root,bg="black",fg="white",text="Search",activebackground="black",font="courier 7", command=self.googlesearcheng)
        searchgooglebutt_inp.grid(row=0,column=0, padx=(1250, 0),pady=(650, 0))

        self.musicplayer_btn6 = PhotoImage(file=r'\Graphics\musicplayer_button.png')
        musicplayerbutt = Button(image=self.musicplayer_btn6, bg="black", fg="blue", borderwidth=0, activebackground="black", command=self.musicplayeropener)
        musicplayerbutt.grid(row=0,column=0, padx=(600, 0),pady=(0, 200))

    def hiveai(self):
        os. system('cls')
        self.curday()
        self.cpuuser()
        self.weatherrn()
        self.buttonsonside()
        #self.batterystatus()
        playsound('\\audio\\Help.mp3')
        exefile = HIVE_GUI.hivefinal()
        execfile('execfile')
        
        
        
    
    def helpmen(self):
        a = tmsg.showinfo("Help","Please contact HIVE team at: \n #EMAIL ADDRESS#")
    

root = Tk()
app = GUI(root)
root.geometry("1400x780+50+0")
root.minsize(1400,780)
root.maxsize(1400,780)
#Process = threading.Thread(target=app.batterystatus).start()
thread = threading.Thread(target=app.hiveai)
thread.daemon = True 
thread.start()

root.mainloop()

    
    
    
