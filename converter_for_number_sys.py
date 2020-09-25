from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

def con():
    n = e1.get()
    typ_i = e2.get()  
    typ_o = e3.get()
    if typ_i.lower() == 'binary':
        n = int(str(n),2)
        if typ_o.lower() == 'decimal':
            e4.delete(0,END)
            e4.insert(0,int(n)) 
        elif typ_o.lower() == 'octal':
            e4.delete(0,END)
            e4.insert(0,oct(int(n)))
        else:
            e4.delete(0,END)
            e4.insert(0,hex(int(n)))
    elif typ_i.lower() == 'decimal':
        if typ_o.lower() == 'binary':
            e4.delete(0,END)
            e4.insert(0,bin(int(n)))
        elif typ_o.lower() == 'octal':
            e4.delete(0,END)
            e4.insert(0,oct(int(n)))
        else:
            e4.delete(0,END)
            e4.insert(0,hex(int(n)))
    elif typ_i.lower() == 'octal':
        n = int(str(n),8)
        if typ_o.lower() == 'decimal':
            e4.delete(0,END)
            e4.insert(0,int(n))
        elif typ_o.lower() == 'binary':
            e4.delete(0,END)
            e4.insert(0,bin(int(n)))
        else:
            e4.delete(0,END)
            e4.insert(0,hex(int(n)))
    else:
        n = int(str(n),16)
        if typ_o.lower() == 'binary':
            e4.delete(0,END)
            e4.insert(0,bin(int(n)))
        elif typ_o.lower() == 'octal':
            e4.delete(0,END)
            e4.insert(0,oct(int(n)))
        elif typ_o.lower() == 'decimal':
            e4.delete(0,END)
            e4.insert(0,int(n))
        else:
            return


m = Tk()
m.title('NON-FRACTIONAL CONVERTER')
m.geometry("300x250")

messagebox.showinfo("Welcome!","This converter can convert among different numbers of bases in 2,4,8,16")
my_font = Font(m,family='Times New Roman',size=12)

l1 = Label(m,bg = '#0EEADD',text = 'ENTER NUMBER: ',font=my_font)
l2 = Label(m,bg = '#6519EA',text = 'Enter type u entered: ',font=my_font)
l3 = Label(m,bg = '#DB1135',text = 'what type you want: ',font=my_font)
l4 = Label(m,bg = '#52CB28',text = 'RESULT: ',font=my_font)

l1.place(relx = 0,rely = 0,relwidth = 0.5,relheight =0.25)
l2.place(relx = 0,rely = 0.2,relwidth = 0.5,relheight =0.25)
l3.place(relx = 0,rely = 0.4,relwidth = 0.5,relheight =0.25)
l4.place(relx = 0,rely = 0.6,relwidth = 0.5,relheight =0.25)

e1 = Entry(m,font=my_font)
e2 = Entry(m,font=my_font)
e3 = Entry(m,font=my_font)
e4 = Entry(m,font=my_font)

e1.place(relx = 0.5,rely = 0.0,relwidth = 0.5,relheight =0.25)
e2.place(relx = 0.5,rely = 0.20,relwidth = 0.5,relheight =0.25)
e3.place(relx = 0.5,rely = 0.40,relwidth = 0.5,relheight =0.25)
e4.place(relx = 0.5,rely = 0.6,relwidth = 0.5,relheight =0.25)



b = Button(m,text = 'EXECUTE :-)',command = con,bg = '#856A60',font=my_font)
b.place(relx = 0,rely = 0.8,relwidth = 1,relheight = 0.25)


m.mainloop()

