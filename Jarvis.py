from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvis import Ui_MainWindow
import sys
from click import command
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyjokes
import pyaudio
import requests
import smtplib
import webbrowser
import time
import wikipedia
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import pywhatkit as kit
import sys  
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
from pytube import YouTube
from playsound import playsound
import keyboard
from googletrans import Translator
from keyboard import press
from keyboard import press_and_release
from keyboard import write 
from time import sleep
import wolframalpha
from plyer import notification

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING JARVIS BOT               ******")
print("*****      This tool was built by Utkarsh Mishra     ******")
print("*****       www.github.com/UtkarshMishra345         ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 120)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



def wish(self):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
        
    speak("I am Jarvis. Please tell me how may I help you") 


# for news updates
def news(self):
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=API_Key"
    #put API key....

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

#open apps
def OpenApps(self):
    speak("Ok Sir , Wait A Second!")
            
    if 'code' in self.query:
        os.startfile("------")
        speak("Your Command Has Been Completed Sir!")
            #give your path here


    elif 'facebook' in self.query:
        webbrowser.open('https://www.facebook.com/')
        speak("Your Command Has Been Completed Sir!")
            #give your path here

    elif 'instagram' in self.query:
        webbrowser.open('https://www.instagram.com/')
        speak("Your Command Has Been Completed Sir!")

    elif 'open drive' in self.query:
        webbrowser.open('https://drive.google.com')
        speak("Your Command Has Been Completed Sir!")

    elif 'map' in self.query:
        webbrowser.open('https://www.google.com/maps/')
        speak("Your Command Has Been Completed Sir!")

    elif 'youtube' in self.query:
        webbrowser.open('https://www.youtube.com')
        speak("Your Command Has Been Completed Sir!")

    elif 'browser' in self.query:
        webbrowser.open('https://www.bing.com')
        speak("Your Command Has Been Completed Sir!")

#temprature
def Temp(self):
    
        speak("tell me the name of place")
        name = self.takecommand()
        search = f"temperature in {name}"

        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_="BNeawe").text
        speak(f"The Temperature Outside Is {temperature}")

        speak("Do I Have To Tell You Another Place Temperature ?")
        next = self.takecommand()

        if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = self.takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_="BNeawe").text
            speak(f"The Temperature in {name} is {temperature}")


def Weather(self):
# import required modules
    import requests, json

    # Enter your API key here
    api_key = "----------" #api_key

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    city_name = input("Enter city name : ")

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values
        speak(" Temperature (in kelvin unit) = " + 
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))

    else:
        print(" City Not Found ")

def UniCo(self):
    # Python Program for simple Unit Converter

    num1 = input('Enter the value: ')
    unit1 = input('Which unit do you want it converted from:  ')
    unit2 = input('Which unit do you want it converted to: ')

    if unit1 == "cm" and unit2 == "m":
        ans = float(num1)/100
        print(ans)
    elif unit1 == "mm" and unit2 == "cm":
        ans = float(num1)/10
        print(ans)
    elif unit1 == "m" and unit2 == "cm":
        ans = float(num1)*100
        print(ans)
    elif unit1 == "cm" and unit2 == "mm":
        ans = float(num1)*10
        print(ans)
    elif unit1 == "mm" and unit2 == "m":
        ans = float(num1)/1000
        print(ans)
    elif unit1 == "m" and unit2 == "mm":
        ans = float(num1)*1000
        print(ans)
    elif unit1 == "km" and unit2 == "m":
        ans = float(num1)*1000
        print(ans)
    elif unit1 == "m" and unit2 == "km":
        ans = float(num1)/1000
        print(ans)
    elif unit1 == "mm" and unit2 == "km":
        ans = float(num1)/1000000
        print(ans)
    elif unit1 == "ft" and unit2 == "cm":
        ans = float(num1)*30.48
        print(ans)
    elif unit1 == "ft" and unit2 == "mm":
        ans = float(num1)*304.8
        print(ans)
    elif unit1 == "ft" and unit2 == "inch":
        ans = float(num1)*12
        print(ans)
    elif unit1 == "inch" and unit2 == "cm":
        ans = float(num1)*2.54
    elif unit1 == "inch" and unit2 == "mm":
        ans = float(num1)*25.4

