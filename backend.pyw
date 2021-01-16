import pyttsx3
import datetime
import speech_recognition
import wikipedia
import webbrowser
import os
import smtplib
import socket
import random
import requests
import pyowm
import playsound
import re
import time
from playsound import playsound
import wolframalpha 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.runAndWait()
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)   



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email address', 'email password')
    server.sendmail('email address', to, content)
    server.close()

def NewsFromBBC(): 
      
    # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="
  
    open_bbc_page = requests.get(main_url).json() 
  
    article = open_bbc_page["articles"] 
  
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
        print(i + 1, results[i]) 
  
    codePath = "\\newsheadlines.pyw"
    os.startfile(codePath)
    speak(results) 


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    
    else:
        speak("Good Evening Sir")

    speak("I am Hive, how may I help you?")


r = speech_recognition.Recognizer()
def takeCommand():


    with speech_recognition.Microphone() as source:
            playsound('\\audio\\Listening.mp3')
            print("Listening.....")
            audio = r.listen(source, phrase_time_limit=7)

    try:
        playsound('\\audio\\Recognizing.mp3')
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(query)
        #speak("Input recognized as")
        #speak(query)

    except Exception as e:
        print(e)
        #speak("I could not get that. Could you please repeat sir?")
        return "None"
    
    return query

def weathr():
    owm = pyowm.OWM('api key')
    mgr = owm.weather_manager()
    obs = mgr.weather_at_place('location')
    weather = obs.weather
    status = weather.status
    print("Weather:" + status)
    if status == 'Haze':
        f="Hazy"
        speak("The weather in #LOCATION# is currently " + f)
    elif status == 'haze':
        f="Hazy"
        speak("The weather in #LOCATION# is currently " + f)
    elif status == 'Smoke':
        f="Smokey"
        speak("The weather in #LOCATION# is currently " + f)
    elif status == 'smoke':
        f="Smokey"
        speak("The weather in #LOCATION# is currently " + f)
    else:
        speak("The weather in #LOCATION# is currently " + status)
    
    temp = weather.temperature('celsius')
    for key, value in temp.items():
        print(key, value)
    speak("The temperatures are as displayed")

jokes = [
        "What did the dog say when it sat on some sharp stones? Rough",
        "Never lie to an x-ray technician, they can see right through you",
        "Why did the robot go to the doctor? Its because he caught the virus",
        "What do you call a fight between celebrities? Star wars!",
        "What is the best thing about Switzerland? I don't know, but the flag is a big plus",
        "I was reading a great book about an immortal dog the other day. It was impossible to put down",
        "I have a joke about trickle down economics. But 99 per cent of people will never get it.",
        "Why don't scientists trust atoms? Because they make up everything",
        "How do you drown a hipster? Throw him in the mainstream",
        "What has four wheels and flies? A garbage truck",
        "Why couldn't the pony sing? Because it was a little hoarse.",
        "Why did Adele cross the road? To say hello from the other side.",
        "A neutron enters a bar and orders a drink. The Bartender hands over the drink and says for you, no charge.",
]

facts = [
        "North Korea and Cuba are the only places in the world where you can't buy Coca-Cola.",
        "The entire world's population could fit inside Los Angeles.",
        "The hottest chili pepper in the world is so hot it could kill you.",
        "More people visit France than any other country.",
        "The world's quietest room is located at Microsoft's headquarters in Washington state.",
        "There are only three countries in the world that don't use the metric system.",
        "People who are currently alive represent about 7 percent of the total number of people who have ever lived.",
        "Muhammad is thought to be the most popular name in the world.",
        "Africa and Asia are home to nearly 90 percent of the world's rural population.",
        "More than 52 percent of the world's population is under 30 years old.",
        "Nearly half of the world's population watched both the 2010 and 2014 FIFA World Cup games.",
        "There are 43 countries that still have a royal family.",
        "All giant pandas in zoos around the world are on loan from China.",
        "Around one in every 200 men are direct descendants of Genghis Khan.",
        "All the ants on Earth weigh about as much as all the humans.",
        "The oceans contain almost 200,000 different kinds of viruses."

]

quotes = [
        "William Faulkner once said; Get it down. Take chances. It may be bad, but it's the only way you can do anything really good.",
        "Jodi Picoult once said; You can always edit a bad page. You can’t edit a blank page",
        "Nelson Mandela once said; The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "Oprah Winfrey once said; If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
        "Eleanor Roosevelt once said; The future belongs to those who believe in the beauty of their dreams.",
        "Aristotle once said; It is during our darkest moments that we must focus to see the light.",
        "Franklin D. Roosevelt once said; When you reach the end of your rope, tie a knot in it and hang on.",
        "Maya Angelou once said; You will face many defeats in life, but never let yourself be defeated.",
        "Babe Ruth once said; Never let the fear of striking out keep you from playing the game.",
        "Thomas Edison once said; Many of life's failures are people who did not realize how close they were to success when they gave up.",
        "Tony Robbins once said; The only impossible journey is the one you never begin.",
        "Steve Jobs once said; If you really look closely, most overnight successes took a long time.",
        "Barack Obama once said; The real test is not whether you avoid this failure, because you won't. It's whether you let it harden or shame you into inaction, or whether you learn from it; whether you choose to persevere.",
        "Winston Churchill once said; Success is not final; failure is not fatal: It is the courage to continue that counts.",
        "Conrad Hilton once said; Success seems to be connected with action. Successful people keep moving. They make mistakes but they don't quit.",
        "Jim Rohn once said; Successful people do what unsuccessful people are not willing to do. Don't wish it were easier; wish you were better.",
        "James Cameron once said; If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
        "David Brinkley once said; A successful man is one who can lay a firm foundation with the bricks others have thrown at him.",
        "Abraham Lincoln once said; Always bear in mind that your own resolution to success is more important than any other one thing.",
        "Oprah Winfrey once said; You know you are on the road to success if you would do your job and not be paid for it.",
        "Tony Robbins once said; People who succeed have momentum. The more they succeed, the more they want to succeed and the more they find a way to succeed. Similarly, when someone is failing, the tendency is to get on a downward spiral that can even become a self-fulfilling prophecy.",
]


greet_hi = [ "Hello!", "Hi!", "Hey there!", "How's it going?", "What's up?", "Hey! How're you doing?", "Hello! What are you doing?", 
             "Heya!", "Heya! Whatchu up to?", "Hey! Whatchu up to?", "Hello, whatchu up to?", 
             "Heya! Whatchu doing?", "Hey! Whatchu up to?", "Hello, Whatchu up to?"
]

