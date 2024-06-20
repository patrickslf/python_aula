#==============================================================
#Autor: Patrick Santos
#Data: 28/05/2024
#Versão: 1.0
#DESCRIÇÃO: Faça um algoritimo que receba o raio em metros de um
#           circulo e apresente a sua area
#           ---------------------------------------------------
#           Exemplo de execução 
#           Insira o raio em metros: 5
#           area do circulo: 78.5m^2
#           ---------------------------------------------------
#           a = área
#           pi = 3.14
#           r = raio
#           a = pi*(r^)
#           ---------------------------------------------------
#===============================================================
#Variaveis
a = 0 #area
pi = 3.14 #constante pi
r = 0 #raio
#Entrada
r = float(input('Insira o raio do circulo em metros:')) #usando casting 'Float'

#Processamento
a = pi*(r**2)

#Saida
print('A area do circulo', a, 'm^2')
#===============================================================
