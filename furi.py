import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import pywhatkit as pwt


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def takeCommand():
    '''
    IT TAKE VOICE as input and return output 
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print('Say that again please...')
        speak("Sorry sir please say again")
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good after noon")
    else :
        speak("Good night")
    
    speak("I am furi How may I help you")
    
    
  
if __name__ == "__main__":
    
    wishMe()
    while True:
        query = takeCommand().lower()    

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query, sentences = 1)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("Youtube is opening sir")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("google is opening sir")
            webbrowser.open("google.com")

        elif "wish me" in query:
            wishMe()
        
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strTime}")
            
        elif "open code" in query:
            path = "C:\\Users\\ARUN SHARMA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("code is opening sir")
            os.startfile(path)
            
        # elif "Google search " in query:
        #     speak("what should I search")
        #     content = takeCommand()
        #     search(content , num=1)
        #     print(search)
            
        
        elif "quit" in query:
            speak("ok sir I am going to sleep")
            exit()
        
        elif "youtube search" in query:
            speak("What I have to search")
            content = takeCommand()
            pwt.playonyt(content)
            