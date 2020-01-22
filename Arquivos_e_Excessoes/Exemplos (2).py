# coding: iso-8859-1 -*-
'''
Created on 26 de dez de 2019

@author: Valentina
'''
nome_do_arquivo =r'C:\Users\Valentina\Desktop\arquivos_acessiveis_a_python\capitulo_10\python.txt'

texto = ''

with open(nome_do_arquivo) as objeto_capturado:
    linhas = objeto_capturado.readlines()
    for linha in linhas:
        print(linha.rstrip())
        texto += linha.strip()
       
print() 
print(texto)
t1 = texto.replace('Python', 'JAVA')
print(t1)


        