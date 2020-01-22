'''
Created on 26 de dez de 2019

@author: Valentina
'''
nome_do_arquivo =r'C:\Users\Valentina\Desktop\arquivos_acessiveis_a_python\capitulo_10\programacao.txt'

texto = ''
continuar = True

with open(nome_do_arquivo, 'a') as escrever:
    while continuar:
        descricao = input("Por que gosta de programar? ")
        escrever.write(descricao + "\n")
        parar = input("Deseja continua? 'S' sim 'N' nao. ")
        if(parar == 'N'):
            continuar = False
    