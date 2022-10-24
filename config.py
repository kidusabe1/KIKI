#global variables
import tkinter
from PIL import ImageTk, Image
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
