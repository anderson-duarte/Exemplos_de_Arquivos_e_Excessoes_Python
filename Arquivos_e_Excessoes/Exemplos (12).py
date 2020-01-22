'''
Created on 27 de dez de 2019

@author: Valentina
'''
nome_do_arquivo =r'C:\Users\Valentina\Desktop\arquivos_acessiveis_a_python\capitulo_10\vasco.txt'

with open(nome_do_arquivo, 'r+') as texto:
    materia = texto.readlines()
    juntar = ''
    for linha in materia:
        juntar += linha
    qtd = juntar.lower().count('vasco')
    print(str(qtd))
    