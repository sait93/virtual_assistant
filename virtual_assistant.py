import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5)
            print("Recognizing...")
            command = listener.recognize_google(voice)
            # print(command)
            command = command.lower()
            if "jarvis" in command:
                command = command.replace('jarvis', '')
            return command
    except:
        pass

def run_alexa():
    while True:
        command = take_command()
        print(command)
        if command == None:
            break
        if 'play' in command:
            song = command.replace('play', '').strip()
            talk('Playing ' + song)
            print(command)
            try:
                pywhatkit.playonyt(song)
            except Exception as e:
                print("An error occurred:", str(e))
                talk("Sorry, I couldn't play the requested song.")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            talk('Current time is ' + time)
        elif 'owner' in command:
            talk('Sai Teja')
        elif 'do you love me' in command:
            talk('Sorry, I have a boyfriend')
        elif 'who ' in command or 'what' in command or ' can you ' in command:
            person = command.replace('who is ', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            # webbrowser.get('chrome').open("https://www.youtube.com")

        elif 'are you single' in command:
            talk('I am in a relationship with WiFi')
        elif "joke" in command:
            talk(pyjokes.get_joke())
        elif 'exit' in command:
            talk('Goodbye!')
            break
        else:
            talk("Please say it again")

run_alexa()