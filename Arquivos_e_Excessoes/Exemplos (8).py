'''
Created on 27 de dez de 2019

@author: Valentina
'''
def adicionar_animal(arquivo, variavel):
    try:    
        with open(arquivo, 'a') as escrever:
            escrever.write(variavel + "\n")   
    except ValueError:
        print("Arquivo nao encontrado.")
    else:
        print("Adicionado com Sucesso")