'''
Abertura Comentario

Autor: Patrick Santos
Data: 04/06/2024
Versão: 1.0
DESCRIÇÃO: Escreva um programa que leia a velocidade maxima permitida em 
        uma avenida e velocidade com que o motorista estava dirigindo nela e
        calcule a multa que uma pessoa vai receber.
            
            Velocidade Ultrapassada            Valor da Multa
                até 10 km/h                     R$ 50,00
                11 a 30 km/h                    R$ 100,00
                mais 31 km/h                    R$ 200,00
                
Fechamento comentario
'''

#===============================================================
#variaveis
velocidadevia = 0
velocidadecondutor = 0
diferenca = 0
multa = '' 
#Entrada
velocidadevia = int(input('Qual a velocidade maxima permitida na via?'))
velocidadecondutor = int ( input('Qual velocidade atingida pelo condutor?'))

#Processamento
diferenca = velocidadecondutor - velocidadevia
print(diferenca)
if (diferenca > 0 and diferenca <= 10):
    multa = 'O condutor foi multado no valor de R$ 50,00'

elif (diferenca >= 11 and diferenca <= 30):
    multa = 'O condutor foi multado no valor de R$ 100,00'
elif (diferenca >= 31):
    multa = 'O condutor foi multado no valor de R$ 200,00'

else:
    multa = 'Motorista isento de multa'

#Saida
print (multa)
