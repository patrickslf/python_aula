'''

Autor: Patrick Santos
Data: 13/06/2024
Versão: 1.0
Algoritimo: "Tabuada"
DESCRIÇÃO: Faça um programa que calcule a tabuada de um numero 
            digitado pelo usuario.

'''

#===============================================================

numero = 0
resultado = 0 
numero = int(input('Digite um numero:'))
for numero2 in range (11):
    #resultado = numero * numero2
    print(f'{numero2} x {numero} = {numero * numero2}') #Ou print(numero2,'x',numero, '=', numero*numero2)



