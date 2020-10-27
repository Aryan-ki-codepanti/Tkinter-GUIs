import os
from tkinter import *
from tkinter import font
from tkinter import messagebox
import itertools

def renamer():

	path = entry.get()

	try:
		os.chdir(path)
		counter = itertools.count(start=1)

		keyword = keyword_entry.get()

		if not keyword:
			keyword = "file"
		for filename in os.listdir():
			f_name,f_ext = os.path.splitext(filename)
			new_name = f"{keyword}_{next(counter)}{f_ext}"
			os.rename(filename,new_name)

			

		messagebox.showinfo("WOAH","Rename Successful")
		

	except Exception as e:
		messagebox.showerror("OOPS",e)

#gui part
root = Tk()
root.title("Bulk File renamer")
root.geometry("500x100")
f = font.Font(root,family = "Comic Sans MS",size = 12)



label = Label(root,font=f,fg='black',bg='Dodger blue',text="Enter path to the folder (using /)")
label.place(relx=0,rely=0,relwidth=0.5,relheight=0.3)

entry = Entry(root,width=100,font=f)
entry.place(relx=0.5,rely=0,relwidth=0.5,relheight=0.3)

keyword_label = Label(root,font=f,fg='black',bg='Dodger blue',text="Enter prefix (for filename)")
keyword_label.place(relx=0,rely=0.3,relwidth=0.4,relheight=0.4)

keyword_entry = Entry(root,width=40,font=f)
keyword_entry.place(relx=0.4,rely=0.3,relwidth=0.6,relheight=0.4)

button = Button(root,font=f,bg='Dodger blue',fg='black',command=renamer,text="Press to rename all files in folder")
button.place(anchor='n',relx = 0.5,rely=0.7,relwidth=0.6,relheight=0.3)
root.mainloop()