def talktome(self):


    import openai
    from dotenv import load_dotenv

    openai.api_key = "------" #api_key
    load_dotenv()
    completion = openai.Completion()
    speak("Hello sir, may I help you with something")

    def QuestionsAnswer(question,chat_log = None):

        if "bye" in question:
            speak("Ok sir, I am going")
            sys.exit()

        else:

                FileLog = open("C:\\Users\\91930\\Desktop\\chat_log.txt", "r")
                chat_log_template = FileLog.read()
                FileLog.close()
                if chat_log is None:
                    chat_log = chat_log_template

                prompt = f'{chat_log}Question : {question}\nAnswer : '
                response = openai.Completion.create(
                model="text-davinci-003",
                prompt= prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )

                answer = response.choices[0].text.strip()
                qna_log_template =  chat_log_template + f"\nQuestion : {question} \n Answer : {answer}"
                FileLog =  open("C:\\Users\\91930\\Desktop\\chat_log.txt", "w")
                FileLog.write(qna_log_template)
                FileLog.close()
                return answer

    while True:

        kk = self.takecommand()
        print(QuestionsAnswer(kk))
        speak(QuestionsAnswer(kk))

def openai(self):

    import openai
    from dotenv import load_dotenv

    openai.api_key = "------" #api_key
    load_dotenv()
    completion = openai.Completion()
    speak("Tell me what do you want to know")

    def QuestionsAnswer(question,chat_log = None):

        if "bye" in question:
            speak("Ok sir, I am going")
            sys.exit()

        else:


                FileLog = open("C:\\Users\\91930\\Desktop\\qna_log.txt", "r")
                chat_log_template = FileLog.read()
                FileLog.close()
                if chat_log is None:
                    chat_log = chat_log_template

                prompt = f'{chat_log}Question : {question}\nAnswer : '
                response = openai.Completion.create(
                model="text-davinci-003",
                prompt= prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )

                answer = response.choices[0].text.strip()
                qna_log_template =  chat_log_template + f"\nQuestion : {question} \n Answer : {answer}"
                FileLog =  open("C:\\Users\\91930\\Desktop\\qna_log.txt", "w")
                FileLog.write(qna_log_template)
                FileLog.close()
                return answer



    while True:
        kk = self.takecommand()
        speak(QuestionsAnswer(kk))
        print(QuestionsAnswer(kk))



def Take_break(self):

    speak("Do you want me to remind you to take a break?")
    question = input(--- : )
      
    if "yes" in question:
        speak("Starting Sir")
      
    if "no" in question:
        speak("We will automatically start after 5 Mins Sir.")
        time.sleep(5*60)
        speak("Starting Sir")

	
	# A notification we will held that
	# Let's Start sir and with a message of
	# will tell you to take a break after 45
	# mins for 10 seconds
        while(True):

            notification.notify(title="Let's Start sir",
            message="will tell you to take a break after 45 mins",
            timeout=10)
            
            # For 45 min the will be no notification but
            # after 45 min a notification will pop up.
            time.sleep(0.5*60)

            speak("Please Take a break Sir")
            
            notification.notify(title="Break Notification",
            message="Please do use your device after sometime as you have"
            "been continuously using it for 45 mins and it will affect your eyes",
            timeout=10)


def phon(self):
            import phonenumbers

            # carrier: to know the name of
            # service provider of that phone number
            from phonenumbers import carrier

            number = input("Enter number here ...")


            service_provider = phonenumbers.parse(number)
            # Indian phone number example: +91**********
            # Nepali phone number example: +977**********

                
            # this will print the service provider name
            speak(carrier.name_for_number(service_provider,
                                        'en'))

#hindi class
def TakeHindi(self):
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

