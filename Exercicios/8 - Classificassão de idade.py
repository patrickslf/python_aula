'''
Abertura Comentario

Autor: Patrick Santos
Data: 04/06/2024
Versão: 1.0
DESCRIÇÃO: Escreva um programa que leia a idade de um indivíduo e
        escreva a faixa etária a que pertence, de acordo com a tabela abaixo;
            e mostre o novo salário sabendo-se que:
            
            Faixa etária            Classificação
                <12                     Criança
                13-17                   Adolescente
                18-59                   Adulto

Fechamento comentario
'''
#entrada
classificacao = int(input('Qual sua classificação de acordo com sua idade?:'))
#processamento
if (classificacao >= 0 and classificacao <=12):
    print('Classificado como Criança')

elif (classificacao >= 13 and classificacao <= 17 ):
    print('Classificado como Adolescente')
elif (classificacao >=18 and classificacao <= 59):
    print ('Classificado como Adulto')

elif (classificacao > 59):
    
    print ('Classificado como 3° Idade')
else:
    print('idade invalida')



''' 

Outra forma que pode ser feito o codigo é:
feito para ser printado apenas no final.

'''

#variaveis
idade = 0
classificacao = 0

#entrada
idade = int(input('Qual sua classificação de acordo com sua idade?:'))
#processamento
if (idade >= 0 and idade <=12):
    classificacao ='Classificado como Criança'

elif (classificacao >= 13 and classificacao <= 17 ):
    classificacao ='Classificado como Criança'

elif (classificacao >=18 and classificacao <= 59):
    classificacao ='Classificado como Criança'

elif (classificacao > 59):
     classificacao ='Classificado como Criança'
else:
    classificacao = 'idade inserida invalida'
#saida
print (classificacao)
#======================================================================