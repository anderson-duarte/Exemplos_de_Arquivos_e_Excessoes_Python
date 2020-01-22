'''
Created on 27 de dez de 2019

@author: Valentina
'''
nome_do_arquivo =r'C:\Users\Valentina\Desktop\arquivos_acessiveis_a_python\capitulo_10\cachorro.txt'
nome_do_arquivo1 =r'C:\Users\Valentina\Desktop\arquivos_acessiveis_a_python\capitulo_10\gato.txt'

print("***** MOSTRAR CACHORROS *****")

try:
    with open(nome_do_arquivo, 'r+') as escrever:
        cachorros = escrever.readlines()
        for cachorro in cachorros:
            print(cachorro.rstrip())   
except ValueError:
    print("Arquivo nao encontrado.")


print("***** MOSTRAR GATOS *****")

try:
    with open(nome_do_arquivo1, 'r+') as escrever:
        gatos = escrever.readlines()
        for gato in gatos:
            print(gato.rstrip())   
except ValueError:
    print("Arquivo nao encontrado.")