#translator
def Tran(self):
    while True:

        speak("Tell Me The Line!")
        
        line = TakeHindi(self)
        if "4" in line:
            break
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        speak(Text)

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    


    # To convert voice into text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=100, phrase_time_limit=10)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"Lucky Said: {query}")

        except Exception as e:
            # speak("Say that again please...")
            return 'none'
        query = query.lower()
        return query



    def TaskExecution(self):

        wish(self)
        
        Take_break(self)

        while True:

            self.query = self.takecommand().lower()

            # Logic building for tasks

            if "open notepad" in self.query:
                npath = 'C:\\Windows\\System32\\notepad.exe'
                #give your path here
                os.startfile(npath)
                speak("opening")

            elif "Hello" in self.query or "hello" in self.query:
                talktome(self)

            elif 'play music' in self.query:
                music_dir = "-----"
                #give your path here
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[128]))
                speak("playing music")

            # To Close any application
            elif 'close notepad' in self.query:
                speak("okay sir, closing")
                os.system("taskkill /f /im notepad.exe")

            # To find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shutdown the system" in self.query:
                os.system("shutdown /s /t 10")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 10")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "you need a break" in self.query:
                speak("Ok sir, I am going")
                break

            elif "tell me the time" in self.query:
                    # Getting current date and time using now().

                    # importing datetime module for now()
                    import datetime

                    # using now() to get current time
                    current_time = datetime.datetime.now()

                    # Printing value of now.
                    speak(current_time)

                

            elif "open camera" in self.query:
                speak("Opening")
                os.startfile("C:\\Users\\91930\\Desktop\\Camera.lnk")

            elif "open alarm" in self.query:
                speak("Opening")
                os.startfile("C:\\Users\\91930\\Desktop\\Alarms & Clock.lnk")

            elif "open mail" in self.query:
                speak("Opening")
                os.startfile("C:\\Users\\91930\\Desktop\\Mail.lnk")

            elif 'weather' in self.query:
                Weather(self)

            elif 'fact about animals' in self.query:
                from animals import Animals

                random = input("Animal name")

                animal = Animals(random)

                print(animal.image()) # Prints the url for the image
                print(animal.fact()) # Prints the fact of the animal

            elif "give me unit converter" in self.query:
                UniCo(self)


            elif "calculator" in self.query:

                # Python program for simple calculator

                # Function to add two numbers
                def add(num1, num2):
                    return num1 + num2

                # Function to subtract two numbers
                def subtract(num1, num2):
                    return num1 - num2

                # Function to multiply two numbers
                def multiply(num1, num2):
                    return num1 * num2

                # Function to divide two numbers
                def divide(num1, num2):
                    return num1 / num2

                print("Please select operation -\n" \
                        "1. Add\n" \
                        "2. Subtract\n" \
                        "3. Multiply\n" \
                        "4. Divide\n")


                # Take input from the user
                select = int(input("Select operations form 1, 2, 3, 4 :"))

                number_1 = int(input("Enter first number: "))
                number_2 = int(input("Enter second number: "))

                if select == 1:
                    print(number_1, "+", number_2, "=",
                                    add(number_1, number_2))

                elif select == 2:
                    print(number_1, "-", number_2, "=",
                                    subtract(number_1, number_2))

                elif select == 3:
                    print(number_1, "*", number_2, "=",
                                    multiply(number_1, number_2))

                elif select == 4:
                    print(number_1, "/", number_2, "=",
                                    divide(number_1, number_2))
                else:
                    print("Invalid input")


            
            elif "switch the window" in self.query:
                speak("Opening")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(10)
                pyautogui.keyUp("alt")

            elif "tell me the news" in self.query:
                speak("please wait sir, while fetching the news for you")
                news(self)

            # to find my location using IPaddress
            elif "where i am" in self.query or "where we are" in self.query:
                speak('wait sir, let me check')
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country}")
                except Exception as e:
                    speak("sorry sir,due to network issue i amnot able to find where we are.")
                    pass

            # to hide files and folder
            elif "hide all files" in self.query or "hide this folder" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takecommand().lower()
                if "hide" in self.condition:
                    os.system("attrib +h /s /d")
                    speak("sir, all files are now hidden")

                elif "visible" in self.condition:
                    os.system("attrib -h /s /d")
                    speak("sir,all the files are now visible")

                elif "leave it" in self.condition:
                    speak("ok sir")

            # how to do mode
            elif "activate how to do mode" in self.query:
                speak("how to do mode is activated")
                while True:
                    speak("please tell me what do you want to know")
                    how = self.takecommand()
                    try:
                        if "exit" in how or "close" in how:
                            speak("okay sir,how to do mode is deactivated")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)  # pip install pywikihow
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry, not able to find")

            # to know battery percentage
            elif "how much power " in self.query or "battery" in self.query:
                import psutil

                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")
                if percentage >= 75:
                    speak("we have enough power, no need to charge")
                elif percentage >= 40 and percentage <= 75:
                    speak("we should connect our system to the charging point")
                elif percentage >= 15 and percentage <= 30:
                    speak("we don't have enough power,please connect to the charger")
                elif percentage <= 15:
                    speak("we ahve very low power , please connect to the charger")

            # to play video and audio on yt
            elif "play songs on youtube" in self.query:
                try:
                    speak("tell me the song name")
                    name = self.takecommand()
                    kit.playonyt(name)
                except Exception as e:
                    speak("sorry sir i am unable to search")


            #web search
            if "open google" in self.query:
                speak("what should i search")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")
                speak("opening")

            if "hotels near me" in self.query:
                speak("Wait, I am searching")
                cm = "hotels near me"
                webbrowser.open(f"{cm}")
                speak("opening")
                
            
            elif "wikipedia" in self.query:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)


            # ip address
            elif "ip address" in self.query:
                from requests import get
                ip = get("https://api.ipify.org").text
                speak(f"your IP address is {ip}")

            # to download video

            elif 'video downloader' in self.query:
                root = Tk()
                root.geometry('500x300')
                root.resizable(0,0)
                root.title("Youtube Video Downloader")
                speak("Enter Video Url Here !")
                Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
                link = StringVar()
                Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
                Entry(root,width = 70,textvariable = link).place(x=32,y=90)

                def VideoDownloader():
                    url = YouTube(str(link.get()))
                    video = url.streams.first()
                    video.download()
                    Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

                Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

                root.mainloop()
                speak("Video Downloaded")

            elif 'close the tab' in self.query:
                keyboard.press_and_release('ctrl + w')
                
            elif 'open new tab' in self.query:
                keyboard.press_and_release('ctrl + t')

            elif 'open new window' in self.query:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in self.query: 
                keyboard.press_and_release('ctrl +h')

            elif 'home screen' in self.query:

                keyboard.press_and_release('windows + m')

            elif 'minimise the window' in self.query:

                keyboard.press_and_release('windows + m')

            elif 'show start' in self.query:

                keyboard.press('windows')

            elif 'open setting' in self.query:

                keyboard.press_and_release('windows + i')

            elif 'open search' in self.query:

                keyboard.press_and_release('windows + s')

            elif 'screen shot' in self.query:

                keyboard.press_and_release('windows + SHIFT + s')

            elif 'restore windows' in  self.query:

                keyboard.press_and_release('Windows + Shift + M')

            elif 'start the video' in self.query:
                keyboard.press('space bar')

            #website automation
            elif 'website' in self.query:
                speak("Ok Sir , Launching.....")
                query = query.replace("jerry","")
                query = query.replace("website","")
                query = query.replace(" ","")
                web1 = query.replace("open","")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                speak("Launched!")

            elif 'launch' in self.query:
                speak("Tell Me The Name Of The Website!")
                name = input("enter the website name: ")
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)
                speak("Done Sir!")

            # open apps
            elif 'open facebook' in self.query:
                OpenApps(self)

            elif 'open instagram' in self.query:
                OpenApps(self)

            elif 'open map' in self.query:
                OpenApps(self)

            elif 'open drive' in self.query:
                OpenApps(self)

            elif 'open code' in self.query:
                OpenApps(self)

            elif 'open youtube' in self.query:
                OpenApps(self)

            elif 'open browser' in self.query:
                OpenApps(self)


            elif "phone number info" in self.query:
                phon(self)

            #translator
            elif 'translator' in self.query:
                Tran(self)

            #temprature
            elif 'temperature' in self.query:
                Temp(self)

            #corona track
            elif 'coronavirus cases' in self.query:

                try:


                    from Marc import CoronaVirus

                    speak("Which Country's Information ?")

                    cccc = self.takecommand()

                    CoronaVirus(cccc)
            
                except:
                    speak("No Data")

            elif 'activate' in self.query:
                try:


                    while True:

                        # Python program to
                        # demonstrate creation of an
                        # assistant using wolf ram API

                        import wolframalpha

                        speak("Tell me what do you want to know")

                        # Taking input from user
                        question = self.takecommand()

                        if "deactivate" in question:

                            speak("Ok sir")
                            break

                        # App id obtained by the above steps
                        app_id = "-----" #give app_id

                        # Instance of wolf ram alpha
                        # client class
                        client = wolframalpha.Client(app_id)

                        # Stores the response from
                        # wolf ram alpha
                        res = client.query(question)

                        # Includes only text from the response
                        answer = next(res.results).text

                        print(answer)
                        speak(answer)
                
                except:
                    speak("I DON'T KNOW THE ANSWER")

            elif 'call' in self.query:
                openai(self)


