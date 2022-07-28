import tkinter
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

#definindo coisas/resultado

def Jogandomoeda():
    result = np.random.binomial(1,0.5)
    tfield.delete("1.0", "end")

    if(result == 1):
        tfield = Text(root, width=52, height=5)
        tfield.insert(INSERT, "DEU CARAAAA!!!")
        i.config(image = Cara)
    else:
        tfield = Text(root, width=52, height=5)
        tfield.insert(INSERT, "DEU COROAAAA!!!")
        i.config(image = Coroa)

#cirando a janela

root = tkinter.Tk()
root.geometry("500x500")
root.title("coin flipper")

#carregando as imagens 

load = Image.open("C:\Users\APRENDER\Desktop\cara.jpg")
Cara = ImageTk.PhotoImage(load)

load = Image.open("C:\Users\APRENDER\Desktop\coroa.jpg")
Coroa = ImageTk.PhotoImage(load)

i = Label (root, image=Cara)
i.pack()

#botão

b1 = Button(root, text="Lançar moeda", font=("Arial", 10), command=Jogandomoeda, bg='teal', fg='white', activebackground="lightblue", padx=10, pady=10)
b1.pack()

#caixa de texto 

tfield = Text(root, width=52, height=5)
tfield.pack()
tfield.insert(INSERT, "Aperte o botão e aguarde o resultado :)")

# tfield.delete("1.0", "end")

root.mainloop

#^^^^^^^^ meu codigo 

#ambos n abrem a imagem, porem o meu não gera resultado

#\/\/\/\/\/\/ codigo copiado 

import numpy as np
from tkinter import *
from PIL import Image, ImageTk
 
 
def coinFlip():
    result = np.random.binomial(1,0.5)
    tfield.delete("1.0", "end")
 
    if(result == 1):
        tfield.insert(INSERT, " It's ————> HEADS")
        i.config(image = heads)
         
    else:
        tfield.insert(INSERT, " It's ————> TAILS")
        i.config(image = tails)
 
root = Tk()
root.title("Python Coin Flip")
 
#load heads image
load = Image.open("cara.jpg")
heads = ImageTk.PhotoImage(load)
 
#load tails image
load = Image.open("coroa.jpg")
tails = ImageTk.PhotoImage(load)
 
i = Label(root, image=heads)
i.pack()
 
root.geometry("500x500")
b1 = Button(root, text="Toss the Coin", font=("Arial", 10), command=coinFlip, bg='teal', fg='white', activebackground="lightblue", padx=10, pady=10)
b1.pack()
 
#Text Field for Result
tfield = Text(root, width=52, height=5)
tfield.pack()
tfield.insert(INSERT, "Click on the Button.. To Flip the Coin and get the result")

root.mainloop()