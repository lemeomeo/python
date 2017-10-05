from Tkinter import * 
from tkFileDialog import *

def Function():
	print("placeholder")

#Open menu
def Open():
	filename = askopenfilename()
	infile = open(filename, 'r+')
	text.insert(1.0, infile.read())
	infile.close()

#Save menu
def SaveAs():
	filename = asksaveasfilename()
	outfile = open(filename, 'w')
	outfile.write(text.get(1.0, END))
	outfile.close()

#clear everything
def NewFile():
	text.delete(1.0, END)

def Undo():
	text.edit_undo()

def Redo():
	text.edit_redo()

root = Tk()
menu = Menu(root)
root.config(menu=menu)

#create File Menu
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=NewFile)
fileMenu.add_command(label="Open", command=Open)
fileMenu.add_command(label="Save", command=SaveAs)
fileMenu.add_command(label="Exit", command=quit)
#create Edit menu
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=Undo)
editMenu.add_command(label="Redo", command=Redo)

#height = number of line, width = number of chars.
#When create a widget, anything that is not included during creation
#will have to be modified using config().
text = Text(root, height = 30, width = 100, undo=True)
text.pack(side=LEFT, fill=Y)
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)
#attach text editor and scroll bar together: yscrollcommand and yview.
text.config(yscrollcommand=scroll.set)
text.config(background="#FFDDF1", font=("Comic Sans MS", 14))
scroll.config(command=text.yview)

root.mainloop()