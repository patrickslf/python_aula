'''
Abertura Comentario

Autor: Patrick Santos
Data: 28/05/2024
Versão: 1.0
DESCRIÇÃO: Estudo do condicional IF ... ELIF

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
elif(nota < 4 ): #else if(nota <4): 
    print ('A nota é:', nota)
    print('Aluno reprovado')
else:
    print('Aluno em recuperação')
#==========================================================




















