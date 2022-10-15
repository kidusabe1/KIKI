import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

i = 0
listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
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

def run_alexa():
    global i
    if i == 0:
        talk('Hey Bami, you have recieved' + str(len(messages)) + 'message from' + str(sender[0]))
        print('Read  Remind me  Check  Delete  Ignore')
        command = take_command()
        print(command)
        if 'read' in command:
            talk(str(messages[0]))
            i = 1
            print('Read Again  Delete  Next')
            command = take_command()
            print(command)
            if 'again' in command:
                talk(str(messages[0]))
                print('Delete  Next')
                command = take_command()
                print(command)
                if 'delete' in command:
                    talk('The message from ' + str(sender[0]) + ' has deleted')
                    sender.pop(0)
                    messages.pop(0)
                else:
                    pass
            elif 'delete' in command:
                talk('The message from ' + str(sender[0]) + ' has deleted')
                sender.pop(0)
                messages.pop(0)
            else:
                pass
        elif 'remind' in command:
            talk('When?')
            print('Today  Tomorrow  Next week')
            command = take_command()
            print(command)
            if 'today' in command:
                talk('Okay I will remind you today evening')
                pass
        elif 'check' in command:
            talk('It is positive, shall i read it?')
            print('Yes  No')
            command = take_command()
            print(command)
            if 'yes' in command:
                talk(str(messages[0]))
                print('Read Again  Delete  Next')
                command = take_command()
                print(command)
                if 'again' in command:
                    talk(str(messages[0]))
                    print('Delete  Next')
                    command = take_command()
                    print(command)
                    if 'delete' in command:
                        talk('The message from ' + str(sender[0]) + ' has deleted')
                        sender.pop(0)
                        messages.pop(0)
                        i = 1
                    else:
                        pass
                elif 'delete' in command:
                    talk('The message from ' + str(sender[0]) + ' has deleted')
                    sender.pop(0)
                    messages.pop(0)
                    i = 1
                else:
                    pass
            else:
                i = 1
                pass
        elif 'delete' in command:
            sender.pop(0)
            messages.pop(0)
            i = 1
            talk('The message from ' + str(sender[0]) + ' has deleted')
            pass
        elif 'ignore' in command:
            i = 1
            pass
        else:
            talk('Say again please?')
            run_alexa()
        
    else:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
            pass
        
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            
        elif 'date' in command: #calendar
            date = datetime.datetime.now().strftime('%B %d %Y')
            talk("Today's is " + date)
            
        elif 'search' in command: #who is / what is
            person = command.replace('search', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
            
        elif 'send' in command: #mail / whatsapp
            talk('For whom shall i send?')
            command = take_command()
            print(command)
            reciever = str(command)
            talk('Tell me what to send?')
            command = take_command()
            print(command)
            print('Sending message for ' + reciever)
            talk('Your message has sucessfully sent to ' + reciever)
            pass
        
        elif 'translate' in command:
            # to be done
            pass
        
        elif 'search' in command:
            # to be done
            pass
        
        elif 'news' in command:
            # to be done
            pass
            
        elif 'weather' in command:
            # to be done
            pass
        
        elif 'location' in command:
            # to be done
            pass
        
        elif 'to do list' in command: #task
            # to be done
            pass
        
        elif 'note' in command:
            # to be done
            pass
        
        elif 'launch' in command: #open
            # to be done
            pass
            
        elif 'bye' in command:
            i = 2
            pass
        
        else:
            talk('Say again please?')
while True:
    if i != 2:
        run_alexa()
    else:
        talk('Okay bye. see you again. take care.')
        break
        #exit()