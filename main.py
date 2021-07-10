'''Import All the stuff below'''

from tkinter import *
from PIL import ImageGrab
import numpy as np
import cv2
from datetime import datetime
import time
import pyautogui
import webbrowser
import emoji


'''Import All the stuff above'''


# Tk() class's instance below
app = Tk()
# Tk() class's instance above


#Virtual cursor

# X and Y coordinates of mouse pointer
Xs = [0,8,6,14,12,4,2,0]
Ys = [0,2,4,12,14,6,8,0]

#Virtual cursor


date_and_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# Getting screen size below
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
#getting screen size above

vid_name = f'Simple Recorder {date_and_time}.mp4'



def record():
	pop.destroy()

	# Vid Name
	date_and_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

	vid_name = f'Simple Recorder {date_and_time}.mp4'

	# Vid Name
	vid_writer = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
	


	if file_name.get() == '':
		vid_name = f'Simple Recorder {date_and_time}.mp4'

	else:
		vid_name = f'{file_name.get()} {date_and_time}.mp4'


	captured_vid = cv2.VideoWriter(vid_name, vid_writer, 24.0, (width, height))

	app.withdraw()
	while 1:
		img = ImageGrab.grab(bbox = (0, 0, width, height))
		img_np = np.array(img)
		img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

		# Synthesize mouse pointer
		mouseX,mouseY = pyautogui.position()
		Xthis = [2*x+mouseX for x in Xs]
		Ythis = [2*y+mouseY for y in Ys]

		points = list(zip(Xthis,Ythis))
		points = np.array(points, 'int32')

		cv2.fillPoly(img_final,[points],color=[200,200,200])
		img_small = cv2.resize(img_final,(960,540))
		cv2.imshow('Simple Recorder - Recording Window', img_small)
		
		cv2.namedWindow('Simple Recorder - Recording Window',cv2.WND_PROP_FULLSCREEN)
		cv2.setWindowProperty('Simple Recorder - Recording Window', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
		
		cv2.waitKey(10)
		captured_vid.write(img_final)


		if cv2.getWindowProperty('Simple Recorder - Recording Window', cv2.WND_PROP_VISIBLE) < 1:
			captured_vid.release()
			break


	app.deiconify()
# some frames you can tweek yourself

# 15.0, 28
# 30.0, 1 (Approx)
# 24.0, 10


''' Actual APP GUI '''

# GUI popup window
def coffee():
	webbrowser.open('https://www.buymeacoffee.com/vanshj')

def popup():
	global pop, var
	pop = Toplevel(app)
	pop.title('Simple Recorder')
	pop.geometry('400x200')
	pop.resizable(False, False)

	frame1=Frame(pop)
	frame1.pack(side='top')

	frame2=Frame(pop)
	frame2.pack(side='top',pady = 10)

	Label(frame1, text = 'To Stop Recording\nClose The Recording Window', font = ('Arial' ,15), foreground = '#303841').pack(side = 'top', pady = 10)

	vid_name = f'Simple Recorder {date_and_time}.mp4'

	mybutton = Button(frame1, text = 'Record', command = record)

	mybutton.pack(pady = 10)

	Label(frame2, text = 'Loving This?\nBuy Me A Coffee!!!', font = ('Arial' ,15), foreground = '#303841').grid(row = 1, column = 0, padx = 10)

	coffee_btn = Button(frame2, text = emoji.emojize('Buy :thumbs_up:'), command = coffee, font = ('Arial' ,13))
	coffee_btn.grid(row = 1, column = 2, padx = 10)




app.geometry('400x200')
app.resizable(False, False)
app.title('Simple Recorder')


frame1=Frame(app)
frame1.pack(side='top')

frame2=Frame(app)
frame2.pack(side='top', pady = 20)

frame3=Frame(app)
frame3.pack(side='top')


#Content & Logic

Label(frame1, text = 'Simple Recorder', font = ('Arial' ,25 , 'bold'), foreground = '#303841').pack(side = 'top')

Label(frame2, text = 'Name your recording : ', font = ('Arial' ,15), foreground = '#303841').grid(row = 1, column = 0)


file_name = Entry(frame2, width = 15, borderwidth = 2)
file_name.grid(row = 1, column = 1, ipady=3)


main_button = Button(frame3, text = 'Record', command = popup)
main_button.pack(side = 'top')
Label(frame3, text = "Date & Time will be the name if you don't name the file", font = ('Arial' ,10), foreground = '#303841').pack(pady = 20)





# The MAINLOOP!!!
app.mainloop()
