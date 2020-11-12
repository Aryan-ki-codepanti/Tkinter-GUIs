import itertools
from tkinter import *
from tkinter import font
from tkinter import messagebox

def generate_n_save():
	word = word_entry.get()
	filename = file_entry.get()

	if word.isspace() or not word:
		word_entry.insert(0,"Enter something here!")

	elif not filename or filename.isspace():
		file_entry.insert(0,"Enter some filename here!")

	else:
		if ".txt" not in filename:
			filename += ".txt"

		with open(filename,"w") as file:
			for passwd in itertools.permutations(word.strip(),len(word.strip())):
				passwd = "".join(passwd) + "\n"
				file.write(passwd)

		messagebox.showinfo("Hurray",f"Passwords have been saved to {filename}\nCheck your current working directory for the same")

root = Tk()
root.title("Password generator")
root.geometry("400x150")

my_font = font.Font(root,family = "Comic Sans MS",size = "15")
my_font2 = font.Font(root,family = "Comic Sans MS",size = "13")

word_label = Label(root,font = my_font,bg = "black",fg = "lime",text = "Enter word")
word_label.place(relx = 0,rely = 0,relwidth = 0.4,relheight = 1/3)
word_entry = Entry(root,font = my_font)
word_entry.place(relx = 0.4,rely = 0,relwidth = 0.6,relheight = 1/3)

file_label = Label(root,font = my_font2,bg = "black",fg = "lime",text = "Enter filename\nto save passwords")
file_label.place(relx = 0,rely = 1/3,relwidth = 0.45,relheight = 1/3)
file_entry = Entry(root,font = my_font2)
file_entry.place(relx = 0.45,rely = 1/3,relwidth = 0.55,relheight = 1/3)

save_button = Button(root,text = "Click me to save possible passwords to file",command = generate_n_save,
	bg = "black",fg = "white",font = my_font2)
save_button.place(relx = 0,rely = 2/3,relwidth = 1,relheight = 1/3)
root.mainloop()