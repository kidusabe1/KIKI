import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

sender = ['David']
messages = ["Hey bami, Whats up my graduation is next week i invited you to come to the ceremony."]



def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

i = 0
def run_alexa():
    global i
    if i == 0:
        talk('Hey Bami, you have recieved' + str(len(messages)) + 'message from' + str(sender[0]))
        i = 1
        command = take_command()
        print(command)
        if 'read' in command:
            talk(str(messages[0]))
            sender.pop(0)
            messages.pop(0)
        elif 'delete' in command:
            sender.pop(0)
            messages.pop(0)
            talk('The message from ' + str(sender[0]) + ' has deleted')
        else:
            talk('Say again please?')
    else:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%B %d %Y')
            talk("Today's is " + date)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        else:
            talk('Say again please?')

while True:
    run_alexa()