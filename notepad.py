import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import tkinter.messagebox as msg

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def NewFile(self):
        if len(self.text.get('1.0', END+"-1c"))>0:
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
         name=asksaveasfile(mode='w',defaultextension=".txt")
         text2save=str(self.text.get(0.0,END))
        # name=f
         name.write(text2save)


    def SaveAs(self):
        name=asksaveasfile(mode='w',defaultextension='.txt')
        t=str(self.text.get(0.0,END))
        try:
            name.write(t.rstrip())

        except:
            showerror("saveError","try valid extension")

    def About(self):
        msg.showinfo('About','this is a text-editor powered by AcadView \n developed by rakesh')

    def Help(self):
        msg.showinfo("information","for more help try google")

    def Exit(self):
        if askyesno('Verify', 'Do you really want to quit?'):
            root.destroy()

    def Undo(self):
        pass

    def Redo(self):
        pass

    def Cut(self):
        self.clipboard_clear()
        text = self.text.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def Copy(self):
        pass

    def Paste(self):
        pass

    def Find(self):
        pass

    def Delete(self):
        pass


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
        filemenu.add_command(label="Exit", command=self.Exit)

        editmenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Undo", command=self.Undo)
        editmenu.add_command(label="Redo", command=self.Redo)
        editmenu.add_separator()
        editmenu.add_command(label="cut", command=self.Cut)
        editmenu.add_command(label="copy", command=self.Copy)
        editmenu.add_command(label="paste", command=self.Paste)
        editmenu.add_command(label="delete", command=self.Delete)
        editmenu.add_separator()
        editmenu.add_command(label="find", command=self.Find)

        menu.add_cascade(label="Help", command=self.Help)
        menu.add_cascade(label="About", command=self.About)


root = Tk(className="Text editor")
app = Application(root)
app.mainloop()
