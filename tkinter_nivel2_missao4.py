#Importação de todos os elementos do tkinter
import tkinter
from tkinter import *
from PIL import ImageTk, Image


#Função que define escrever um texto na tela e imprimir que o botão foi pressionado no console
def funcClicar():
    texto = Label(master=janelaPrincipal, text='Você apertou esse botão')  # Criação do elemento
    texto.pack()
    print('Botão pressionado')


#criação da janela
janelaPrincipal = Tk()  #Um objeto Tk é um elemento que representa a janela GUI


# #Elemento Label utilizado para exibir textos
texto = Label(master = janelaPrincipal, text = 'Minha janela exibida')  #Criação do elemento
texto.pack()


#Insere uma imagem
pic = ImageTk.PhotoImage(Image.open('gatinho.jpg'))
gato = Label(master=janelaPrincipal, image=pic)
gato.pack()


#Insere um botão e da um comando para ele
botao = Button(master = janelaPrincipal, text = 'Clique aqui', command = funcClicar)
botao.pack()


# texto.place(x = 50, y = 100)  #Posicionamento de elemento na janela
janelaPrincipal.mainloop()  #Para exibir a janela é necessário chamar o método mainloop


