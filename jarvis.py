import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import speech_recognition as sr
import os 
import random
import confi
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():#Wishes the user according to course of the day..
    hour=int(datetime.datetime.now().hour)#Accept the present hour clock
    if  hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis sir,plese tell me how may I help you")


def takeCommand():#It takes microphone input from the user and return string operation
    r=sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...") 
       r.pause_threshold=1# seconds of non-speaking audio before a phrase is considered complete
     
       audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')#Recognize the user voice
        print(f"user said: {query} \n")
    
    except Exception as e:#In case jarvis unable to listen to voice..
        
        print("say that again sir...")
        speak("say that again sir")
        
        return "None"
    return query
   
def sendEmail(to,content):
    
    server=smtplib.SMTP("smtp.gmail.com",587)#to create a server which will send email 
    server.ehlo()#Its helps to send mail via email
    server.starttls()# tls=TRANSFER LAYER SECURITY to make the server feel secure from sender
   
    server.login(confi.myem,confi.p)
    server.close()
    
    
        
        
if __name__=="__main__": 
    wishMe()
    while True:
        query=takeCommand().lower()
         
        #logic for executing a task based on  query
        
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        #play utube........>
        
        elif "open youtube" in query:
             webbrowser.open("youtube.com")
        
        #play goggle........>
        
        elif "open google" in query:
             webbrowser.open("google.com")
        
        #play spotify........>
        
        elif "open spotify" in query:
             webbrowser.open("open.spotify.com")
       
        #play music.........>
        
        elif "play music" in query:
             
             music_dir='C:\\Users\\HP\\Desktop\\Music'
             songs=os.listdir(music_dir)# gives the list of songs
             
             n=random.randint(0,106)
             os.startfile(os.path.join(music_dir,songs[n]))
        
        #Say time....> 
        
        elif "the time" in query:
             
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir the time is {strTime}")
        elif "shutdown" in query or "power of" in query:
             speak("are you sure you want to shutdown")
             res=takeCommand()
             if "yes" in res:
               speak("Sir,I am going to power off so take care")
               os.system('shutdown /s /t 1') # for shutdown
             else:
               speak("ok sir")
               
        elif "restart" in query:
             speak("are you sure you want to restart")
             res=takeCommand()
             if "yes" in res:
               speak("Sir,I am going to restart so plese wait")
               os.system('shutdown /r /t 1') # for restart
             else:
               speak("ok sir")
        #for opening dev C++
        
        elif "open dev" in query:
             devpath="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
             os.startfile(devpath)
        
        elif "send email" in query:
            try:
                speak("What should I Say?")
                content=takeCommand()
                to=confi.myem
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry")
             
             
            
            
      
               
                    
        
            
    
    