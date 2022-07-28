
import tkinter
import random, string
import pyperclip

#criar uma aba 

#configurar o gerador 

#configurar fontes, tamanhos e etc

#criar botões pra serem usados, "gerar" e "copiar"

root =tkinter.Tk()
root.geometry("500x500") 
 
root.title("Gerador de Senhas Aleatório")
 
output_pass = tkinter.StringVar()
 
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  

 
def randPassGen():
    password = "" 
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)   
        password = password + random.choice(char_type)
     
    output_pass.set(password)
 

 
def copyPass():
    pyperclip.copy(output_pass.get())
 
 
pass_head = tkinter.Label(root, text = 'Tamanho da Senha', font = 'arial 12 bold').pack(pady=10) 
 
pass_len = tkinter.IntVar() 
length = tkinter.Spinbox(root, from_ = 6, to_ = 42 , textvariable = pass_len , width = 24, font='arial 16').pack()

tkinter.Button(root, command = randPassGen, text = "Gerar Senha", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
pass_label = tkinter.Label(root, text = 'Senha Gerada', font = 'arial 12 bold').pack(pady="30 10")
tkinter.Entry(root , textvariable = output_pass, width = 24, font='arial 16').pack()
 
tkinter.Button(root, text = 'Copiar', command = copyPass, font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
root.mainloop() 

