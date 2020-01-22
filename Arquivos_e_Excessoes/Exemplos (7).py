'''
Created on 27 de dez de 2019

@author: Valentina
'''
prosseguir = True

while prosseguir:
    try:
        numero = int(input("Primeiro numero. "))
        numero1 = int(input("Segundo numero. "))
    except ValueError:
        print("Desculpe nao e possivel fazer o calculo utilizando algarismos alfabetico")
    else:
        print(str(numero + numero1))
        
    msg = input("Deseja continuar? 'Y' ou 'N' ")
    if(msg == 'N'):
        prosseguir = False
    