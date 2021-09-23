#Membuat microsoft word clone dengan menggunakan python dan package tkinter
#ini adalah private project dimana saya tidak bisa membuka miccrosoft word saya 
#jadi saya memilih untuk membuat nya sendiri
from tkinter import *
from tkinter import filedialog

def klikSave():
    file = filedialog.asksaveasfile(defaultextension=' .txt',
                                     filetypes=[
                                         ("Text file", ".txt"),
                                         ("HTML file", ".html"),
                                         ("Python file", ".py"),
                                         ("Word file", ".docx"),
                                     ])
    filetext = str(Wilayahmenulis.get(1.0,END))
    file.write(filetext)
    file.close()



word = Tk()
word.title("TamaDocument")

#Menubar Aplication
menubar = Menu(word)
word.config(menu=menubar)

filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As", command=klikSave)
filemenu.add_command(label="quit")

filemenu = Menu(menubar)
menubar.add_cascade(label="Edit")
#Menubar Aplication

#TextArea untuk menulis
Wilayahmenulis = Text(word)
Wilayahmenulis.pack()
#TextArea untuk menulis

word.mainloop()