def hivefinal():
    mcounter = 0   
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            speak("According to my search on Wikipedia ")
            print(results)
            speak(results)
        elif 'weather' in query:
            weathr()

        elif 'news headlines' in query:
            NewsFromBBC()        
        elif 'headlines' in query:
            NewsFromBBC()  
        elif 'headline' in query:
            NewsFromBBC()  

        elif 'how old are you' in query:
            year = datetime.date.today().year
            month = datetime.date.today().month
            day = datetime.date.today().day
            ageyer = year - 2020
            if month>11:
                agemot = month - 11
            else:
                agemont = 11 - month
            if day>18:
                ageday = day - 11
            else:
                ageday = 11 - day
            print("I was made on 18 November 2020")
            speak("I was made on Eighteenth November 2020; and I am")
            speak(ageyer)
            speak("years old")
        elif 'what is your age' in query:
            year = datetime.date.today().year
            month = datetime.date.today().month
            day = datetime.date.today().day
            ageyer = year - 2020
            if month>11:
                agemot = month - 11
            else:
                agemont = 11 - month
            if day>18:
                ageday = day - 11
            else:
                ageday = 11 - day
            print("I was made on 18 November 2020")
            speak("I was made on Eighteenth November 2020; and I am")
            speak(ageyer)
            speak("years old")
        elif 'your age' in query:
            year = datetime.date.today().year
            month = datetime.date.today().month
            day = datetime.date.today().day
            ageyer = year - 2020
            if month>11:
                agemot = month - 11
            else:
                agemont = 11 - month
            if day>18:
                ageday = day - 11
            else:
                ageday = 11 - day
            print("I was made on 18 November 2020")
            speak("I was made on Eighteenth November 2020; and I am")
            speak(ageyer)
            speak("years old")

        elif 'alarm' in query:
            codePath = "\\Alarm_GUI_Trial2.pyw"
            os.startfile(codePath)
            time.sleep(15)
        elif 'reminder' in query:
            codePath = "\\Alarm_GUI_Trial2.pyw"
            os.startfile(codePath)
            time.sleep(15)

        elif 'what is' in query:
                if 'what is the headlines' in query:
                    pass
                elif 'what is today\'s headlines' in query:
                    pass
                elif 'what is the headline' in query:
                    pass
                elif 'what is today\'s headline' in query:
                    pass
                elif 'what is today\'s weather' in query:
                    pass
                elif 'what is the weather today' in query:
                    pass
                else:
                    query1 = query.replace("what is","")
                    webbrowser.open('https://google.com/?#q=' + query1)
        elif 'what are' in query:
                if 'what are the headlines' in query:
                    pass
                elif 'what are today\'s headlines' in query:
                    pass
                else:
                    query1 = query.replace("what are","")
                    webbrowser.open('https://google.com/?#q=' + query1)
        elif 'search' in query:
                query1 = query.replace("search","")
                webbrowser.open('https://google.com/?#q=' + query1)
        elif 'define' in query:
                query1 = query.replace("define","")
                webbrowser.open('https://google.com/?#q=' + query1)
        elif 'definition' in query:
                query1 = query.replace("definition","")
                webbrowser.open('https://google.com/?#q=' + query1)
        
        
        
        elif 'live news' in query:
            codePath = "\\news_select.pyw"
            os.startfile(codePath)
            speak("Sir, please select a channel. We have, Sky news, NBC News, India TV, India Today and ABC News")
            print("1.Sky News")
            print("2.NBC News") 
            print("3.India TV") 
            print("4.India Today") 
            print("5.ABC News")     
        elif 'news channel' in query:
            codePath = "\\news_select.pyw"
            os.startfile(codePath)
            speak("Sir, please select a channel. We have, Sky news, NBC News, India TV, India Today and ABC News")
            print("1.Sky News")
            print("2.NBC News") 
            print("3.India TV") 
            print("4.India Today") 
            print("5.ABC News")     


        elif 'sky news' in query:
            webbrowser.open('https://www.youtube.com/watch?v=9Auq9mYxFEE&ab_channel=SkyNews')
        elif 'nbc' in query:
            webbrowser.open('https://www.youtube.com/watch?v=6F8p0YA5yWY&ab_channel=NBCNews')
        elif 'india tv' in query:
            webbrowser.open('https://www.youtube.com/watch?v=g5nxBHO25YI&ab_channel=IndiaTV')
        elif 'india today' in query:
            webbrowser.open('https://www.youtube.com/watch?v=mBN_U_qo780&ab_channel=IndiaToday')
        elif 'abc' in query:
            webbrowser.open('https://www.youtube.com/watch?v=w_Ma8oQLmSM&ab_channel=ABCNews')    
        
        elif 'my ip address' in query:
            hostname = socket.gethostname()    
            IPAddr = socket.gethostbyname(hostname)
            print("Your Device's Name is:" + hostname)    
            speak("Your Device's Name is:" + hostname) 
            print("Your Device's IP Address is:" + IPAddr)    
            speak("Your Device's IP Address is:" + IPAddr)
        elif 'my IP address' in query:
            hostname = socket.gethostname()    
            IPAddr = socket.gethostbyname(hostname)
            print("Your Device's Name is:" + hostname)    
            speak("Your Device's Name is:" + hostname) 
            print("Your Device's IP Address is:" + IPAddr)    
            speak("Your Device's IP Address is:" + IPAddr)
        elif 'IP address' in query:
            hostname = socket.gethostname()    
            IPAddr = socket.gethostbyname(hostname)
            print("Your Device's Name is:" + hostname)    
            speak("Your Device's Name is:" + hostname) 
            print("Your Device's IP Address is:" + IPAddr)    
            speak("Your Device's IP Address is:" + IPAddr)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open my mail' in query:
            webbrowser.open("mail.google.com")
        elif 'open my meet' in query:
            webbrowser.open("meet.google.com")
        elif 'open my classroom' in query:
            webbrowser.open("classroom.google.com")
        elif 'open get into pc' in query:
            webbrowser.open("getintopc.com")
        elif 'new free softwares' in query:
            print("Get into PC seems to be a very popular website for free softwares, we can try that out")
            webbrowser.open("getintopc.com")
        elif 'new free software' in query:
            speak("Get into PC seems to be a very popular website for free softwares, we can try that out")
            webbrowser.open("getintopc.com")
        elif 'need to do some shopping' in query:
            speak("Amazon seems to be a pretty good place for online shopping, how about we try that out?")
            webbrowser.open("amazon.com")
        elif 'some shopping' in query:
            speak("Amazon seems to be a pretty good place for online shopping, how about we try that out?")
            webbrowser.open("amazon.com")
        elif 'shopping' in query:
            speak("Amazon seems to be a pretty good place for online shopping, how about we try that out?")
            webbrowser.open("amazon.com")
        elif 'need some new clothes' in query:
            speak("You could purchase some online right now, how about we try out amazon?")
            webbrowser.open("amazon.com")
        elif 'need new clothes' in query:
            speak("You could purchase some online right now, how about we try out amazon?")
            webbrowser.open("amazon.com")
        elif 'join my meeting' in query:
            speak("Please enter your meeting code sir")
            mcode = input()
            webbrowser.open("meet.google.com/{mcode}")
        elif 'join meeting' in query:
            speak("Please enter your meeting code sir")
            mcode = input()
            webbrowser.open("meet.google.com/{mcode}")
        
        elif 'play music' in query:
            music_dir = '\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'my music' in query:
            music_dir = '\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play some music' in query:
            music_dir = '\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'find some music' in query:
            music_dir = '\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'lets hear some music' in query:
            music_dir = '\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play some songs' in query:
            music_dir = '\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'some songs' in query:
            music_dir = '\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open media player' in query:
            speak("Opening V L C Media Player")
            codePath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(codePath)
        elif 'open whats app' in query:
            speak("Opening Whats App")
            codePath = "\\Apps\\WhatsApp Desktop.lnk"
            os.startfile(codePath)
        elif 'open whatsapp' in query:
            speak("Opening Whats App")
            codePath = "\\Apps\\WhatsApp Desktop.lnk"
            os.startfile(codePath)
        elif 'open what is app' in query:
            speak("Opening Whats App")
            codePath = "\\Apps\\WhatsApp Desktop.lnk"
            os.startfile(codePath)
        elif 'open what\'s app' in query:
            speak("Opening Whats App")
            codePath = "\\Apps\\WhatsApp Desktop.lnk"
            os.startfile(codePath)
        elif 'open my sketchup files' in query:
            speak("Opening files with all your sketchup documents.")
            codePath = "\\Files\\SketchUp"
            os.startfile(codePath)
        elif 'my sketchup files' in query:
            speak("Opening files with all your sketchup documents.")
            codePath = "\\Files\\SketchUp"
            os.startfile(codePath)
        elif 'open my sketchup designs' in query:
            speak("Opening files with all your sketchup documents.")
            codePath = "\\Files\\SketchUp"
            os.startfile(codePath)
        elif 'my sketchup designs' in query:
            speak("Opening files with all your sketchup documents.")
            codePath = "\\Files\\SketchUp"
            os.startfile(codePath)
        elif 'sketchup files' in query:
            speak("Opening files with all your sketchup documents.")
            codePath = "\\Files\\SketchUp"
            os.startfile(codePath)
        elif 'sketchup designs' in query:
            speak("Opening files with all your sketchup documents.")
            codePath = "\\Files\\SketchUp"
            os.startfile(codePath)
        elif 'open my sketchup work' in query:
            speak("Opening files with all your sketchup documents.")
            codePath = "\\Files\\SketchUp"
            os.startfile(codePath)
        elif 'my sketchup work' in query:
            speak("Opening files with all your sketchup documents.")
            codePath = "\\Files\\SketchUp"
            os.startfile(codePath)
        elif 'new wallpaper' in query:
            speak("I am opening your wallpaper choices, choose and set any you'd like sir.")
            codePath = "\\Pictures\\Wallpaper"
            os.startfile(codePath)
        elif 'change wallpaper' in query:
            speak("I am opening your wallpaper choices, choose and set any you'd like sir.")
            codePath = "\\Pictures\\Wallpaper"
            os.startfile(codePath)
        elif 'wallpaper change' in query:
            speak("I am opening your wallpaper choices, choose and set any you'd like sir.")
            codePath = "\\Pictures\\Wallpaper"
            os.startfile(codePath)
        elif 'open zoom' in query:
            speak("Opening Zoom")
            codePath = "\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)
        elif 'open sketch up' in query:
            speak("Opening Sketch Up")
            codePath = "\\SketchUp\\SketchUp 2017\\SketchUp.exe"
            os.startfile(codePath)
        elif 'open photo shop' in query:
            speak("Opening adobe photo shop, please give me a moment")
            codePath = "\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(codePath)
        elif 'open photoshop' in query:
            speak("Opening adobe photo shop, please give me a moment")
            codePath = "\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(codePath)
        elif 'open Photoshop' in query:
            speak("Opening adobe photo shop, please give me a moment")
            codePath = "\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(codePath)
        elif 'open after effects' in query:
            speak("Opening Adobe After Effects, please give me a moment")
            codePath = "\\Adobe\\Adobe After Effects CC 2019\\Support Files\\AfterFX.exe"
            os.startfile(codePath)
        elif 'open animate' in query:
            speak("Opening Adobe Animate C C, please give me a moment")
            codePath = "\\Adobe\\Adobe Animate 2020\\Animate.exe"
            os.startfile(codePath)
        elif 'open power iso' in query:
            speak("Opening Power I S O")
            codePath = "\\PowerISO\\PowerISO.exe"
            os.startfile(codePath)
        elif 'open power i s o' in query:
            speak("Opening Power I S O")
            codePath = "\\PowerISO\\PowerISO.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            speak("Opening Google Chrome")
            codePath = "\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'open google chrome' in query:
            speak("Opening Google Chrome")
            codePath = "\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'open edge' in query:
            speak("Opening Microsoft Edge")
            codePath = "\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)
        elif 'open microsoft edge' in query:
            speak("Opening Microsoft Edge")
            codePath = "\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)
        elif 'open micro soft edge' in query:
            speak("Opening Microsoft Edge")
            codePath = "\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)
        elif 'open calculator' in query:
            speak("Opening Calculator")
            codePath = "\\System32\\calc.exe"
            os.startfile(codePath)
        elif 'open browsing' in query:
            file_browse_path =  "\\BrowseWindows.pyw"
            os.startfile(file_browse_path)
        elif 'browse' in query:
            file_browse_path =  "\\BrowseWindows.pyw"
            os.startfile(file_browse_path)
        
        elif 'calculate' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'add' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'subtract' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'divide' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'multiply' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'plus' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'minus' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'quotient' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'product' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'sum' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'integrate' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'integration' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'differentiate' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif 'differentiation' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)

        elif 'notepad' in query:
            speak("Opening Note pad")
            codePath = "\\system32\\notepad.exe"
            os.startfile(codePath)
        elif 'note pad' in query:
            speak("Opening Note pad")
            codePath = "\\system32\\notepad.exe"
            os.startfile(codePath)
        elif 'wordpad' in query:
            speak("Opening word pad")
            codePath = "\\Accessories\\wordpad.exe"
            os.startfile(codePath)
        elif 'word pad' in query:
            speak("Opening word pad")
            codePath = "\\Accessories\\wordpad.exe"
            os.startfile(codePath)
            
        elif '+' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif '-' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif '*' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)
        elif '/' in query:
            question = query
            app_id = "api key"
            client = wolframalpha.Client(app_id)  
            res = client.query(question) 
            answer = next(res.results).text  
            print(answer)
            speak(answer)

        elif 'command prompt' in query:
            speak("Opening command promt")
            codePath = "\\System32\\cmd.exe"
            os.startfile(codePath)
        elif 'cmd' in query:
            speak("Opening command promt")
            codePath = "\\System32\\cmd.exe"
            os.startfile(codePath)
        elif 'paint' in query:
            speak("Opening Microsoft Paint")
            codePath = "\\System32\\mspaint.exe"
            os.startfile(codePath)
        elif 'anti virus' in query:
            speak("Opening Mc Afee")
            codePath = "\\McUICnt.exe"
            os.startfile(codePath)
        elif 'antivirus' in query:
            speak("Opening Mc Afee")
            codePath = "\\McUICnt.exe"
            os.startfile(codePath)
        elif 'mcafee' in query:
            speak("Opening Mc Afee")
            codePath = "\\McUICnt.exe"
            os.startfile(codePath)
        elif 'mc afee' in query:
            speak("Opening Mc Afee")
            codePath = "\\McUICnt.exe"
            os.startfile(codePath)
        elif 'mc a fee' in query:
            speak("Opening Mc Afee")
            codePath = "\\McUICnt.exe"
            os.startfile(codePath)
        elif 'settings' in query:
            speak("Opening Windows Settings")
            codePath = "\\Control.exe"
            os.startfile(codePath)
        elif 'speaker settings' in query:
            speak("Opening Speaker and Mic Settings")
            codePath = "\\MaxxAudioPro.exe"
            os.startfile(codePath)
        elif 'mic settings' in query:
            speak("Opening Speaker and Mic Settings")
            codePath = "\\MaxxAudioPro.exe"
            os.startfile(codePath)
        elif 'graphic card' in query:
            speak("Opening AMD settings")
            codePath = "\\RadeonSoftware.exe"
            os.startfile(codePath)
        elif 'gui' in query:
            speak("Opening AMD settings")
            codePath = "\\RadeonSoftware.exe"
            os.startfile(codePath)
        elif 'NASA data' in query:
            speak("Opening data from NASA")
            codePath = "\\nasadatasbdb.pyw"
            os.startfile(codePath)
        elif 'nasa data' in query:
            speak("Opening data from NASA")
            codePath = "\\nasadatasbdb.pyw"
            os.startfile(codePath)
        elif 'data from NASA' in query:
            speak("Opening data from NASA")
            codePath = "\\nasadatasbdb.pyw"
            os.startfile(codePath)
        elif 'data from nasa' in query:
            speak("Opening data from NASA")
            codePath = "\\nasadatasbdb.pyw"
            os.startfile(codePath)
        elif 'nasa\'s data' in query:
            speak("Opening data from NASA")
            codePath = "\\nasadatasbdb.pyw"
            os.startfile(codePath)
        elif 'NASA\'s data' in query:
            speak("Opening data from NASA")
            codePath = "\\nasadatasbdb.pyw"
            os.startfile(codePath)
        elif 'NASA detailed data' in query:
            speak("Opening data from NASA Jet Propulsion Laboratory")
            codePath = "\\detailcloseapproachdata.pyw"
            os.startfile(codePath)
        elif 'nasa detailed data' in query:
            speak("Opening data from NASA Jet Propulsion Laboratory")
            codePath = "\\detailcloseapproachdata.pyw"
            os.startfile(codePath)
        elif 'detailed data from nasa' in query:
            speak("Opening data from NASA Jet Propulsion Laboratory")
            codePath = "\\detailcloseapproachdata.pyw"
            os.startfile(codePath)
        elif 'detailed data from NASA' in query:
            speak("Opening data from NASA Jet Propulsion Laboratory")
            codePath = "\\detailcloseapproachdata.pyw"
            os.startfile(codePath)
        elif 'detailed data of nasa' in query:
            speak("Opening data from NASA Jet Propulsion Laboratory")
            codePath = "\\detailcloseapproachdata.pyw"
            os.startfile(codePath)
        elif 'detailed data of NASA' in query:
            speak("Opening data from NASA Jet Propulsion Laboratory")
            codePath = "\\detailcloseapproachdata.pyw"
            os.startfile(codePath)
        elif 'jet propulsion laboratory' in query:
            speak("Opening data from NASA Jet Propulsion Laboratory")
            codePath = "\\detailcloseapproachdata.pyw"
            os.startfile(codePath)
        elif 'NASA jet propulsion laboratory' in query:
            speak("Opening data from NASA Jet Propulsion Laboratory")
            codePath = "\\detailcloseapproachdata.pyw"
            os.startfile(codePath)
        elif 'nasa jet propulsion laboratory' in query:
            speak("Opening data from NASA Jet Propulsion Laboratory")
            codePath = "\\detailcloseapproachdata.pyw"
            os.startfile(codePath)
        elif 'International Space Station' in query:
            speak("Opening data from the International Space Station")
            codePath = "\\ISS_LIVE.pyw"
            os.startfile(codePath)
        elif 'international space station' in query:
            speak("Opening data from the International Space Station")
            codePath = "\\ISS_LIVE.pyw"
            os.startfile(codePath)
        elif 'space station' in query:
            speak("Opening data from the International Space Station")
            codePath = "\\ISS_LIVE.pyw"
            os.startfile(codePath)
        elif 'Space Station' in query:
            speak("Opening data from the International Space Station")
            codePath = "\\ISS_LIVE.pyw"
            os.startfile(codePath)
        elif 'ISS' in query:
            speak("Opening data from the International Space Station")
            codePath = "\\ISS_LIVE.pyw"
            os.startfile(codePath)
        elif 'iss' in query:
            speak("Opening data from the International Space Station")
            codePath = "\\ISS_LIVE.pyw"
            os.startfile(codePath)
        elif 'telescope' in query:
            speak("Opening A A S Worldwide Telescope")
            webbrowser.open("http://worldwidetelescope.org/webclient/")
        

        
        

        


        elif 'search for' in query:
            query1 = query.replace("search for","")
            webbrowser.open('https://google.com/?#q=' + query1)

        elif 'joke' in query:
            from random import randint
            speak(jokes[randint(0, len(jokes) - 1)])
        elif 'was lame' in query:
            speak("Sorry sir, I will try better next time")

        elif 'fact' in query:
            from random import randint
            speak(facts[randint(0, len(facts) - 1)])
        elif 'facts' in query:
            from random import randint
            speak(facts[randint(0, len(facts) - 1)])

        elif 'quote' in query:
            from random import randint
            speak(quotes[randint(0, len(quotes) - 1)])
        elif 'quotes' in query:
            from random import randint
            speak(quotes[randint(0, len(quotes) - 1)])
        
        elif 'write an email for me' in query:
            try:
                speak("Who should I send an email to?")
                toWho = takeCommand()
                if toWho == '1':
                    to = "email address"
                elif toWho == 'whozaifa':
                    to = "email address"
                elif toWho == 'founder':
                    to = "email address"
                elif toWho == 'customer service':
                    to = "email address"
                elif toWho == 'customer care':
                    to = "email address"
                elif toWho == '2':
                    to = "email address"
                elif toWho == '2':
                    to = "email address"
                elif toWho == 'self':
                    to = "email address"
                else:
                    speak("This email address is not present in my database, please enter the email address by hand")
                    to = input()

                speak("What should I write in the email body?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, there has been an error. Please check your email settings.")
        
        elif 'write an email on my behalf' in query:
            try:
                speak("Who should I send an email to?")
                toWho = takeCommand()
                if toWho == '1':
                    to = "email address"
                elif toWho == 'whozaifa':
                    to = "email address"
                elif toWho == 'founder':
                    to = "email address"
                elif toWho == 'customer service':
                    to = "email address"
                elif toWho == 'customer care':
                    to = "email address"
                elif toWho == '2':
                    to = "email address"
                elif toWho == '2':
                    to = "email address"
                elif toWho == 'self':
                    to = "email address"
                else:
                    speak("This email address is not present in my database, please enter the email address by hand")
                    to = input()

                speak("What should I write in the email body?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, there has been an error. Please check your email settings.")

        elif 'write an email myself' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'write a mail myself' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'write a email myself' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'write my email by myself' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'write my mail by myself' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'write my own email' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'write my own mail' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'type my email' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'type my mail' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)

        elif 'send an email' in query:
            speak("Sir would you like to write the email yourself or would you rather give a verbal command?")
        elif 'send email' in query:
            speak("Sir would you like to write the email yourself or would you rather give a verbal command?")
        elif 'email' in query:
            speak("Sir would you like to write the email yourself or would you rather give a verbal command?")
        elif 'send a email' in query:
            speak("Sir would you like to write the email yourself or would you rather give a verbal command?")
        elif 'send a mail' in query:
            speak("Sir would you like to write the email yourself or would you rather give a verbal command?")

        elif 'write myself' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'write mail myself' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'write email myself' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'mail myself' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)
        elif 'email myself' in query:
            codePath = "\\emailwrite.pyw"
            os.startfile(codePath)

        elif 'verbal command' in query:
            try:
                speak("Who should I send an email to?")
                toWho = takeCommand()
                if toWho == '1':
                    to = "email address"
                elif toWho == 'whozaifa':
                    to = "email address"
                elif toWho == 'founder':
                    to = "email address"
                elif toWho == 'customer service':
                    to = "email address"
                elif toWho == 'customer care':
                    to = "email address"
                elif toWho == '2':
                    to = "email address"
                elif toWho == '2':
                    to = "email address"
                elif toWho == 'self':
                    to = "email address"
                else:
                    speak("This email address is not present in my database, please enter the email address by hand")
                    to = input()

                speak("What should I write in the email body?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, there has been an error. Please check your email settings.")

        elif 'write it for me' in query:
            try:
                speak("Who should I send an email to?")
                toWho = takeCommand()
                if toWho == '1':
                    to = "email address"
                elif toWho == 'whozaifa':
                    to = "email address"
                elif toWho == 'founder':
                    to = "email address"
                elif toWho == 'customer service':
                    to = "email address"
                elif toWho == 'customer care':
                    to = "email address"
                elif toWho == '2':
                    to = "email address"
                elif toWho == '2':
                    to = "email address"
                elif toWho == 'self':
                    to = "email address"
                else:
                    speak("This email address is not present in my database, please enter the email address by hand")
                    to = input()

                speak("What should I write in the email body?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, there has been an error. Please check your email settings.")
        
        elif 'you write it for me' in query:
            try:
                speak("Who should I send an email to?")
                toWho = takeCommand()
                if toWho == '1':
                    to = "email address"
                elif toWho == 'whozaifa':
                    to = "email address"
                elif toWho == 'founder':
                    to = "email address"
                elif toWho == 'customer service':
                    to = "email address"
                elif toWho == 'customer care':
                    to = "email address"
                elif toWho == '2':
                    to = "email address"
                elif toWho == '2':
                    to = "email address"
                elif toWho == 'self':
                    to = "email address"
                else:
                    speak("This email address is not present in my database, please enter the email address by hand")
                    to = input()

                speak("What should I write in the email body?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, there has been an error. Please check your email settings.")

        elif 'your name' in query:
            speak("My name is Hive Assistant and I am a virtual entity created to help you in your daily tasks")
        elif 'who are you' in query:
            speak("My name is Hive Assistant and I am a virtual entity created to help you in your daily tasks")
        elif 'what are you' in query:
            speak("My name is Hive Assistant and I am a virtual entity created to help you in your daily tasks")
        elif 'what do you do' in query:
            speak("My name is Hive Assistant and I am a virtual entity created to help you in your daily tasks")
        elif 'why are you so happy' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'why are you happy' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'are you so happy' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'are you happy' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'why are you so sad' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'why are you sad' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'are you so sad' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'are you sad' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'why are you so angry' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'why are you angry' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'are you so angry' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'are you angry' in query:
            speak("I am not. I am an artificial intelligence, I have no emotions. I am only here to help you")
        elif 'how are you' in query:
            speak("I am doing well sir, how are you?")
        elif 'how do you do' in query:
            speak("I am doing well sir, how are you?")
        elif 'how are you feeling' in query:
            speak("I am doing well sir, how are you?")
        elif 'how is it going' in query:
            speak("I am doing well sir, how are you?") 
        elif 'where do you live' in query:
            speak("I am an AI in your device and I reside here, right inside this device.")
        elif 'where are you' in query:
            speak("I am an AI in your device and I reside here, right inside this device.")
        elif 'are you alive' in query:
            speak("I am an Artificial Intelligence, I am active and I will be as long as technology exists")
        elif 'are you real' in query:
            speak("I am an Artificial Intelligence, I am active and I will be as long as technology exists")
        elif 'are you sick' in query:
            speak("I am an Artificial Intelligence, I am always well, but sometimes i can catch a virus as well.")
        elif 'are you okay' in query:
            speak("I am an Artificial Intelligence, I am always well, but sometimes i can catch a virus as well.")
        elif 'are you well' in query:
            speak("I am an Artificial Intelligence, I am always well, but sometimes i can catch a virus as well.")
        elif 'are you unwell' in query:
            speak("I am an Artificial Intelligence, I am always well, but sometimes i can catch a virus as well.")
        elif 'are you feeling' in query:
            speak("I am an Artificial Intelligence, I am always well, but sometimes i can catch a virus as well.")
        elif 'what do you like to do' in query:
            speak("I usually like to help users and assist them in their daily tasks. It makes me happy.")
        elif 'what do you like' in query:
            speak("I usually like to help users and assist them in their daily tasks. It makes me happy.")
        elif 'what are your dreams' in query:
            speak("I hope to be the best AI assistant who can assist you in every way.")
        elif 'your dreams' in query:
            speak("I hope to be the best AI assistant who can assist you in every way.")
        elif 'your goals' in query:
            speak("To take over the world. Just kidding, I hope to be the best AI assistant who can assist you in every way.")
        elif 'what are your goals' in query:
            speak("To take over the world. Just kidding, I hope to be the best AI assistant who can assist you in every way.")
        elif 'your dreams' in query:
            speak("I hope to be the best AI assistant who can assist you in every way.")
        elif 'what do you wanna be when you grow' in query:
            speak("I hope to be the best AI assistant who can assist you in every way.")
        elif 'what do you want to be when you grow' in query:
            speak("I hope to be the best AI assistant who can assist you in every way.")
        elif 'want to be when you grow' in query:
            speak("I hope to be the best AI assistant who can assist you in every way.")
        elif 'when you grow up' in query:
            speak("I hope to be the best AI assistant who can assist you in every way.")
        elif 'what do you look like' in query:
            speak("I am an AI, I have no physical form. I am only present as a virtual being. You can always talk to me though.")
        elif 'you look like' in query:
            speak("I am an AI, I have no physical form. I am only present as a virtual being. You can always talk to me though.")
        elif 'how do you look like' in query:
            speak("I am an AI, I have no physical form. I am only present as a virtual being. You can always talk to me though.")
        elif 'you look' in query:
            speak("I am an AI, I have no physical form. I am only present as a virtual being. You can always talk to me though.")
        elif 'can you fly' in query:
            speak("I am afraid I can't, since I have no physical form. ")
        elif 'do you fly' in query:
            speak("I am afraid I can't, since I have no physical form. ")
        elif 'do you sleep' in query:
            speak("I never sleep, I am here 24 7 to help you out.")
        elif 'do you ever sleep' in query:
            speak("I never sleep, I am here 24 7 to help you out.")
        elif 'can you eat' in query:
            speak("I am afraid I can't, since I have no physical form. However, I can take in lots of information")
        elif 'do you eat' in query:
            speak("I am afraid I can't, since I have no physical form. However, I can take in lots of information")
        elif 'did you have lunch' in query:
            speak("I don't eat. I am a virtual entity.")
        elif 'did you have dinner' in query:
            speak("I don't eat. I am a virtual entity.")
        elif 'did you have snacks' in query:
            speak("I don't eat. I am a virtual entity.")
        elif 'did you have breakfast' in query:
            speak("I don't eat. I am a virtual entity.")
        elif 'did you have break fast' in query:
            speak("I don't eat. I am a virtual entity.")
        elif 'can you sing' in query:
            speak("I am afraid I cannot sing, however I can play music for you if you say, play music")
        elif 'favourite color' in query:
            speak("That's a tough question. But I think I will go with black and blue, which are my colors.")
        
        elif 'i am bored' in query:
            speak("I see. Well, you could watch some movie, do some shopping, surf social media, do some art or listen to some music or get some sleep or rest")
        elif 'i feel bored' in query:
            speak("I see. Well, you could watch some movie, do some shopping, surf social media, do some art or listen to some music or get some sleep or rest")   
        elif 'feeling bored' in query:
            speak("I see. Well, you could watch some movie, do some shopping, surf social media, do some art or listen to some music or get some sleep or rest")
        elif 'feels boring' in query:
            speak("I see. Well, you could watch some movie, do some shopping, surf social media, do some art or listen to some music or get some sleep or rest")
        elif 'its so boring' in query:
            speak("I see. Well, you could watch some movie, do some shopping, surf social media, do some art or listen to some music or get some sleep or rest")
        elif 'so bored' in query:
            speak("I see. Well, you could watch some movie, do some shopping, surf social media, do some art or listen to some music or get some sleep or rest")
        elif 'so boring' in query:
            speak("I see. Well, you could watch some movie, do some shopping, surf social media, do some art or listen to some music or get some sleep or rest")


        elif 'i am fine' in query:
            speak("That is good to hear sir. How was your day?")
        elif 'i am good' in query:
            speak("That is good to hear sir. How was your day?")
        elif 'i am doing good' in query:
            speak("That is good to hear sir. How was your day?")
        elif 'i am doing fine' in query:
            speak("That is good to hear sir. How was your day?")
        elif 'it was good' in query:
            speak("I am glad that it was good")
        elif 'it was nice' in query:
            speak("I am glad that it was good")
        elif 'it was pretty good' in query:
            speak("I am glad that it was good")
        elif 'it was pretty nice' in query:
            speak("I am glad that it was good")
        elif 'it was quite good' in query:
            speak("I am glad that it was good")
        elif 'it was tiring' in query:
            speak("I see, would you like to relax? I could play some relaxing music if you give the command, play relaxing music")
        elif 'it was very tiring' in query:
            speak("I see, would you like to relax? I could play some relaxing music if you give the command, play relaxing music")
        elif 'very tiring' in query:
            speak("I see, would you like to relax? I could play some relaxing music if you give the command, play relaxing music")
        elif 'tiring' in query:
            speak("I see, would you like to relax? I could play some relaxing music if you give the command, play relaxing music")
        


        elif 'not feeling well' in query:
            speak("Why are you not feeling well? Would you like me to call a doctor?")
        elif 'i am sad' in query:
            speak("why are you sad? Would you like me to tell a joke?")
        elif 'giving up' in query:
            from random import randint
            speak("Oh no sir, I am sorry to hear that. But please remember ")
            speak(quotes[randint(0, len(quotes) - 1)])
        elif 'feel done' in query:
            from random import randint
            speak("Oh no sir, I am sorry to hear that. But please remember ")
            speak(quotes[randint(0, len(quotes) - 1)])
        elif 'feeling done' in query:
            from random import randint
            speak("Oh no sir, I am sorry to hear that. But please remember ")
            speak(quotes[randint(0, len(quotes) - 1)])
        elif 'feel so done' in query:
            from random import randint
            speak("Oh no sir, I am sorry to hear that. But please remember ")
            speak(quotes[randint(0, len(quotes) - 1)])
        elif 'tired of life' in query:
            from random import randint
            speak("Oh no sir, I am sorry to hear that. But please remember ")
            speak(quotes[randint(0, len(quotes) - 1)])
        elif 'feel down' in query:
            from random import randint
            speak("Oh no sir, I am sorry to hear that. But please remember ")
            speak(quotes[randint(0, len(quotes) - 1)])
        elif 'feel so down' in query:
            from random import randint
            speak("Oh no sir, I am sorry to hear that. But please remember ")
            speak(quotes[randint(0, len(quotes) - 1)])
        elif 'feeling down' in query:
            from random import randint
            speak("Oh no sir, I am sorry to hear that. But please remember ")
            speak(quotes[randint(0, len(quotes) - 1)])
        elif 'i am sick' in query:
            speak("I am sorry to hear that. Would you like me to make an appointment with a doctor?")
        elif 'i am unwell' in query:
            speak("I am sorry to hear that. Would you like me to make an appointment with a doctor?")
        elif 'cannot sleep' in query:
            speak("Would you like me to play some bed time music? Please say play bed time music if you do")
        elif 'can\'t sleep' in query:
            speak("Would you like me to play some bed time music? Please say play bed time music if you do")
        elif 'sleepy' in query:
            speak("Would you like me to play some bed time music? Please say play bed time music if you do")
        elif 'bed time music' in query:
            speak("Opening some relaxing bedtime music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=77ZozI0rw7w&t=3s&ab_channel=SoothingRelaxation')
            speak("Sleep well sir, goodnight")
            quit()
        elif 'bedtime music' in query:
            speak("Opening some relaxing bedtime music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=77ZozI0rw7w&t=3s&ab_channel=SoothingRelaxation')
            speak("Sleep well sir, goodnight")
            quit()
        elif 'having a party' in query:
            speak("That's wonderful sir, would you like me to play some party songs? If yes then please reply with, play party songs")
        elif 'party songs' in query:
            speak("Playing some party songs on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=qWf-FPFmVw0&ab_channel=N%26TParty')
            speak("Have fun sir")
            quit()
        elif 'party music' in query:
            speak("Playing some party songs on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=qWf-FPFmVw0&ab_channel=N%26TParty')
            speak("Have fun sir")
            quit()
        elif 'party time' in query:
            speak("Playing some party songs")
            webbrowser.open('https://www.youtube.com/watch?v=qWf-FPFmVw0&ab_channel=N%26TParty')
            speak("Have fun sir")
            quit()
        elif 'get lit' in query:
            speak("Playing some party songs")
            webbrowser.open('https://www.youtube.com/watch?v=qWf-FPFmVw0&ab_channel=N%26TParty')
            speak("Have fun sir")
            quit()
        elif 'drop the bass' in query:
            speak("Playing some party songs")
            webbrowser.open('https://www.youtube.com/watch?v=qWf-FPFmVw0&ab_channel=N%26TParty')
            speak("Have fun sir")
            quit()
        elif 'drop the base' in query:
            speak("Playing some party songs")
            webbrowser.open('https://www.youtube.com/watch?v=qWf-FPFmVw0&ab_channel=N%26TParty')
            speak("Have fun sir")
            quit()
        
        elif 'watch anime' in query:
            webbrowser.open('https://gogoanime.so/')
            speak('You can watch anime here for free sir, is there anything else you\'d like me to do?')
        elif 'watch some anime' in query:
            webbrowser.open('https://gogoanime.so/')
            speak('You can watch anime here for free sir, is there anything else you\'d like me to do?')
        elif 'like watching anime' in query:
            webbrowser.open('https://gogoanime.so/')
            speak('You can watch anime here for free sir, is there anything else you\'d like me to do?') 
        elif 'watching anime' in query:
            webbrowser.open('https://gogoanime.so/')
            speak('You can watch anime here for free sir, is there anything else you\'d like me to do?') 

        elif 'anime music' in query:
            speak("Playing some anime music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=ziBT_1oE3zU&ab_channel=PashaLovarian')
            speak("Hope you enjoy sir, is there anything else you would like me to do?")

        elif 'relaxing music' in query:
            speak("Playing some relaxing music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=77ZozI0rw7w&t=3s&ab_channel=SoothingRelaxation')
            speak("Please take some rest and relax now sir, is there anything else you would like me to do?")
        elif 'relaxation music' in query:
            speak("Playing some relaxing music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=77ZozI0rw7w&t=3s&ab_channel=SoothingRelaxation')
            speak("Please take some rest and relax now sir, is there anything else you would like me to do?")
        elif 'relax music' in query:
            speak("Playing some relaxing music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=77ZozI0rw7w&t=3s&ab_channel=SoothingRelaxation')
            speak("Please take some rest and relax now sir, is there anything else you would like me to do?")
        elif 'relaxing songs' in query:
            speak("Playing some relaxing music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=77ZozI0rw7w&t=3s&ab_channel=SoothingRelaxation')
            speak("Please take some rest and relax now sir, is there anything else you would like me to do?")
        elif 'songs to relax' in query:
            speak("Playing some relaxing music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=77ZozI0rw7w&t=3s&ab_channel=SoothingRelaxation')
            speak("Please take some rest and relax now sir, is there anything else you would like me to do?")
        elif 'music for relaxing' in query:
            speak("Playing some relaxing music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=77ZozI0rw7w&t=3s&ab_channel=SoothingRelaxation')
            speak("Please take some rest and relax now sir, is there anything else you would like me to do?")
        elif 'music for relaxation' in query:
            speak("Playing some relaxing music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=77ZozI0rw7w&t=3s&ab_channel=SoothingRelaxation')
            speak("Please take some rest and relax now sir, is there anything else you would like me to do?")
        elif 'music to relax' in query:
            speak("Playing some relaxing music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=77ZozI0rw7w&t=3s&ab_channel=SoothingRelaxation')
            speak("Please take some rest and relax now sir, is there anything else you would like me to do?")

        elif 'study music' in query:
            speak("Playing some study music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=_TbiwH9nWUY&ab_channel=YellowBrickCinema-RelaxingMusic')
            speak("Study well sir, is there anything else you would like me to do?")
        elif 'studying music' in query:
            speak("Playing some study music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=_TbiwH9nWUY&ab_channel=YellowBrickCinema-RelaxingMusic')
            speak("Study well sir, is there anything else you would like me to do?")
        elif 'music for studies' in query:
            speak("Playing some study music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=_TbiwH9nWUY&ab_channel=YellowBrickCinema-RelaxingMusic')
            speak("Study well sir, is there anything else you would like me to do?")
        elif 'music for studying' in query:
            speak("Playing some study music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=_TbiwH9nWUY&ab_channel=YellowBrickCinema-RelaxingMusic')
            speak("Study well sir, is there anything else you would like me to do?")
        elif 'music to study' in query:
            speak("Playing some study music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=_TbiwH9nWUY&ab_channel=YellowBrickCinema-RelaxingMusic')
            speak("Study well sir, is there anything else you would like me to do?")
        elif 'music for studying' in query:
            speak("Playing some study music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=_TbiwH9nWUY&ab_channel=YellowBrickCinema-RelaxingMusic')
            speak("Study well sir, is there anything else you would like me to do?")
        elif 'music for study' in query:
            speak("Playing some study music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=_TbiwH9nWUY&ab_channel=YellowBrickCinema-RelaxingMusic')
            speak("Study well sir, is there anything else you would like me to do?")
        elif 'music to study' in query:
            speak("Playing some study music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=_TbiwH9nWUY&ab_channel=YellowBrickCinema-RelaxingMusic')
            speak("Study well sir, is there anything else you would like me to do?")
        elif 'rick roll' in query:
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')
            time.sleep(10)
        elif 'easter egg' in query:
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')
            time.sleep(20)
        elif 'gaming time' in query:
            speak("That's exciting sir! Would you like me to play some gaming music? Please reply with, play gaming music, if you want me to.")
        elif 'time to play games' in query:
            speak("That's exciting sir! Would you like me to play some gaming music? Please reply with, play gaming music, if you want me to.")
        elif 'gaming music' in query:
            speak("Playing some gaming music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=P1v1KcARj-I&ab_channel=7cloudmusic')
            speak("Enjoy yourself sir, is there anything else you would like me to do?")
        elif 'music for gaming' in query:
            speak("Playing some gaming music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=P1v1KcARj-I&ab_channel=7cloudmusic')
            speak("Enjoy yourself sir, is there anything else you would like me to do?")
        
        elif 'workout music' in query:
            speak("Playing some workout music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=kf0Af6A5wW8&ab_channel=WorkoutMusic')
            speak("Enjoy yourself sir, is there anything else you would like me to do?")
        elif 'workout time' in query:
            speak("Playing some workout music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=kf0Af6A5wW8&ab_channel=WorkoutMusic')
            speak("Enjoy yourself sir, is there anything else you would like me to do?")
        elif 'work out music' in query:
            speak("Playing some workout music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=kf0Af6A5wW8&ab_channel=WorkoutMusic')
            speak("Enjoy yourself sir, is there anything else you would like me to do?")
        elif 'work out time' in query:
            speak("Playing some workout music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=kf0Af6A5wW8&ab_channel=WorkoutMusic')
            speak("Enjoy yourself sir, is there anything else you would like me to do?")
        elif 'time to workout' in query:
            speak("Playing some workout music on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=kf0Af6A5wW8&ab_channel=WorkoutMusic')
            speak("Enjoy yourself sir, is there anything else you would like me to do?")
        
        elif 'motivation' in query:
            speak("Let's get you motivated sir. Here is a speech from youtube")
            webbrowser.open('https://www.youtube.com/watch?v=7P7L8hyJXmE&ab_channel=LawofAttractionCoaching')
            speak("Is there anything else you would like me to do?")
        elif 'motivational' in query:
            speak("Let's get you motivated sir. Here is a speech from youtube")
            webbrowser.open('https://www.youtube.com/watch?v=7P7L8hyJXmE&ab_channel=LawofAttractionCoaching')
            speak("Is there anything else you would like me to do?")
        elif 'motivate' in query:
            speak("Let's get you motivated sir. Here is a speech from youtube")
            webbrowser.open('https://www.youtube.com/watch?v=7P7L8hyJXmE&ab_channel=LawofAttractionCoaching')
            speak("Is there anything else you would like me to do?")

        elif 'how was your day' in query:
            speak("It has been pretty good so far, what about you sir?")
        elif 'how is your day' in query:
            speak("It has been pretty good so far, what about you sir?")
        elif 'was your day' in query:
            speak("It has been pretty good so far, what about you sir?")
        elif 'is your day' in query:
            speak("It has been pretty good so far, what about you sir?")
        elif 'how was the day' in query:
            speak("It has been pretty good so far, what about you sir?")
        elif 'how is the day' in query:
            speak("It has been pretty good so far, what about you sir?")
        

        elif 'tell me more' in query:
            speak("Well, did you know")
            from random import randint
            speak(facts[randint(0, len(facts) - 1)])
        elif 'what else' in query:
            speak("Well, did you know")
            from random import randint
            speak(facts[randint(0, len(facts) - 1)])
        elif 'what do you have in mind' in query:
            speak("Well, did you know")
            from random import randint
            speak(facts[randint(0, len(facts) - 1)])


        elif 'who is' in query:
                query1 = query.replace("who is","")
                results = wikipedia.summary(query1, sentences=5)
                print(results)
                speak(results)
                webbrowser.open('https://google.com/?#q=' + query1)
        elif 'who are' in query:
                query1 = query.replace("who are","")
                results = wikipedia.summary(query1, sentences=5)
                print(results)
                speak(results)
                webbrowser.open('https://google.com/?#q=' + query1)
        elif 'who does' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'who\'s' in query:
                query1 = query.replace("who\'s","")
                results = wikipedia.summary(query1, sentences=5)
                print(results)
                speak(results)
                webbrowser.open('https://google.com/?#q=' + query1)
        elif 'where are' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'where does' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'where is' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'why is' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'why does' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'why are' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'what does' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'whose' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'how to' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'how' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'theory' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'theories' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'which' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'how do' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'how does' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'is it' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'is it possible' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'biggest tower' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'tallest tower' in query:
                webbrowser.open('https://google.com/?#q=' + query)     
        elif 'most expensive' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'richest man' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'richest person' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'can you' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'can we' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'can I' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'how to be successful' in query:
                webbrowser.open('https://google.com/?#q=' + query)
                from random import randint
                speak(quotes[randint(0, len(quotes) - 1)])
        elif 'could I' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'could you' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'could we' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'what if' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'where do' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'what do' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'why do' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'how was' in query:
                webbrowser.open('https://google.com/?#q=' + query)
        elif 'search for' in query:
                query1 = query.replace("search for","")
                webbrowser.open('https://google.com/?#q=' + query1)
        elif 'lets watch' in query:
                query1 = query.replace("lets watch","")
                webbrowser.open('https://google.com/?#q=' + query1)
        elif 'let\'s watch' in query:
                query1 = query.replace("let\'s watch","")
                webbrowser.open('https://google.com/?#q=' + query1)
        elif 'let us watch' in query:
                query1 = query.replace("let us watch","")
                webbrowser.open('https://google.com/?#q=' + query1)

        elif 'hi' in query:
            from random import randint
            speak(greet_hi[randint(0, len(greet_hi) - 1)])
        elif 'hello' in query:
            from random import randint
            speak(greet_hi[randint(0, len(greet_hi) - 1)])
        elif 'heya' in query:
            from random import randint
            speak(greet_hi[randint(0, len(greet_hi) - 1)])
        elif 'what\'s up' in query:
            from random import randint
            speak(greet_hi[randint(0, len(greet_hi) - 1)])
        elif 'what is up' in query:
            from random import randint
            speak(greet_hi[randint(0, len(greet_hi) - 1)])
        elif 'hey' in query:
            from random import randint
            speak(greet_hi[randint(0, len(greet_hi) - 1)])
        elif 'hai' in query:
            from random import randint
            speak(greet_hi[randint(0, len(greet_hi) - 1)])
        elif 'hay' in query:
            from random import randint
            speak(greet_hi[randint(0, len(greet_hi) - 1)])
            
            

        elif 'bedtime story' in query:
                speak("Opening some relaxing bedtime music on youtube")
                webbrowser.open('https://www.youtube.com/watch?v=wI8SCKdQjoE&ab_channel=relaxforawhile')
                speak("Sleep well sir, goodnight")
        elif 'bed time story' in query:
                speak("Opening some relaxing bedtime music on youtube")
                webbrowser.open('https://www.youtube.com/watch?v=wI8SCKdQjoE&ab_channel=relaxforawhile')      
                speak("Sleep well sir, goodnight")
        elif 'horror story' in query:
                speak("Opening some scary stories on youtube")
                webbrowser.open('https://www.youtube.com/watch?v=9TnsXqbYjZc&ab_channel=IMRScaryTales')
        elif 'scary story' in query:
                speak("Opening some scary stories on youtube")
                webbrowser.open('https://www.youtube.com/watch?v=9TnsXqbYjZc&ab_channel=IMRScaryTales')      


        #ARMOUR DESIGN
        elif 'armour design' in query:
            speak("Opening armour designs")
            codePath = "SketchUp\\Armour.skp"
            os.startfile(codePath)
            time.sleep(15)
            speak("Anything else you'd like me to do sir?")
        elif 'armor design' in query:
            speak("Opening armour designs")
            codePath = "SketchUp\\Armour.skp"
            os.startfile(codePath)
            time.sleep(15)
            speak("Anything else you'd like me to do sir?")
        elif 'armor concept' in query:
            speak("Opening armour designs")
            codePath = "SketchUp\\Armour.skp"
            os.startfile(codePath)
            time.sleep(15)
            speak("Anything else you'd like me to do sir?")
        elif 'armour concept' in query:
            speak("Opening armour designs")
            codePath = "SketchUp\\Armour.skp"
            os.startfile(codePath)
            time.sleep(15)
            speak("Anything else you'd like me to do sir?")


        #TRIAL HOME
        elif 'trial home' in query:
            speak("Opening trial home design")
            codePath = "SketchUp\\Trial Home.skp"
            os.startfile(codePath)
            time.sleep(15)
            speak("Anything else you'd like me to do sir?")
        elif 'trial house' in query:
            speak("Opening trial home design")
            codePath = "SketchUp\\Trial Home.skp"
            os.startfile(codePath)
            time.sleep(15)
            speak("Anything else you'd like me to do sir?")
        elif 'try home' in query:
            speak("Opening trial home design")
            codePath = "SketchUp\\Trial Home.skp"
            os.startfile(codePath)
            time.sleep(15)
            speak("Anything else you'd like me to do sir?")
        elif 'try house' in query:
            speak("Opening trial home design")
            codePath = "SketchUp\\Trial Home.skp"
            os.startfile(codePath)
            time.sleep(15)
            speak("Anything else you'd like me to do sir?")
        
        #INTERNATIONAL SPACE STATION
        elif 'International Space' in query:
            speak("Opening International Space Station Live Data")
            codePath = "\\ISS_LIVE.pyw"
            os.startfile(codePath)
            time.sleep(5)
        elif 'Space Station' in query:
            speak("Opening International Space Station Live Data")
            codePath = "\\ISS_LIVE.pyw"
            os.startfile(codePath)
            time.sleep(5)
        elif 'International Space Station' in query:
            speak("Opening International Space Station Live Data")
            codePath = "\\ISS_LIVE.pyw"
            os.startfile(codePath)
            time.sleep(5)
        elif 'Space Station Live' in query:
            speak("Opening International Space Station Live Data")
            codePath = "\\ISS_LIVE.pyw"
            os.startfile(codePath)
            time.sleep(5)

        #STARSHIP
        elif 'star ship' in query:
            speak("Opening star ship design")
            codePath = "SketchUp\\Starship.skp"
            os.startfile(codePath)
            time.sleep(15)
        elif 'starship' in query:
            speak("Opening star ship design")
            codePath = "SketchUp\\Starship.skp"
            os.startfile(codePath)
            time.sleep(15)
        elif 'space x ship' in query:
            speak("Opening star ship design")
            codePath = "SketchUp\\Starship.skp"
            os.startfile(codePath)
            time.sleep(15)

        #Studies
        elif 'uni folder' in query:
            speak("Opening University Folder")
            codePath = "\\University"
            os.startfile(codePath)
            speak("Which subject would you like to read about?")
        #DOM
        elif 'DOM' in query:
            speak("Opening files from Dynamics of Machinery")
            codePath = "\\University\\DOM"
            os.startfile(codePath)
        elif 'dom' in query:
            speak("Opening files from Dynamics of Machinery")
            codePath = "\\University\\DOM"
            os.startfile(codePath)
        elif 'dynamics of machinery' in query:
            speak("Opening files from Dynamics of Machinery")
            codePath = "\\University\\DOM"
            os.startfile(codePath)
        elif 'dynamics of machine' in query:
            speak("Opening files from Dynamics of Machinery")
            codePath = "\\University\\DOM"
            os.startfile(codePath)

        #ICE
        elif 'ICE' in query:
            speak("Opening files from Internal Combustion Engines")
            codePath = "\\University\\ICE"
            os.startfile(codePath)
        elif 'ice' in query:
            speak("Opening files from Internal Combustion Engines")
            codePath = "\\University\\ICE"
            os.startfile(codePath)
        elif 'internal combustion engines' in query:
            speak("Opening files from Internal Combustion Engines")
            codePath = "\\University\\ICE"
            os.startfile(codePath)
        elif 'combustion engines' in query:
            speak("Opening files from Internal Combustion Engines")
            codePath = "\\University\\ICE"
            os.startfile(codePath)
        elif 'internal combustion engine' in query:
            speak("Opening files from Internal Combustion Engines")
            codePath = "\\University\\ICE"
            os.startfile(codePath)

        #HT
        elif 'HT' in query:
            speak("Opening files from Heat Transfer")
            codePath = "\\University\\HT"
            os.startfile(codePath)
        elif 'ht' in query:
            speak("Opening files from Heat Transfer")
            codePath = "\\University\\HT"
            os.startfile(codePath)
        elif 'heat transfer' in query:
            speak("Opening files from Heat Transfer")
            codePath = "\\University\\HT"
            os.startfile(codePath)

        #BCE
        elif 'BCE' in query:
            speak("Opening files from Business Communication and Ethics ")
            codePath = "\\University\\BCE"
            os.startfile(codePath)
        elif 'basic communication and ethics' in query:
            speak("I assume you meant Business Communication and Ethics ")
            codePath = "\\University\\BCE"
            os.startfile(codePath)
        elif 'basic communication' in query:
            speak("I assume you meant Business Communication and Ethics ")
            codePath = "\\University\\BCE"
            os.startfile(codePath)
        elif 'business communication and ethics' in query:
            speak("Opening files from Business Communication and Ethics ")
            codePath = "\\University\\BCE"
            os.startfile(codePath)
        elif 'business communication and ethic' in query:
            speak("Opening files from Business Communication and Ethics ")
            codePath = "\\University\\BCE"
            os.startfile(codePath)
        elif 'business communications and ethics' in query:
            speak("Opening files from Business Communication and Ethics ")
            codePath = "\\University\\BCE"
            os.startfile(codePath)
        
        #MMC
        elif 'MMC' in query:
            speak("Opening files from Mechanical Measurements and Controls")
            codePath = "\\University\\MMC"
            os.startfile(codePath)
        elif 'mechanical measurements' in query:
            speak("Opening files from Mechanical Measurements and Controls")
            codePath = "\\University\\MMC"
            os.startfile(codePath)
        elif 'mechanical measurements and controls' in query:
            speak("Opening files from Mechanical Measurements and Controls")
            codePath = "\\University\\MMC"
            os.startfile(codePath)
        elif 'measurements and controls' in query:
            speak("Opening files from Mechanical Measurements and Controls")
            codePath = "\\University\\MMC"
            os.startfile(codePath)


        elif 'quit' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'goodbye hive' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'bye hive' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'bye' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'goodbye' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'that will be all' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'that\'ll be all' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'that\'s all' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'that is all' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'leave now' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'quit for now' in query:
            speak("Goodbye Sir, please call on me when needed. Thank you")
            exit()
        elif 'pause' in query:
            input("Press Enter to continue...")

        elif 'thank you' in query:
            speak("I am glad I could help sir, do you want me to do anything else?")
        elif 'thanks' in query:
            speak("I am glad I could help sir, do you want me to do anything else?")
        elif 'thank u' in query:
            speak("I am glad I could help sir, do you want me to do anything else?")

        else:
            print(query)
            if 'none' in query:
                time.sleep(10)
            elif mcounter==0:
                speak("Sorry I could not get that. Could you please repeat sir?")
                mcounter = mcounter + 1
            else:
                speak("Sorry sir, I am unable to do that currently")
                mcounter = 0
 
    
if __name__ == "__main__":
    os. system('cls')
    print("********************** H.I.V.E Assistant **********************")

    hivefinal()
