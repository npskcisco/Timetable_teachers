import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()





def wishme():
    print("""

//////////////     //////////////
   -----              -----
    ()                 ()
              |
              |            ___________________
              |_          (                   )
                          ( Hi, I am SG 1210  ) 
       |______________|   <___________________)
                          

""")

    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour<12) :
        speak("Good Morning")

    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon ")
    else:
        speak("Good Evening ")

    speak("I am SG1210 . How  may I help you ")
    


def takeCommand() :

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(">>> Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try: 
        print(">>> Recognising...")
        query = r.recognize_google(audio, language = 'en-in')
        print(">>> You said : ", query , "\n")
    except Exception as e:
        print("Please say that again....")
        return ("none")
    return query


def searchifyes(tg):
    print(">>> I do not know how to respond to that")
    s = input("press enter to search online (type anything and press enter to continue talking)")
    if s != "" :
        pass
    else :
        su = 'www.google.com/search?q=' + tg
        speak("Checking on google")
        webbrowser.get('chrome %s').open(su)
        
if __name__ == "__main__":
    
    wishme()
   
    while(True):
        query = takeCommand().lower()


        #wikipedia search

        if'who' in query or 'wikipedia ' in query or 'wiki ' in query :
            speak(">>> Searching Wikipedia...")
            r = ""
            for i in query:
                r = r + i
                if('who is' in r or ' who ' in r or ' is ' in r or ' wikipedia ' in r or ' wiki ' in r or 'for' in r ):
                    r = " "
            query = r 
            try:
                results = wikipedia.summary(query, sentences = 2, auto_suggest = True, redirect = True)
                print(">>> according to Wikipedia , " + results)
                speak("according to Wikipedia , ")          
                speak(results)
            except Exception as e :
                print(">>> The personality is not famous enough to be on wikipedia. Checking on Google")
                speak("The personality is not famous enough to be on wikipedia. Checking on Google")

                
                sg = query
                for i in query:
                    sg = sg + i
                    if('search for' in sg or 'search ' in sg ):
                        sg = " "
                query = sg
                
                su = 'www.google.com/search?q=' + query
                webbrowser.get('chrome %s').open(su)

                continue


        elif'open youtube' in query or 'time for some videos' in query or 'best videos' in query :
            print(">>> opening")
            speak("opening youtube")
            webbrowser.get('chrome %s').open('youtube.com')
            continue

        elif'open google' in query or 'time to discover something' in query or 'knowledge ' in query :
            print(">>> opening")
            speak("opening google")
            webbrowser.get('chrome %s').open('google.com')
            continue

        
        elif'open stack' in query or 'fix this bug' in query or 'problems in code ' in query or 'open stackoverflow' in query :
            print(">>> opening")
            speak("opening stack overflow")
            webbrowser.get('chrome %s').open('stackoverflow.com')
            continue
     
        elif'open gmail' in query or 'check my mail' in query or 'check my email' in query or 'what messages do i have' in query :
            print(">>> opening")
            speak("opening gmail")
            webbrowser.get('chrome %s').open('gmail.com')
            continue

        elif'time'in query and 'now' in query :
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(">>> the time is :" + time)
            speak(time)
            continue

        elif'open code' in query or 'recent code' in query or 'time to code' in query or 'coding time' in query or 'open vs code' in query :
            codepath = "C:\\Users\\Shubham Goyal\\Desktop\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            print(">>> opening")
            speak("opening VS code")
            continue

        elif'open android' in query or 'android studio' in query or 'java app' in query or 'code in java' in query or 'recent java code' in query :
            codepath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(codepath)
            print(">>> opening") 
            speak("opening Android Studio")
            continue

        elif'open unity' in query or 'unity time' in query or 'game development' in query or 'make games' in query or 'recent game code' in query :
            codepath = "C:\\Program Files\\Unity\\Editor\\Unity.exe"
            os.startfile(codepath)
            print(">>> opening") 
            speak("opening Unity")
            continue

        elif'open fortnite' in query or 'game time' in query or 'fortnite time' in query or 'lets play' in query or "let's play" in query :
            codepath = "C:\\Users\\Shubham Goyal\\Desktop\\Fortnite.url"
            os.startfile(codepath)
            print(">>> opening") 
            speak("opening Fortnite")
            continue

        elif 'send email' in query:
            speak('Who is the recipient? ')
            recipe = takeCommand().lower()
            recipient = ""
            for i in recipe:
               
                if i == " ":
                    recipient = recipient
                else:
                    recipient = recipient + i
            print(">>>" + recipient)
            speak ('is the email id correct ?')
            tr = takeCommand() 
            if( 'yes' in tr or 'yeah' in tr or'ok' in tr):
                
                speak('What should I say ? ')
                text = takeCommand()
                speak("ok..")
                

                try: 
                    sendemail(recipient,text)
                    
                except Exception as e :
                    print(">>> Sorry, mail not sent for some reason")
                    speak("Sorry, mail not sent for some reason")

            else :
                speak("Oh ok...")
                pass

            



        elif query == "none":
            pass 

 
        #Sg1210 tasks
           
        elif 'you ' in query and 'can 'in query and 'do' in query and 'what ' in query  :
            print(">>> I can chat with you. I can help you open your most used applications. I can help you search about popular people, places or items from Wikipedia . I can even send mail, and open famous sites. Anything for you !")
            speak("I can chat with you. I can help you open your most used applications. I can help you search about popular people, places or items from Wikipedia . I can even send mail, and open famous sites . Anything for you !")
            continue


        
        #Exit conditions
        
        elif'bye' in query or 'thats all for today ' in query or 'thanks for your help' in query or 'gtg' in query or 'i have to go now ' in query or 'you are of great help ' in query  :
            print(">>> I hope you are satisfied with my service. Bye !" )    
            speak("I hope you are satisfied with my service. Bye !")
            print("""

//////////////     //////////////
   -----              -----
    ()                 ()
              |
              |            ______________________________
              |_          (                              )
                          ( May The Force Be with You !  ) 
       |______________|   <______________________________)
                          

""")
            speak("May the force be with you !!")
            break
        

        elif "search" in query:

            sg = ""
            for i in query:
                sg = sg + i
                if('h for' in sg or 'searc' in sg ):
                    sg = " "
            query = sg
            
            su = 'www.google.com/search?q=' + query
            speak("Checking on google")
            webbrowser.get('chrome %s').open(su)
            continue

        else :
            searchifyes(query)
            
  





                  
    



def sendemail(to, s):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sg1210bot@gmail.com", 'sg12abc123')
    server.sendmail('sg1210bot@gmail.com', to, s)
    server.close()
    speak('Email sent!')

    