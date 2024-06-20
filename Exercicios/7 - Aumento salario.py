'''
Abertura Comentario

Autor: Patrick Santos
Data: 04/06/2024
Versão: 1.0
DESCRIÇÃO: Faça um programa que receba o salário de um funcionário, calcule
            e mostre o novo salário sabendo-se que:
            Salario < R$ 1.000,00 Aumento de 25%
            salario >= R$ 1.000,00 e < R$ 2.000,00 aumento de 15%.
            Salário >= R$ 2.000,00 aumento de 10%

Fechamento comentario
'''
#===================================================================================

#variaveis
salario = 0 
aumento = 0
porcentagem = 0

#entrada
salario = float(input('Qual o valor do seu salário atual?:'))

#processamento
if (salario<1000):
    aumento = salario + (salario * 25 / 100) 
    print ('Aumento de 25%')
    print('Com o aumento, seu novo salario será de',round(aumento))

elif(salario >=2000):
    aumento = salario + (salario * 10 / 100)
    print ('Aumento de 10%')
    print('Com o aumento, seu novo salario será', round(aumento))
else:
    aumento = salario + (salario * 15/100)
    print ('Aumento de 15%')
    print('Com o aumento, seu novo salario será',round(aumento))
    
#saida



