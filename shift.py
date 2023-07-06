
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

import os

def CreateWidgets():
    link_Label = Label(root, text="Select The File To Copy : ",
                       bg="#E8D579")
    link_Label.grid(row=1, column=0,
                    pady=5, padx=5)

    root.sourceText = Entry(root, width=50,
                            textvariable=sourceLocation)
    root.sourceText.grid(row=1, column=1,
                         pady=5, padx=5,
                         columnspan=2)

    source_browseButton = Button(root, text="Browse",
                                 command=SourceBrowse, width=15)
    source_browseButton.grid(row=1, column=3,
                             pady=5, padx=5)



    copyButton = Button(root, text="Copy File",
                        command=CopyFile, width=15)
    copyButton.grid(row=3, column=1,
                    pady=5, padx=5)



def SourceBrowse():

    root.files_list = list(
        filedialog.askopenfilenames(initialdir="C:/Users/Hp"))

    root.sourceText.insert('1', root.files_list)


def CopyFile():


    files_list = root.files_list
    a=files_list[0]

    head, tail = os.path.split(a)
    l = -len(tail)
    b = a[:l] + r'\texttoconvert.png'
    os.rename(a, b)

    destination_location = r'C:\Users\Hp\PycharmProjects\textto speech 2'


    shutil.copy(b,destination_location)

    messagebox.showinfo("SUCCESSFUL")

root = tk.Tk()
root.geometry("830x120")
root.title("Copy-Move GUI")
root.config(background="black")
sourceLocation = StringVar()
destinationLocation = StringVar()

CreateWidgets()

root.mainloop()
