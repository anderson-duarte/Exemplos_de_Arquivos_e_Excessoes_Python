'''
Created on 27 de dez de 2019

@author: Valentina
'''
from capitulo_10_Arquivos_e_Excessoes.Exercicio_08 import adicionar_animal

nome_do_arquivo =r'C:\Users\Valentina\Desktop\arquivos_acessiveis_a_python\capitulo_10\cachorro.txt'
nome_do_arquivo1 =r'C:\Users\Valentina\Desktop\arquivos_acessiveis_a_python\capitulo_10\gato.txt'

x = 0

while x < 3:
    cachorro = input("Nome do Cachorro. ")
    gato = input("Nome do gato. ")
    adicionar_animal(nome_do_arquivo, cachorro)
    adicionar_animal(nome_do_arquivo1, gato)
    x += 1