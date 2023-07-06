
from tkinter import *
from tkinter import messagebox



def callback(selection):
    print(selection)


def Widgets():
    label = Label(win, text="Select language to translate", bg="#00ffff")
    label.pack()

    menu = StringVar()
    menu.set("Select Any Language")
    drop = OptionMenu(win, menu, "Arabic", "German", "Spanish", "French", "Hindi", "Korean", "Nepali", "Portuguese", "Dutch",
                      "Romanian", "Russian", "Tamil", "Telugu", "Thai", "Urdu", "Vietnamese", "Chinese",
                      command=abc)

    drop.pack()

def abc(language):
    if language=="German":
        lang="de"
    if language=="Spanish":
        lang="es"
    if language=="Arabic":
        lang="ar"
    if language=="French":
        lang="fr"
    if language=="Hindi":
        lang="hi"
    if language=="Korean":
        lang="ko"
    if language=="Nepali":
        lang="ne"
    if language=="Portuguese":
        lang="pt"
    if language=="Dutch":
        lang="nl"
    if language=="Romanian":
        lang="ro"
    if language=="Russian":
        lang="ru"
    if language=="Tamil":
        lang="ta"
    if language=="Telugu":
        lang="te"
    if language=="Thai":
        lang="th"
    if language=="Urdu":
        lang="ur"
    if language=="Vietnamese":
        lang="vi"
    if language=="Chinese":
        lang="zh-CN"
    import trans
    trans.con(lang)


win = Tk()

win.geometry("830x120")
win.title("Image to speech converter")
win.config(background="black")
sourceLocation = StringVar()

Widgets()

win.mainloop()