startExecution = MainThread()  

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_6.clicked.connect(self.jokes)
        self.ui.pushButton_3.clicked.connect(self.Youtube)
        self.ui.pushButton_5.clicked.connect(self.Wht)
        self.ui.pushButton_4.clicked.connect(self.brow)
        self.ui.pushButton_7.clicked.connect(self.python)
        self.ui.pushButton_8.clicked.connect(self.loca)
        self.ui.pushButton_9.clicked.connect(self.opencod)
        self.ui.pushButton_10.clicked.connect(self.PowerP)
        self.ui.pushButton_13.clicked.connect(self.Ip)
        self.ui.pushButton_12.clicked.connect(self.Howto)
        self.ui.pushButton_11.clicked.connect(self.launch)
        self.ui.pushButton_14.clicked.connect(self.Search)
        self.ui.pushButton_shutdown.clicked.connect(self.Shut)
        self.ui.pushButton_restart.clicked.connect(self.res)
        self.ui.pushButton_sleep_2.clicked.connect(self.sleep)



    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        time = current_time.toString()
        date = current_date.toString()

        self.ui.dateEdit.setDate(current_date)
        self.ui.timeEdit.setTime(current_time)
        


    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\91930\\Downloads\\Wallpapers-Gifs-7.gif") #place your image path
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\91930\\Downloads\\Wallpapers-Gifs-7.gif") #place your image path
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\91930\\Downloads\\Jarvis_Loading_Screen.gif") #place your image path
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\91930\\Downloads\\giphy.gif") #place your image path
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        startExecution.start()


    def jokes(self):
        joke = pyjokes.get_joke()
        speak(joke)
    def Youtube(self):
        speak("opening")
        webbrowser.open("www.youtube.com")
    def Wht(self):
        speak("opening")
        webbrowser.open("web.whatsapp.com")
    def brow(self):
        speak("opening")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk") #place your path
    def python(self):
        speak("opening")
        os.startfile("C:\\Users\\91930\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Python 3.9 (64-bit).lnk")  #place your path
    def loca(self):
        speak('wait sir, let me check')
        try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country}")
        except Exception as e:
                    speak("sorry sir,due to network issue i amnot able to find where we are.")
                    pass
    def opencod(self):
        speak("opening")
        os.startfile("C:\\Users\\91930\\Desktop\\Marc.py")  #place your path
    def PowerP(self):
        speak("opening")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk")  #place your path
    def Ip(self):
        from requests import get
        ip = get("https://api.ipify.org").text
        speak(f"your IP address is {ip}")
    def Howto(self):
                speak("how to do mode is activated")
                while True:
                    speak("please tell me what do you want to know")
                    how = self.takecommand()
                    try:
                        if "exit" in how or "close" in how:
                            speak("okay sir,how to do mode is activated")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)  # pip install pywikihow
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry, not able to find")
    def launch(self):
                speak("Tell Me The Name Of The Website!")
                name = input("enter the website name: ")
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)
                speak("Done Sir!")
    def Search(self):
                speak("what should i search")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")
                speak("opening")
    def Shut(self):
                os.system("shutdown /s /t 10")
    def sleep(self):
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    def res(self):
                os.system("shutdown /r /t 10")

GuiApp = QApplication(sys.argv)
Jarvis_gui = Main()
Jarvis_gui.show()
(GuiApp.exec_())

        
        




    
