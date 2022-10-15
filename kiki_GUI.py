from cProfile import run
from re import I
import tkinter
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3
import pytz
import datetime
import wikipedia
import pyaudio
import threading
#import pywhatkit
i=0
command=''
instruction_message_label=0
active_flag=0
deactivate_image=Image.open("Deactivate.png")
activate_image=Image.open("Activate.png")

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

sender = ['David']
messages = ["Hey bami, Whats up my graduation is next week i invited you to come to the ceremony."]

# speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# listen to command
def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # optional
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    
    global i
    talk('Hey Bami, you have recieved' + str(len(messages)) + 'message from' + str(sender[0]))
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
            i = 1
            pass
    elif 'remind' in command:
        talk('When?')
        print('Today  Tomorrow  Next week')
        command = take_command()
        print(command)
        if 'today' in command:
            talk('Okay I will remind you' + today)
            i = 1
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
        talk('The message from ' + str(sender[0]) + ' has deleted successfully')
        pass
    elif 'ignore' in command:
        i = 1
        pass
    else:
        talk('Say again please?')
        run_alexa()






main_window= tkinter.Tk()
main_window.geometry("370x750")
main_window.config(bg="white")
main_window.resizable(False,False)

def create_deactivate_button():
    def after_read():
        read_button.destroy()
    global active_flag
    active_flag=1
    global instruction_message_label
    instruction_message_label.destroy()
    global deactivate_image
    deactivate_image=Image.open("Deactivate.png")
    deactivate_image=deactivate_image.resize((70,80),Image.ANTIALIAS)
    deactivate_image=ImageTk.PhotoImage(deactivate_image)
    def widget_destroyer():
        if len(messages)==0:
            translate_button.destroy()
            time_button.destroy()
            date_button.destroy()
            weather_button.destroy()
            send_message_button.destroy()
        else:
            read_button.destroy()
            check_button.destroy()
            delete_button.destroy()
            ignore_button.destroy()
            block_button.destroy()
            Remind_me_button.destroy()

    deactivate_button=tkinter.Button(main_window,image=deactivate_image,
                                bg="white",border=0,activebackground="white",
                                command=lambda:[deactivate_button.destroy(),
                                        deactivate_label.destroy(),
                                        create_activate_button(),
                                        listening_label.destroy(),
                                        widget_destroyer()])
    deactivate_button.grid(row=5,column=0,padx=(47,0),pady=(120,0),
                            ipadx=0,ipady=0,sticky="W")
    deactivate_label=tkinter.Label(main_window,text="Deactivate",
                            font=("Poppins",16,"bold"),bg="white")
    deactivate_label.grid(row=6,column=0,padx=(32,0),
                            pady=(2,0),ipadx=0,ipady=0,sticky="w")

    if(len(messages)!=0):
        listening_label=tkinter.Label(main_window,text="Listening...",
                            font=("Poppins",17,"bold"),bg="white")
        listening_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
        button_frame=tkinter.Frame(main_window,border=0,bg="white")
        button_frame.grid(row=4,column=0,sticky="NEWS",ipadx=0,ipady=0,padx=(7,10))

        read_button=tkinter.Button(button_frame,text="Read",font=("Poppins",12,"bold"),
                            width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
        read_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)

        delete_button=tkinter.Button(button_frame,text="Delete",font=("Poppins",12,"bold"),
                            width=10,bg="#CDF5F6",border=0,activebackground="#CDF5F6")
        delete_button.grid(row=1,column=1,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)

        block_button=tkinter.Button(button_frame,text="Block",font=("Poppins",12,"bold"),
                            width=10,bg="#EFF9DA",border=0,activebackground="#EFF9DA")
        block_button.grid(row=1,column=2,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)

        Remind_me_button=tkinter.Button(button_frame,text="Remind Me",font=("Poppins",12,"bold"),
                            width=10,bg="#F9EBDF",border=0,activebackground="#F9EBDF")
        Remind_me_button.grid(row=2,column=0,padx=(10,10),pady=(20,0),ipadx=0,ipady=0)

        ignore_button=tkinter.Button(button_frame,text="Ignore",font=("Poppins",12,"bold"),
                            width=10,bg="#D6CDEA",border=0,activebackground="#D6CDEA")
        ignore_button.grid(row=2,column=1,padx=(0,10),pady=(20,0),ipadx=0,ipady=0)

        check_button=tkinter.Button(button_frame,text="Check",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
        check_button.grid(row=2,column=2,padx=(0,10),pady=(20,0),ipadx=0,ipady=0)
        if active_flag==1:
            start_time=threading.Timer(0.1,run_alexa)
            start_time.start()
    else:
        listening_label=tkinter.Label(main_window,text="Listening...",
                            font=("Poppins",17,"bold"),bg="white")
        listening_label.grid(row=3,column=0,padx=(32,0),pady=(35,0),sticky="W",
                            ipadx=0,ipady=0,columnspan=3)
        button_frame=tkinter.Frame(main_window,border=0,bg="white")
        button_frame.grid(row=4,column=0,sticky="NEWS",ipadx=0,ipady=0,padx=(7,10))

        translate_button=tkinter.Button(button_frame,text="Translate",font=("Poppins",12,"bold"),
                            width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
        translate_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)

        time_button=tkinter.Button(button_frame,text="Time",font=("Poppins",12,"bold"),
                            width=10,bg="#CDF5F6",border=0,activebackground="#CDF5F6")
        time_button.grid(row=1,column=1,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)

        date_button=tkinter.Button(button_frame,text="Date",font=("Poppins",12,"bold"),
                            width=10,bg="#EFF9DA",border=0,activebackground="#EFF9DA")
        date_button.grid(row=1,column=2,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)

        weather_button=tkinter.Button(button_frame,text="Weather",font=("Poppins",12,"bold"),
                            width=10,bg="#D6CDEA",border=0,activebackground="#D6CDEA")
        weather_button.grid(row=2,column=0,padx=(10,10),pady=(20,0),ipadx=0,ipady=0)

        send_message_button=tkinter.Button(button_frame,text="Send text",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
        send_message_button.grid(row=2,column=1,padx=(0,10),pady=(20,0),ipadx=0,ipady=0)


def create_activate_button():
    global active_flag
    active_flag=0
    global instruction_message_label
    instruction_message_label=tkinter.Label(main_window,text="Activate to check for new messages.",
                            font=("Poppins",13,"bold"),bg="white")
    instruction_message_label.grid(row=3,column=0,padx=32,pady=(20,0),sticky="W",ipadx=0,ipady=0)
    global activate_image
    activate_image=Image.open("Activate.png")
    activate_image=activate_image.resize((70,80),Image.ANTIALIAS)
    activate_image=ImageTk.PhotoImage(activate_image)
    activate_button=tkinter.Button(main_window,image=activate_image,bg="white",
                            border=0,activebackground="white",command=lambda:[activate_button.destroy(),
                            activate_label.destroy(),create_deactivate_button()])
    activate_button.grid(row=5,column=0,padx=(42,0),pady=(120,0),ipadx=0,ipady=0,sticky="WS")
    activate_label=tkinter.Label(main_window,text="Activate",font=("Poppins",16,"bold"),bg="white")
    activate_label.grid(row=6,column=0,padx=(32,0),pady=(2,0),ipadx=0,ipady=0,sticky="w")




avatar=Image.open("avatar.png")
resized_avatar=avatar.resize((80,80),Image.ANTIALIAS)
resized_avatar=ImageTk.PhotoImage(resized_avatar)
avatar_label= tkinter.Label(main_window,image=resized_avatar,bg="white")
avatar_label.grid(row=0,column=0, sticky="W",pady=(80,5),padx=32)

welcome_label=tkinter.Label(main_window,text="Welcome",font=("Poppins",15),bg="white")
welcome_label.grid(row=1,column=0,padx=32,sticky="W",ipadx=0,ipady=0)

user_name_label=tkinter.Label(main_window,text="Bemnet",font=("Poppins",20,"bold"),bg="white")
user_name_label.grid(row=2,column=0,padx=32,sticky="W",ipadx=0,ipady=0)


create_activate_button()
main_window.mainloop()
