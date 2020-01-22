# coding: iso-8859-1 -*-
'''
Created on 26 de dez de 2019

@author: Valentina
'''
nome_do_arquivo =r'C:\Users\Valentina\Desktop\arquivos_acessiveis_a_python\capitulo_10\descricao.txt'

texto = ''

with open(nome_do_arquivo, 'a') as escrever:
    descricao = input("Qual seu descricao? ")
    escrever.write(descricao + "\n")
    
print("Ola, " + descricao)
  

        