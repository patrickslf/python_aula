#==============================================================
#Autor: Patrick Santos
#Data: 23/05/2024
#Versão: 1.0
#DESCRIÇÃO: Faça um algoritimo que trasnforme °C
#           em °F e K
#           ---------------------------------------------------
#           Exemplo de execução 
#           Insira a temperatura em °C:0
#           Fahrenheit: 32
#           Kelvin: 273,15
#           ---------------------------------------------------
#===============================================================
#variaveis
C = 0 #Temperatura rm Celsius inserida pelo usuário
F = 0 #Tempertura em Fahrenheit vinda da conversão
K = 0 #Tempertura em Kelvin vinda da conversão
#Entrada
C = float(input('Insira o valor em °C:')) #usando casting 'Float'
#Processamento
F = (C * (9/5)) + 32 
K = (C + 273.15) 

#Saida
print(C ,'°C equivale a:' , F ,'°F' )
print(C ,'°C equivale a:' , K ,'K' )

