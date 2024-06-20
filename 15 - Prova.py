'''
Descrição : Faça um programa que receba dois valores, sendo que o
            primeiro deve ser menor que o segundo.
            O programa deve apresentar todos os números ímpares contidos nesta seuqencia.
            (Modulo %. Exemplo: 7%2 = 1)

'''
v = 0 
v2 = 0

v = int(input(f'Digite um valor:'))
v2 = int(input('Digite um valor:'))
for c in range (v,v2):
    resto = c % 2 
    if resto == 1:
        print(f'{c} % 2 = {resto}')
   