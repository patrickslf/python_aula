'''
Descrição : Faça um programa que receba o numero do mês e 
            apresente ele por extenso:
            Sem utilizar condicional!

'''

mes = ['','Janeiro', 'Fevereiro', 'Maço', 'Abril', 'Maio', 'Junho', 'Julho', 
       'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

while True:
    mes2 = 0
    mes2 = int(input('Digite um número de 1 a 12 para indicar o mes selecionado:'))
    print (mes [mes2])
    break