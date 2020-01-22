'''
Created on 26 de dez de 2019

@author: Valentina
'''

try:
    num = int(input('Digite um numero. '))
    num1 = int(input("Digite outro numero. "))
    soma = num + num1
except ValueError:
    msg = "Desculpe nao e possivel fazer o calculo utilizando algarismos alfabetico" 
    print(msg)
else:
    print(str(soma))