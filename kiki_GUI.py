#from cProfile import run
#from re import I
#from tabnanny import check
import tkinter
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3
import pytz
import datetime
import wikipedia
import pyaudio
import threading
import pywhatkit

# Creating The main window
main_window= tkinter.Tk()
main_window.geometry("450x900")
main_window.config(bg="white")
main_window.resizable(False,False)

#global variables
listen=0
i=0
j=0
command=''
instruction_message_label=0
active_flag=0
run_again_button=tkinter.Button()
button_frame=tkinter.Frame()
listening_label=tkinter.Label(text="")
command_label=tkinter.Label(text="")
activate_button=tkinter.Button()
activate_label=tkinter.Label()
deactivate_image=Image.open("Deactivate.png")
activate_image=Image.open("Activate.png")
result_image=Image.open("result.png")

#setting up the voice recognizer and storer
listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

sender = ['David']
#messages = ["Hey bami, Whats up, my graduation is next week I invite you to come to the ceremony."]
messages=[]
# speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# listen to command
def take_command():
    global listen
    global j
    global command
    global command_label
    command_label.destroy()
    try:
        with sr.Microphone() as source:
            global listening_label
            if(listen!=0):
                listening_label=tkinter.Label(main_window,text="Listening...",
                                font=("Poppins",17,"bold"),bg="white")
                listening_label.grid(row=3,column=0,
                                pady=(35,0),ipadx=0,padx=(32,0),ipady=0,sticky="W")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # optional
            if 'kiki' in command:
                command = command.replace('kiki', '')
                print(command)
    except:
        pass
    listen=1
    return command



