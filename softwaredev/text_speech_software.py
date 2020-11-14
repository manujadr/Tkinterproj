import gtts
import os
from tkinter import *
import playsound
root = Tk()
root.geometry('350x300')
root.configure(bg = "sky blue")
root.title(" Manuja - Text to Speech ")
Label(root, text = "Text To Speech", font = "arial 15 bold", bg = "white smoke").pack(side = 'top')
# Label(text = " Developer: Manuja D R", font = "arial 15 bold", bg = 'white smoke', width = "30").pack(side = 'bottom')
Label(text = " By: Manuja D R", font = "arial 8 bold", fg = 'blue', bg = 'white smoke', width = "15").place(x=240, y=270)
Msg = StringVar()
Label(root, text = "Enter text here", font = 'arial 10 bold', bg ='white smoke').place(x=20,y=75)
entry_field = Entry(root, textvariable = Msg, width = '50')
entry_field.place(x=20,y=100)

def Text_to_speech():
	message = entry_field.get()
	# Speech = gtts.gTTS(text = message)
	# Speech.save('DataFlair.mp3')
	# playsound.playsound('DataFlair.mp3')
	language = 'en'
	try:
		myobj = gtts.gTTS(text=message,lang=language,slow=False)
	except AssertionError as e:
		print("No text to speak!!!, input should not be null.")
	else:
		myobj.save("speech_is.mp3")
		os.system("speech_is.mp3")
		print("Happy day...")
	finally:
		print(" Complete Execution is done !!!...")
	

	# ("morning_ringtone.mp3")


def Exit():
	root.destroy()

def Reset():
	Msg.set("")

Button(root, text = 'Play', font = 'arial 15 bold', bg = 'lawn green', command = Text_to_speech, width='4').place(x=25, y=140)
Button(root, text = 'Exit', font = 'arial 15 bold', bg = 'orange red2', command = Exit, width ='4').place(x=120, y = 140)
Button(root, text = 'Reset', font = 'arial 15 bold', bg = 'yellow', command = Reset, width='6').place(x=210,y=140)


root.mainloop()