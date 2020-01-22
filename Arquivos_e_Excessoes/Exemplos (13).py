'''
Created on 27 de dez de 2019

@author: Valentina
'''
import json

nome_do_arquivo =r'C:\Users\Valentina\Desktop\arquivos_acessiveis_a_python\capitulo_10\numero.json'

with open(nome_do_arquivo, 'w') as numer:
    umer = int(input("Qual seu numero favorito? "))
    json.dump(umer, numer)
    
    


with open(nome_do_arquivo, 'r+') as num:
    umer = json.load(num)
    print( "Seu numero favorito e: " + str(umer))