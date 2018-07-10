import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def NewFile(self):
        print("New File")

    def OpenFile(self):
        name = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                               title="Choose a file.")
        try:
            with open(name, 'r') as UseFile:
                contents = UseFile.read()
                self.text.insert(END, contents)
                UseFile.close()

        except:
            showerror("Error", "Sorry, no file exists")

    def Save(self):
        print("save file in folder")

    def SaveAs(self):
        print("Save the file as you want")

    def About(self):
        msg = "This is a special text editor"
        about = Message(root, text=msg)

    def Help(self):
        print("for help visit youtube")

    def callback(self):
        if askyesno('Verify', 'Do you really want to quit?'):
            root.destroy()

    def create_widgets(self):
        scrollbar = Scrollbar(root)
        self.text = Text(root, height=20, width=50)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, fill=Y)
        scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=scrollbar.set)
        self.text.configure(cursor='xterm')

        menu = Menu(root)
        root.config(menu=menu)

        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.NewFile)
        filemenu.add_command(label="Open", command=self.OpenFile)
        filemenu.add_command(label="Save", command=self.Save)
        filemenu.add_command(label="Save as", command=SaveAs)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.callback)

        editmenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Undo")
        editmenu.add_command(label="Redo")
        editmenu.add_separator()
        editmenu.add_command(label="cut")
        editmenu.add_command(label="copy")
        editmenu.add_command(label="paste")
        editmenu.add_command(label="delete")
        editmenu.add_separator()
        editmenu.add_command(label="find")

        menu.add_cascade(label="Help", command=self.Help)
        menu.add_cascade(label="About", command=self.About)


root = Tk(className="Text editor")
app = Application(root)
app.mainloop()
