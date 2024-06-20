''''

Autor: Patrick Santos
Data: 17/06/2024
Versão: 1.0
DESCRIÇÃO: Estudo do tipo de dado Array (Vetor)

'''
carros = ['vw']

carros.append ('GM')
carros.append ('Ford')
carros.append ('Fiat')
carros.append ('Renalt')

print(carros)

#escolha = int(input('Digite um numero para descobrir uma marca de carro:'))

#print(carros[escolha])

carros.remove('Ford') 
print(carros)

carros.pop(3)#remove item indicando index(numero)
print(carros)

#print(carros[escolha])

print(len(carros))#Tamanho do vetor
carros.pop(len(carros) - 1) #Deleta sempre a última posição do array
print(carros)