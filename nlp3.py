import speech_recognition as sr
import pyttsx3

def take_Command_Hindi():
    engine=pyttsx3.init('dummy')
    engine.runAndWait()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold=0.7
        audio=r.listen(source)
        try:
            print('Recognizing..')
            Query=r.recognize_google(audio,language='hi-ln') 
            print("the query is printed=",Query,"")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query
take_Command_Hindi()