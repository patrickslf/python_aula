#==========================================================
#Autor: Patrick Santos
#Data: 23/05/2024
#Versão: 1.0
#DESCRIÇÃO: Faça um algoritimo que receba 5 notas e imprima
#           a media final do aluno
#           --------------------------------------------
#           Exemplo de execução
#           Nota 1: 10
#           Nota 2: 10
#           Nota 3: 10
#           Nota 4: 10
#           Nota 5: 10
#           Média final: 10
#           --------------------------------------------
#==========================================================
#Entrada
#Casting => para converter o valor de string para inteiro
#   5  = int('5')
nota1 = int(input('Insira a nota 1:')) #usando casting 'int'
nota2 = int(input('Insira a nota 2:')) #usando casting 'int'
nota3 = int(input('Insira a nota 3:')) #usando casting 'int'
nota4 = int(input('Insira a nota 4:')) #usando casting 'int'
nota5 = int(input('Insira a nota 5:')) #usando casting 'int'
#Processamento
soma = nota1 + nota2 + nota3 + nota4 + nota5
media = soma/5
#Saida
print('A media do aluno é:', media)
#fim
#
#
#Observação: Toda entrada em input(##) é classificada como str, caso queira colocar como numero, é necessario iniciar com "int(input('####'))".