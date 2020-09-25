
'''

importing concerned module
tkinter helps us to create user interactive apps and GUIs

'''

from tkinter import *
from tkinter import messagebox

m = Tk()  ##making our window
m.title('CALCULATOR')
messagebox.showinfo("Welcome!","This calculator evaluates binary expressions")
##in tkinter we first define the widget then place it in window

#entry is box where we enter our text
e = Entry(m,width = 50,borderwidth = 10)
e.grid(row = 0,column = 0,columnspan = 4,padx = 40,pady = 20)

##these functions guide buttons what to do

##this accept input in entry concatenates with previous string

def calc(number):
	current = e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

#for closing the window

def close():
	m.destroy()

#clears this entry box

def clear():
	e.delete(0,END)

##functions that perform operations

def equal():
	str1 = e.get()
	l = []
	for i in str1:
		l.append(i)
	#for taking first number
	a = ''
	#for taking second number
	b = ''

	for z in range(len(l)):
		if l[z] in ['1','2','3','4','5','6','7','8','9','0']:
			a+=l[z]
		else:
			break
	lr = []
	for y in range(len(l)-1,-1,-1):
		if l[y] in ['1','2','3','4','5','6','7','8','9','0']:
			lr.append(l[y])
		else :
			break


	for o in range(len(lr)-1,-1,-1):
		b+=lr[o]
	for op in l:
		if op in ['0','1','2','3','4','5','6','7','8','9']:
			pass
		else:
			if op == '+':
				e.delete(0,END)
				e.insert(0,int(a)+int(b))
			elif op == '-':
				e.delete(0,END)
				e.insert(0,int(a)-int(b))
			elif op == '/':
				e.delete(0,END)
				e.insert(0,int(a)/int(b))
			else:
				e.delete(0,END)
				e.insert(0,int(a)*int(b))

##defining numeric buttons

b1 = Button(m,text = '1' ,padx = 40,pady= 20,command =lambda: calc(1))
b2 = Button(m,text = '2' ,padx = 40,pady= 20,command =lambda: calc(2))
b3 = Button(m,text = '3' ,padx = 40,pady= 20,command =lambda: calc(3))
b4 = Button(m,text = '4' ,padx = 40,pady= 20,command =lambda: calc(4))
b5 = Button(m,text = '5' ,padx = 40,pady= 20,command =lambda: calc(5))
b6 = Button(m,text = '6' ,padx = 40,pady= 20,command =lambda: calc(6))
b7 = Button(m,text = '7' ,padx = 40,pady= 20,command =lambda: calc(7))
b8 = Button(m,text = '8' ,padx = 40,pady= 20,command =lambda: calc(8))
b9 = Button(m,text = '9' ,padx = 40,pady= 20,command =lambda: calc(9))
b0 = Button(m,text = '0' ,padx = 40,pady= 20,command =lambda: calc(0))

##other buttons

beq = Button(m,text = '=' ,padx = 30,pady= 15,command =equal)
bquit  = Button(m,text = 'PRESS TO QUIT ',padx = 30, pady = 15,
				command = close)
bclear = Button(m,text = 'C' ,padx = 39,pady= 15,command = clear)
badd = Button(m,text = '+' ,padx = 39,pady= 15,command = lambda: calc('+'))
bsub = Button(m,text = '-' ,padx = 39,pady= 15,command = lambda: calc('-'))
bdiv = Button(m,text = '/' ,padx = 39,pady= 15,command = lambda: calc('/'))
bmul = Button(m,text = '*' ,padx = 39,pady= 15,command = lambda: calc('*'))

#placing numeric butoons

b1.grid(row = 1,column = 0)
b2.grid(row = 1,column = 1)
b3.grid(row = 1,column = 2)
b4.grid(row = 1,column = 3)
b5.grid(row = 2,column = 0)
b6.grid(row = 2,column = 1)
b7.grid(row = 2,column = 2)
b8.grid(row = 2,column = 3)
b9.grid(row = 3,column = 0)
b0.grid(row = 3,column = 1)

#placing other buttons

bquit.grid(row = 5,column = 0,columnspan = 4)
beq.grid(row = 3,column = 2)
bclear.grid(row = 3,column = 3)
badd.grid(row = 4,column = 0)
bsub.grid(row = 4,column = 1)
bdiv.grid(row = 4,column = 2)
bmul.grid(row = 4,column = 3)



m.mainloop()
## the end