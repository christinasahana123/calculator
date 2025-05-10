import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')

if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # Corrected from 'voices' to 'voice'
else:
    engine.setProperty('voice', voices[0].id)  # Corrected from 'voices' to 'voice'

def engine_talk(text):
    print(f"Alexa is saying: {text}")
    engine.say(text)
    engine.runAndWait()

def user_commands():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Start speaking!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  # Corrected spelling of 'recognize_google'
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(f"User said: {command}")
                return command
    except Exception as e:
        print(f"Error: {e}")
    return ""

def run_alexa():
    command = user_commands()
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            engine_talk('Playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')  # Corrected strftime format
            engine_talk('The current time is ' + time)
        elif 'who is' in command:  # Corrected 'who ia' to 'who is'
            name = command.replace('who is', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)
        elif 'joke' in command:
            engine_talk(pyjokes.get_joke())
        elif 'stop' in command:  # Corrected ' stop' to 'stop'
            sys.exit()
        else:
            engine_talk('I could not hear you properly')
    

if __name__ == "__main__":
    run_alexa()  # Corrected missing colon and removed infinite loop