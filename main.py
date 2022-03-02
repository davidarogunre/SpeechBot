import webbrowser
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import pywhatkit
import wikipedia
import time

recognizer = sr.Recognizer()
def say(command):
    engine = pyttsx3.init()
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',voice_id )
    engine.setProperty('rate', 170)
    engine.say(command)
    engine.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
    except sr.RequestError:
        print('Could not get text')
    
    except sr.UnknownValueError:
        print('Try again')
    return command

runner = True    
def task():
    try:
        command = get_command()
        if 'hello' in command:
            say('Hello David')
        elif 'hey' in command:
            say('Hello David')
        elif 'time' in command:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            say(current_time)
        elif 'google' in command:
            command = command.replace('google','')
            print('Open webpage...')
            time.sleep(2)
            pywhatkit.search(command)
        elif 'what is' in command:
            command = command.replace('what is','')
            print('Open webpage...')
            pywhatkit.search(command)
        elif 'who is' in command:
            command = command.replace('who is', '')
            answer = wikipedia.summary(command, 1)
            print(answer)
            say(answer)
        elif 'open' in command:
            command = command[command.index('open')+5:]
            webbrowser.open(f'https://{command}.com')
            pywhatkit.search(command)
    except:
        print('I didn\'t hear you')
while runner:
    task()