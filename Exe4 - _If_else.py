'''
Abertura Comentario

Autor: Patrick Santos
Data: 28/05/2024
Versão: 1.0
DESCRIÇÃO: Estudo do condicional IF ... ELSE

Fechamento comentario
'''
#==========================================================
#Variavel
nota = 0
#Entrada
nota = int(input('Insira uma nota:'))

#Processamento
if (nota >= 6):
    print ('A nota é:', nota)
    print('Aluno aprovado')
    #Saida
    
else: #if(nota <6): #Ao invés de fazer dois comandos iguals com o 'IF'
#       O 'ELSE' já serve para dar a condição contraria.
    print ('A nota é:', nota)
    print('Aluno reprovado')

#==========================================================

