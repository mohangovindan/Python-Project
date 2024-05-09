from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from PIL import ImageTk, Image
import pyttsx3
import sys

engine = pyttsx3.init()

root = Tk()
root.state('zoomed')
#root.geometry('1200x1200')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title("Language Translator")


def clear():
    src_lang.set('choose input language')
    dest_lang.set('choose output language')
    Input_text.delete("1.0", "end-1c")
    Output_text.delete("1.0", "end-1c")
    

   
def cancel():
    root.destroy()
    

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

def speak(sentence):
    engine.say(sentence)
    engine.runAndWait()     

#Background

url = ImageTk.PhotoImage(Image.open(r"D:\desktop\63dce0d783953deb29b43e03_Artificial Intelligence Translation.png"))
p1 = Label(root, image = url,height=1000,width=3000)
p1.pack(fill="both")
    
    
#Label

Label(root, text = "LANGUAGE TRANSLATOR",fg='orange', font = "master 28 bold", bg='black').place(x=550,y=70)

#Label(root,text ="", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Label(root,text ="Enter Text",fg='black', font = 'arial 15 bold', bg ='orange').place(x=420,y=280)

Label(root,text ="Output",fg='black', font = 'arial 15 bold', bg ='orange').place(x=1350,y=280)

#Entry

Input_text = Text(root,font = 'master 15 bold',bg='white',fg='black', height = 10, wrap = WORD, padx=3, pady=2, width = 47)
Input_text.place(x=50,y = 320)

Output_text = Text(root,font = 'master 15 bold',bg='white',fg='black', height = 10, wrap = WORD, padx=3, pady= 2, width =46)
Output_text.place(x = 1000 , y = 330)

language = list(LANGUAGES.values())

#Combobox

src_lang = ttk.Combobox(root, values= language, width =25,font = 'arial 12 bold')
src_lang.place(x=80,y=270)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values= language, width =25,font = 'arial 12 bold')
dest_lang.place(x=1000,y=270)
dest_lang.set('choose output language')

#button
trans_btn = Button(root, text = 'Translate',font = 'arial 18 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')

trans_btn.place(x = 730, y= 450 )


trans_btn = Button(root,text='Quit',font=('calibri',20),command=cancel, bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x=830,y=650)

trans_btn = Button(root,text='Clear',font=('calibri',20),command=clear , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x=630,y=650)

b4 = Button(root, text="voice",font=('calibri',15), width=20,bg = 'royal blue1', activebackground = 'sky blue',command=lambda:speak(Output_text.get("1.0", "end-1c")))
b4.place(x=1150, y=650)



root.mainloop()


