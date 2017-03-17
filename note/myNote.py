__author__ = 'zyl'

from tkinter import*
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
import os


filename = ''

#Help
def aboutNotepad():
	messagebox.showinfo('About Notepad', '一页书')

def viewHelp():
	messagebox.showinfo('About Notepad', '百世经纶')

#File defaultextension='.txt', 
def openFile():
	global filename
	filename = filedialog.askopenfilename(filetypes=(("All files", "*.txt"),), title='open')
	root.title(os.path.basename(filename)+' - Notepad')
	fs = open(filename, 'r', encoding='utf-8')
	text.delete(1.0, END)
	text.insert(END, fs.read())
	fs.close()





def new():
	print(1)

root = Tk()
root.title('Notepad')
root.geometry('500x500+100+100')

#definition font
ft = font.Font(family = 'Fixdsys',size = 20,weight = 'bold')
font.families()

#create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', accelerator='Ctrl+N', command=new)
filemenu.add_command(label='Open', accelerator='Ctrl+O', command=openFile)
filemenu.add_command(label='Save', accelerator='Ctrl+S', command=new)
filemenu.add_command(label='Save as', accelerator='Ctrl+Shift+S', command=new)
filemenu.add_command(label='Exit', command=new)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Undo', accelerator='Ctrl+Z', command=new)
editmenu.add_command(label='Cut', accelerator='Ctrl+X', command=new)
editmenu.add_command(label='Copy', accelerator='Ctrl+C', command=new)
editmenu.add_command(label='Paste', accelerator='Ctrl+P', command=new)
editmenu.add_command(label='Delete', accelerator='Ctrl+Delete', command=new)
editmenu.add_command(label='Select All', accelerator='Ctrl+A', command=new)
editmenu.add_separator()
editmenu.add_command(label='Find..,', accelerator='Ctrl+N', command=new)
editmenu.add_command(label='Find Next', accelerator='Ctrl+N', command=new)

formatmenu = Menu(menu)
menu.add_cascade(label='Font', menu=formatmenu)
formatmenu.add_command(label='Font', command=new)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='View Help', command=viewHelp)
helpmenu.add_command(label='About Notepad', command=aboutNotepad)

#create a toolbar
toolbar = Frame(root, bg='light sea green')
b = Button(toolbar, text='new', width=6, command=new)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text='open', width=6, command=openFile)
b.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#create a status bars
class StatusBar(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.label = Label(master, text='ln20', bg='antique white', relief=RAISED, anchor=W)
		self.label.pack(fill=X)

	def set(self, format, *args):
		self.label.config(text=format % args)
		self.label.update_idletasks()

	def clear(self):
		self.label.config(text='')

status = StatusBar(root)
status.label.pack(side=BOTTOM, fill=X)

lnstatus = StatusBar(root)
lnstatus.label.pack(side=LEFT, fill=Y)
lnstatus.label.config(text='12')

#create a textedit
text = Text(root, undo=True)
text.pack(expand=YES, fill=BOTH)
text.config(font=ft)


#create a scrollbar
scrollbar = Scrollbar(text)
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)


root.mainloop()