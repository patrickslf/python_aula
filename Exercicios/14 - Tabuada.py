'''

Autor: Patrick Santos
Data: 13/06/2024
Versão: 1.0
Algoritimo: "Tabuada 1 ao 10"
DESCRIÇÃO: Faça um programa que calcule a tabuada do 0 ao 10
            

'''


for numero2 in range (1,11):
    print('\n')
    print (f'Aqui está a tabuada do {numero2}')
    for numero in range (11):
        print(f'{numero2} x {numero} = {numero * numero2}') #Ou print(numero2,'x',numero, '=', numero*numero2)