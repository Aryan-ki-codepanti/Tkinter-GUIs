from tkinter import *
from random import *
import time
import tkinter.font as t
count = 10
m = Tk()
m.title("GUESS GAME")
m.geometry("400x400")

my_font_button = t.Font(m,family = "Comic Sans MS",size = 12)
guess_me = randint(10,99)
def gue(x):
	global guess_me
	global count
	if not e.get().isdigit():
		mes = "ENTER A \n VALID POSITIVE NUMBER" 
	else: 
		count-=x
		if count != 0: 
			n = int(e.get())

			if n == guess_me:
				mes = "CONGO YOU WON "
			elif n > guess_me:
				mes = "OHH YOU GUESS \n IS TOO HIGH"

			else:
				mes = "OHH YOUR GUESS \n IS TOO LOW"
		else:
			mes = "OUT OF TRIES,\n CORRECT ANS IS "+str(guess_me)

	lab = Label(c,text = mes,fg = "BLACK",bg = "AQUA",font = "verdana")
	#lab.grid_forget()
	
	lab.place(anchor = 'n',relx = 0.5,rely = 0.5,relwidth = 0.5,relheight = 0.2)

	tr = Label(c,text = "YOU HAVE "+str(count)+"\n tries left",fg = "BLACK",bg = "AQUA",font = "verdana")
	tr.place(anchor = 'n',relx = 0.5,rely = 0.7,relwidth = 0.5,relheight = 0.1)



HEIGHT = 500
WIDTH = 500
c = Canvas(m,height = HEIGHT,width =WIDTH,bg = 'BLACK')
c.pack()

e = Entry(c,width =40,font=my_font_button)
e.insert(0,"GUESS A 2 DIGIT NUMBER")
e.place(anchor = 'n',relx = 0.5,rely = 0,relwidth = 0.8,relheight = 0.1)

b = Button(c,bg = '#0099ff',fg = 'BLACK',text = "CLICK TO \n CHECK",command =lambda: gue(1),
	font=my_font_button)
b.place(anchor = 'n',relx = 0.2,rely = 0.2,relwidth = 0.3,relheight = 0.1)


bq  = Button(c,bg = 'lime',fg = 'black',text = "PRESS TO \n QUIT",command = m.quit,
	font=my_font_button)
bq.place(anchor = 'n',relx = 0.7,rely = 0.2,relwidth = 0.3,relheight = 0.1)

m.mainloop()