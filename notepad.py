""" This is a simple text editor created by  Rakesh Kumar as a project assignment during training."""

#---import required modules---
import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import tkinter.messagebox as msg
import tkinter.filedialog as fld

#---main class Application---
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.changes = [""]
        self.steps = int()
        self.file_name = None

# ---functions for File menu i.e. new, open, save, save as, exit
    def NewFile(self, event=None):
        if len(self.text.get('1.0', END + "-1c")) > 0:
            if msg.askyesno('Save', 'Do you want to save'):
                self.SaveAs()

            else:
                self.text.delete('1.0', END)

    def OpenFile(self):
        name = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                               title="Choose a file.")
        try:
            with open(name, 'r') as UseFile:
                contents = UseFile.read()
                self.text.insert(END, contents)
                UseFile.close()

        except:
            msg.showerror("Error", "Sorry, no file exists")

    def Save(self):
        name = asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str(self.text.get(0.0, END))
        name.write(text2save)

    def SaveAs(self):
        name = asksaveasfile(mode='w', defaultextension='.txt')
        t = str(self.text.get(0.0, END))
        try:
            name.write(t.rstrip())

        except:
            showerror("saveError", "try valid extension")

    def Exit(self):
        if askyesno('Verify', 'Do you really want to quit?'):
            root.destroy()

# function for about menu
    def About(self):
        msg.showinfo('About', 'this is a text-editor powered by AcadView \n developed by rakesh')

# function for help menu
    def Help(self):
        msg.showinfo("information", "for more help try google")

# functions for Edit menus i.e. undo, redo, cut, copy, paste, find, delete, select all

    def Undo(self, event=None):
        self.text.event_generate("<<Undo>>")
        return "break"

    def Redo(self, event=None):
        self.text.event_generate("<<Redo>>")
        return "break"

    def Cut(self, evt=None):
        self.text.event_generate("<<Cut>>")
        return "break"

    def Copy(self):
        self.text.event_generate("<<Copy>>")

    def Paste(self):
        self.text.event_generate("<<Paste>>")

    def Select_All(self, event=None):
        self.text.tag_add('sel', '1.0', 'end')
        return "break"

    def Find(self):
        findString = fld.askstring("Find...", "Enter Text")

    def Delete(self):
        pass

#---function for creating text area, scroll bar---

    def create_widgets(self):
        scrollbar = Scrollbar(root)
        self.text = Text(root, height=20, width=50)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, fill=Y)
        scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=scrollbar.set)
        self.text.configure(cursor='xterm')

        # --- it holds the images for shortcut icons

        new_file_icon = PhotoImage(file='C:/Users/Som Prakash Thakur\Desktop/icons/new_file.gif')
        open_file_icon = PhotoImage(file='C:/Users/Som Prakash Thakur/Desktop/icons/open_file.gif')
        save_file_icon = PhotoImage(file='C:/Users/Som Prakash Thakur/Desktop/icons/save.gif')
        cut_file_icon = PhotoImage(file='C:/Users/Som Prakash Thakur/Desktop/icons/cut.gif')
        copy_file_icon = PhotoImage(file='C:/Users/Som Prakash Thakur/Desktop/icons/copy.gif')
        paste_file_icon = PhotoImage(file='C:/Users/Som Prakash Thakur/Desktop/icons/paste.gif')
        undo_file_icon = PhotoImage(file='C:/Users/Som Prakash Thakur/Desktop/icons/undo.gif')
        redo_file_icon = PhotoImage(file='C:/Users/Som Prakash Thakur/Desktop/icons/redo.gif')
        about_file_icon = PhotoImage(file='C:/Users/Som Prakash Thakur/Desktop/icons/about.gif')
        find_file_icon = PhotoImage(file='C:/Users/Som Prakash Thakur/Desktop/icons/find_text.gif')

        #--- it creates the menus on menubar
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", compound='left', image=new_file_icon, command=self.NewFile, underline=0)
        filemenu.add_command(label="Open", command=self.OpenFile)
        filemenu.add_command(label="Save", command=self.Save)
        filemenu.add_command(label="Save as", command=SaveAs)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.Exit)

        editmenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Undo", command=self.Undo)
        editmenu.add_command(label="Redo", command=self.Redo)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.Cut)
        editmenu.add_command(label="Copy", command=self.Copy)
        editmenu.add_command(label="Paste", command=self.Paste)
        editmenu.add_command(label="Delete", command=self.Delete)
        editmenu.add_separator()
        editmenu.add_command(label="find", command=self.Find)
        editmenu.add_command(label="Select All", command=self.Select_All)

        menu.add_cascade(label="Help", command=self.Help)
        menu.add_cascade(label="About", command=self.About)

        shortcut_bar = Frame(root, height=25)
        shortcut_bar.pack(expand='no', fill='x')

        # code for displaying icons
        icons = ('about', 'open_file', 'save', 'cut', 'copy', 'paste', 'undo', 'redo', 'find_text', 'about')
        for i, icon in enumerate(icons):
            tool_bar_icon = PhotoImage(file='C:/Users/Som Prakash Thakur/Desktop/icons/{}.gif'.format(icon))
            cmd = eval(icon)
            tool_bar = Button(shortcut_bar, image=tool_bar_icon, command=cmd)
            tool_bar.image = tool_bar_icon
            tool_bar.pack(side='left')

#--- main root window and object for main class---
root = Tk(className="Text editor")
app = Application(root)
app.mainloop()