def run_alexa():
    global run_again_button
    global button_frame
    global command_label
    global listening_label
    global i
    global instruction_message_label
    run_again_button.destroy()
    instruction_message_label.destroy()
    command_label.destroy()
    listening_label.destroy()
    i=1
    # Run_alex_2 is so that we avoid saying the same starting message again
    def run_alexa_2():
        global i
        global run_again_button
        global command_label
        command_label.destroy()
        run_again_button.destroy()
        command = take_command()
        ##############
        print(command)
        listening_label.destroy()
        command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
        command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)

        if 'read' in command:

            run_again_button=tkinter.Button(button_frame,text="Go back",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
            run_again_button.grid(row=3,column=0,padx=(0,10),pady=(30,10),ipadx=0,ipady=0)
        
            talk(str(messages[0]))
            i = 1
            #print('Read Again  Delete  Next')
            read_button.destroy()
            Remind_me_button.destroy()
            ignore_button.destroy()
            check_button.destroy()
            read_again_button=tkinter.Button(button_frame,text="Read again",font=("Poppins",12,"bold"),
                            width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
            read_again_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)
            
            command = take_command()
            ### How do you display the next print display
            print(command)
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text=command,
                        font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                        pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            
            if 'again' in command:
                talk(str(messages[0]))
                read_again_button.destroy()
                print('Delete  Next')
                command = take_command()
                print(command)
                listening_label.destroy()
                command_label=tkinter.Label(main_window,text=command,
                        font=("Poppins",17,"bold"),bg="white")
                command_label.grid(row=3,column=0,padx=(32,0),
                        pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
                if 'delete' in command:
                    delete_button.destroy()
                    talk('The message from ' + str(sender[0]) + ' has deleted')
                    sender.pop(0)
                    messages.pop(0)
                else:
                    talk('Say again please')
                    run_alexa_2()
                    i=1
                    pass
            elif 'delete' in command:
                #delete_button.destroy()
                talk('The message from ' + str(sender[0]) + ' has deleted')
                sender.pop(0)
                messages.pop(0)
                i=1
                run_alexa()
            elif 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            else:
                talk('Say again please.')
                run_alexa_2()
                i = 1
                pass


        elif 'remind' in command:
            run_again_button=tkinter.Button(button_frame,text="Go back",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
            run_again_button.grid(row=3,column=0,padx=(0,10),pady=(30,10),ipadx=0,ipady=0)
        
            today_button=tkinter.Button(button_frame,text="Today",font=("Poppins",12,"bold"),
                                width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
            today_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)

            Tomorrow_button=tkinter.Button(button_frame,text="Tomorrow",font=("Poppins",12,"bold"),
                                width=10,bg="#CDF5F6",border=0,activebackground="#CDF5F6")
            Tomorrow_button.grid(row=1,column=1,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)

            Next_Week_button=tkinter.Button(button_frame,text="Next Week",font=("Poppins",12,"bold"),
                                width=10,bg="#EFF9DA",border=0,activebackground="#EFF9DA")
            Next_Week_button.grid(row=1,column=2,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)

            check_button.destroy()
            Remind_me_button.destroy()
            ignore_button.destroy()
            talk('When?')

            print('Today  Tomorrow  Next week')
            command = take_command()
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text=command,
                    font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                    pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            print(command)
            if 'today' in command:
                talk('Okay I will remind you today')
                i = 1
                pass
            elif 'tomorrow' in command:
                talk('Okay, I will remind you tomorrow')
                i=1
                pass
            elif 'next' in command:
                talk('Okay, I will remind you next week')
                i=1
                pass
            elif 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            else:
                talk("I didn't get that, try again please.")
                run_alexa()
                pass
        elif 'search' in command: 
            button_frame.destroy()
            result_image=Image.open("result.png")
            result_image=result_image.resize((100,100),Image.ANTIALIAS)
            result_image=ImageTk.PhotoImage(result_image)
            result_button=tkinter.Button(main_window,image=result_image,bg="white",
                                    border=0,activebackground="white")
            result_button.grid(row=4,column=0,padx=(42,0),ipadx=0,ipady=0,pady=(15,0),sticky="NEWS")
            person = command.replace('search', '')
            info = wikipedia.summary(person, 1)
            print(info) #optional
            talk(info)
            command_label.destroy()
            talk("Do you want to go back?")
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
            pass
        elif 'check' in command:
            talk('It is positive, shall i read it?')
            Yes_button=tkinter.Button(button_frame,text="Yes",font=("Poppins",12,"bold"),
                                width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
            Yes_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)
        
            No_button=tkinter.Button(button_frame,text="No",font=("Poppins",12,"bold"),
                                width=10,bg="#CDF5F6",border=0,activebackground="#CDF5F6")
            No_button.grid(row=1,column=1,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)
            
            run_again_button=tkinter.Button(button_frame,text="Go back",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
            run_again_button.grid(row=3,column=0,padx=(0,10),pady=(30,10),ipadx=0,ipady=0)
        
            block_button.destroy()
            check_button.destroy()
            Remind_me_button.destroy()
            ignore_button.destroy()
            print('Yes  No')
            command = take_command()
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text=command,
                    font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                    pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            print(command)

            if 'yes' in command:
                talk(str(messages[0]))
                Read_again_button=tkinter.Button(button_frame,text="Read Again",font=("Poppins",12,"bold"),
                                    width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
                Read_again_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)
            
                delete_button=tkinter.Button(button_frame,text="Delete",font=("Poppins",12,"bold"),
                                    width=10,bg="#CDF5F6",border=0,activebackground="#CDF5F6")
                delete_button.grid(row=1,column=1,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)
                next_button=tkinter.Button(button_frame,text="Next",font=("Poppins",12,"bold"),
                                    width=10,bg="#EFF9DA",border=0,activebackground="#EFF9DA")
                next_button.grid(row=1,column=2,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)
                print('Read Again  Delete  Next')

                command = take_command()
                listening_label.destroy()
                command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
                command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
                print(command)
                if 'again' in command:
                    Yes_button.destroy()
                    No_button.destroy()
                    Read_again_button.destroy()
                    talk(str(messages[0]))
                    print('Delete  Next')
                    command = take_command()
                    listening_label.destroy()
                    command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
                    command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
                    print(command)
                    if 'delete' in command:
                        delete_button.destroy()
                        talk('The message from ' + str(sender[0]) + ' has deleted')
                        sender.pop(0)
                        messages.pop(0)
                        i = 1
                    else:
                        talk('Say again please')
                        run_alexa_2()
                elif 'delete' in command:
                    Yes_button.destroy()
                    No_button.destroy()
                    Read_again_button.destroy()
                    delete_button.destroy()
                    talk('The message from ' + str(sender[0]) + ' has deleted')
                    sender.pop(0)
                    messages.pop(0)
                    i = 1
                else:
                    talk('Say again please')
                    run_alexa_2()
            elif 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            elif 'no' in command:
                i = 1
                pass
            else:
                talk('Say again please')
                run_alexa_2()
        elif 'delete' in command:
            run_again_button=tkinter.Button(button_frame,text="Go back",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
            run_again_button.grid(row=3,column=0,padx=(0,10),pady=(30,10),ipadx=0,ipady=0)
        
            read_button.destroy()
            delete_button.destroy()
            #block_button.destroy()
            ignore_button.destroy()
            Remind_me_button.destroy()
            check_button.destroy()
            sender.pop(0)
            messages.pop(0)
            i = 1
            talk('The message from ' + str(sender[0]) + ' has deleted successfully')
            talk("Do you want to go back?")
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            pass
##
## next is to add the run again if block everywhere
##
        elif 'ignore' in command:
            i = 1
            pass
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            talk("Do you want to go back?")
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            pass
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
            pass
        elif 'date' in command: #calendar
            date = datetime.datetime.now().strftime('%B %d %Y')
            talk("Today's is " + date)
            talk("Do you want to go back?")
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            pass
        elif 'send' in command: #mail / whatsapp
            talk('For whom shall i send?')
            command = take_command()
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            print(command)
            reciever = str(command)
            talk('Tell me what to send?')
            command = take_command()
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            print(command)
            print('Sending message for ' + reciever)
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text='Sending message for ' + reciever,
                            font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            talk('Your message has sucessfully sent to ' + reciever)
            talk("Do you want to go back?")
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            pass
        elif 'bye' in command:
            talk('Okay bye. see you again. take care.')
            main_window.destroy()
            i = 2
            pass
        elif 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
        else:
            talk('Say Again please.')
            run_alexa_2()
        j==0
    instruction_message_label.destroy()
    
    if(len(messages)!=0):
        talk('Hey Bami, you have recieved' + str(len(messages)) + 'message from' + str(sender[0]))
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

        deactivate_button=tkinter.Button(main_window,image=deactivate_image,
                                    bg="white",border=0,activebackground="white",
                                    command=main_window.destroy)
        deactivate_button.grid(row=5,column=0,padx=(47,0),pady=(120,0),
                                ipadx=0,ipady=0,sticky="W")
        deactivate_label=tkinter.Label(main_window,text="Deactivate",
                                font=("Poppins",16,"bold"),bg="white")
        deactivate_label.grid(row=6,column=0,padx=(32,0),
                                pady=(2,0),ipadx=0,ipady=0,sticky="w")
        ##############
        #if(j!=5):
        command = take_command()
        ##############
        print(command)
        listening_label.destroy()
        command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
        command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)

        if 'read' in command:

            run_again_button=tkinter.Button(button_frame,text="Go back",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
            run_again_button.grid(row=3,column=0,padx=(0,10),pady=(30,10),ipadx=0,ipady=0)
        
            talk(str(messages[0]))
            i = 1
            #print('Read Again  Delete  Next')
            read_button.destroy()
            Remind_me_button.destroy()
            ignore_button.destroy()
            check_button.destroy()
            read_again_button=tkinter.Button(button_frame,text="Read again",font=("Poppins",12,"bold"),
                            width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
            read_again_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)
            
            command = take_command()
            ### How do you display the next print display
            print(command)
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text=command,
                        font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                        pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            
            if 'again' in command:
                talk(str(messages[0]))
                read_again_button.destroy()
                print('Delete  Next')
                command = take_command()
                print(command)
                listening_label.destroy()
                command_label=tkinter.Label(main_window,text=command,
                        font=("Poppins",17,"bold"),bg="white")
                command_label.grid(row=3,column=0,padx=(32,0),
                        pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
                if 'delete' in command:
                    delete_button.destroy()
                    talk('The message from ' + str(sender[0]) + ' has deleted')
                    sender.pop(0)
                    messages.pop(0)
                    talk("Do you want to go back?")
                    command=take_command()
                    if 'yes' or 'go' or 'back' in command:
                        run_alexa()
                        pass
                else:
                    talk('Say again please')
                    run_alexa_2()
                    i=1
                    pass
            elif 'delete' in command:
                delete_button.destroy()
                talk('The message from ' + str(sender[0]) + ' has deleted')
                sender.pop(0)
                messages.pop(0)
                talk("Do you want to go back?")
                command=take_command()
                if 'yes' or 'go' or 'back' in command:
                    run_alexa()
                    pass
            else:
                talk('Say again please.')
                run_alexa_2()
                i = 1
                pass


        elif 'remind' in command:
            run_again_button=tkinter.Button(button_frame,text="Go back",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
            run_again_button.grid(row=3,column=0,padx=(0,10),pady=(30,10),ipadx=0,ipady=0)
        
            today_button=tkinter.Button(button_frame,text="Today",font=("Poppins",12,"bold"),
                                width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
            today_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)

            Tomorrow_button=tkinter.Button(button_frame,text="Tomorrow",font=("Poppins",12,"bold"),
                                width=10,bg="#CDF5F6",border=0,activebackground="#CDF5F6")
            Tomorrow_button.grid(row=1,column=1,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)

            Next_Week_button=tkinter.Button(button_frame,text="Next Week",font=("Poppins",12,"bold"),
                                width=10,bg="#EFF9DA",border=0,activebackground="#EFF9DA")
            Next_Week_button.grid(row=1,column=2,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)

            check_button.destroy()
            Remind_me_button.destroy()
            ignore_button.destroy()
            talk('When?')

            print('Today  Tomorrow  Next week')
            command = take_command()
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text=command,
                    font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                    pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            print(command)
            if 'today' in command:
                talk('Okay I will remind you today')
                i = 1
                pass
            elif 'tomorrow' in command:
                talk('Okay, I will remind you tomorrow')
                i=1
                pass
            elif 'next' in command:
                talk('Okay, I will remind you next week')
                i=1
                pass
            else:
                talk("I didn't get that, try again please.")
                run_alexa()
                pass
            talk("Do you want to go back?")
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
        elif 'search' in command: #who is / what is
            #global result_image
            #run_again_button=tkinter.Button(main_window,text="Go back",font=("Poppins",12,"bold"),
            #                width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
            #run_again_button.grid(row=5,column=0,padx=(0,10),pady=(30,10),ipadx=0,ipady=0)
            button_frame.destroy()
            result_image=Image.open("result.png")
            result_image=result_image.resize((100,100),Image.ANTIALIAS)
            result_image=ImageTk.PhotoImage(result_image)
            result_button=tkinter.Button(main_window,image=result_image,bg="white",
                                    border=0,activebackground="white")
            result_button.grid(row=4,column=0,ipadx=0,ipady=0,pady=(15,0),sticky="NEWS")
            person = command.replace('search', '')
            person=command.replace('who','')
            person=command.replace('what','')
            #activate_label=tkinter.Label(main_window,text=person,font=("Poppins",16,"bold"),bg="white")
            #activate_label.grid(row=5,column=0,padx=(32,0),ipadx=0,ipady=0,sticky="w")
            info = wikipedia.summary(person, 1)
            print(info) #optional
            talk(info)
            command_label.destroy()
            talk("Do you want to go back?")
            result_button.destroy()
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
            pass
        elif 'check' in command:
            talk('It is positive, shall i read it?')
            Yes_button=tkinter.Button(button_frame,text="Yes",font=("Poppins",12,"bold"),
                                width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
            Yes_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)
        
            No_button=tkinter.Button(button_frame,text="No",font=("Poppins",12,"bold"),
                                width=10,bg="#CDF5F6",border=0,activebackground="#CDF5F6")
            No_button.grid(row=1,column=1,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)
            
            run_again_button=tkinter.Button(button_frame,text="Go back",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
            run_again_button.grid(row=3,column=0,padx=(0,10),pady=(30,10),ipadx=0,ipady=0)
        
            block_button.destroy()
            check_button.destroy()
            Remind_me_button.destroy()
            ignore_button.destroy()
            print('Yes  No')
            command = take_command()
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text=command,
                    font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                    pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            print(command)

            if 'yes' in command:
                talk(str(messages[0]))
                Read_again_button=tkinter.Button(button_frame,text="Read Again",font=("Poppins",12,"bold"),
                                    width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
                Read_again_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)
            
                delete_button=tkinter.Button(button_frame,text="Delete",font=("Poppins",12,"bold"),
                                    width=10,bg="#CDF5F6",border=0,activebackground="#CDF5F6")
                delete_button.grid(row=1,column=1,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)
                next_button=tkinter.Button(button_frame,text="Next",font=("Poppins",12,"bold"),
                                    width=10,bg="#EFF9DA",border=0,activebackground="#EFF9DA")
                next_button.grid(row=1,column=2,padx=(0,10),pady=(35,0),ipadx=0,ipady=0)
                print('Read Again  Delete  Next')

                command = take_command()
                listening_label.destroy()
                command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
                command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
                print(command)
                if 'again' in command:
                    Yes_button.destroy()
                    No_button.destroy()
                    Read_again_button.destroy()
                    talk(str(messages[0]))
                    print('Delete  Next')
                    command = take_command()
                    listening_label.destroy()
                    command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
                    command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
                    print(command)
                    if 'delete' in command:
                        delete_button.destroy()
                        talk('The message from ' + str(sender[0]) + ' has deleted')
                        sender.pop(0)
                        messages.pop(0)
                        i = 1
                        talk("Do you want to go back?")
                        command=take_command()
                        if 'yes' or 'go' or 'back' in command:
                            run_alexa()
                            pass
                    else:
                        talk('Say again please')
                        run_alexa_2()
                elif 'delete' in command:
                    Yes_button.destroy()
                    No_button.destroy()
                    Read_again_button.destroy()
                    delete_button.destroy()
                    talk('The message from ' + str(sender[0]) + ' has deleted')
                    sender.pop(0)
                    messages.pop(0)
                    i = 1
                    talk("Do you want to go back?")
                    command=take_command()
                    if 'yes' or 'go' or 'back' in command:
                        run_alexa()
                        pass
                else:
                    talk('Say again please')
                    run_alexa_2()
            elif 'no' in command:
                i = 1
                pass
                talk("Do you want to go back?")
                command=take_command()
                if 'yes' or 'go' or 'back' in command:
                    run_alexa()
                    pass
            else:
                #talk('Say again please')
                #run_alexa_2()
                talk("I didn't get that, try again please.")
                run_alexa()
        elif 'delete' in command:
            run_again_button=tkinter.Button(button_frame,text="Go back",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
            run_again_button.grid(row=3,column=0,padx=(0,10),pady=(30,10),ipadx=0,ipady=0)
        
            read_button.destroy()
            delete_button.destroy()
            #block_button.destroy()
            ignore_button.destroy()
            Remind_me_button.destroy()
            check_button.destroy()
            talk('The message from ' + str(sender[0]) + ' has deleted successfully')
            sender.pop(0)
            messages.pop(0)
            i = 1
            talk("Do you want to go back?")
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            pass
        elif 'ignore' in command:
            i = 1
            pass
        elif 'bye' in command:
            talk('Okay bye. see you again. take care.')
            main_window.destroy()
            i = 2
            pass
        else:
            talk('Say again please?')
            run_alexa_2()
    else:
        talk("How may I assist you bami?")
        i=2
        button_frame=tkinter.Frame(main_window,border=0,bg="white")
        button_frame.grid(row=4,column=0,sticky="NEWS",ipadx=0,ipady=0,padx=(7,10))

        search_button=tkinter.Button(button_frame,text="Search",font=("Poppins",12,"bold"),
                            width=10,bg="#CBE4F9",border=0,activebackground="#CBE4F9")
        search_button.grid(row=1,column=0,padx=(10,10),pady=(35,0),ipadx=0,ipady=0)

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
        
        play_button=tkinter.Button(button_frame,text="Play Music",font=("Poppins",12,"bold"),
                            width=10,bg="#F9D8D6",border=0,activebackground="#F9D8D6")
        play_button.grid(row=2,column=2,padx=(0,10),pady=(20,0),ipadx=0,ipady=0)
        
        
        deactivate_button=tkinter.Button(main_window,image=deactivate_image,
                                    bg="white",border=0,activebackground="white",
                                    command=main_window.destroy)
        deactivate_button.grid(row=5,column=0,padx=(47,0),pady=(120,0),
                                ipadx=0,ipady=0,sticky="W")
        deactivate_label=tkinter.Label(main_window,text="Deactivate",
                                font=("Poppins",16,"bold"),bg="white")
        deactivate_label.grid(row=6,column=0,padx=(32,0),
                                pady=(2,0),ipadx=0,ipady=0,sticky="w")
        command = take_command()
        print(command)

        listening_label.destroy()
        command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
        command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            talk("Do you want to go back?")
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            pass
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
            pass
        elif 'date' in command: #calendar
            date = datetime.datetime.now().strftime('%B %d %Y')
            talk("Today's is " + date)
            talk("Do you want to go back?")
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            pass
        elif 'send' in command: #mail / whatsapp
            talk('For whom shall i send?')
            command = take_command()
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            print(command)
            reciever = str(command)
            talk('Tell me what to send?')
            command = take_command()
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text=command,
                            font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            print(command)
            print('Sending message for ' + reciever)
            listening_label.destroy()
            command_label=tkinter.Label(main_window,text='Sending message for ' + reciever,
                            font=("Poppins",17,"bold"),bg="white")
            command_label.grid(row=3,column=0,padx=(32,0),
                            pady=(35,0),sticky="W",ipadx=0,ipady=0,columnspan=3)
            talk('Your message has sucessfully sent to ' + reciever)
            talk("Do you want to go back?")
            command=take_command()
            if 'yes' or 'go' or 'back' in command:
                run_alexa()
                pass
            pass
        elif 'bye' in command:
            talk('Okay bye. see you again. take care.')
            main_window.destroy()
            i = 2
            pass
        else:
            talk('Say Again please.')
            run_alexa_2()
    j==0

def create_deactivate_button():
    global listen
    global active_flag
    active_flag=1
    global deactivate_image
    global instruction_message_label
    instruction_message_label.destroy()
    deactivate_image=Image.open("Deactivate.png")
    deactivate_image=deactivate_image.resize((70,80),Image.ANTIALIAS)
    deactivate_image=ImageTk.PhotoImage(deactivate_image)
    if(len(messages)!=0):
        if active_flag==1:
            start_time=threading.Timer(0.1,run_alexa)
            start_time.start()
    else:
        if active_flag==1:
            start_time=threading.Timer(0.1,run_alexa)
            start_time.start()
    listen+=1

def create_activate_button():    
    global active_flag
    active_flag=0
    global instruction_message_label
    
    instruction_message_label=tkinter.Label(main_window,text="Activate or say 'Hey kiki'...",
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

