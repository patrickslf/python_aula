#==============================================================
#Autor: Patrick Santos
#Data: 23/05/2024
#Versão: 1.0
#DESCRIÇÃO: Faça um algoritimo que um valor na moeda real (R$),
#           a cotação da conversão REAL para DOLAR, e apresente 
#           a quantidade desse valor em dolar ($)
#           ---------------------------------------------------
#           Exemplo de execução 
#           Insira o valor em real: 5000
#           Insira a cotação do dia: 5
#           R$5000,00 equivalem $1000,00
#           ---------------------------------------------------
#===============================================================
#variaveis
real = 0 #recebo o valor em reais
cotacao = 0 #valor da cotacao 1 dolar x reais
dolar = 0 #valor convertido real para dolar
#Entrada
print ('========================================================')
real = float(input('Insira o valor em Real:')) #usando casting 'Float'
cotacaodia = float(input('Insira a cotação do dia:')) #usando casting 'Float'
#Processamento
dolar = real / cotacaodia 
#Saida
print(real , 'Equivale a:' , dolar )
print ('========================================================')
