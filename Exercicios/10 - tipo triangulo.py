''''

Autor: Patrick Santos
Data: 04/06/2024
Versão: 1.0
DESCRIÇÃO: Faça um programa que receba 3 valores e verifique se podem representar 
        os lados em um triangulo:
            
         1 - Triângulo escaleno: triangulo que possui todos os lados com medidas diferentes.
         2 - Triangulo isósceles: triangulo que possui dois lados com medidas iguais
         3 - Triangulo equilátero: triângulo que possui todos os lados com medidas iguais.
              
         Lembrando que a soma das medidas de dois lados de um triangulo é sempre maior que a medida do terceiro lado.       
                

'''

#variaveis
a = 0
b = 0
c = 0
tipotriangulo = ''

#entrada
a = float(input('Primeiro lado:'))
b = float(input('Segundo lado:'))
c = float(input('Terceiro lado:'))
#processamento 

if ((a + b) > c and 
    (a + c) > b and 
    (b + c) > a and
    a > 0 and b > 0 and c > 0):
    print('Triangulo existe')
    if (a == b and b == c ): # forma utilizada apenas em python (a == b == c)
        tipotriangulo = 'Triangulo Equilatero'

        #como existiu a verificação no if anterior que um dos lados não são iguais,
        #não existe a necessidade da verificação do terceiro lado como diferente.

    elif (a == b or a == c or b == c):
        tipotriangulo = 'Triangulo isósceles'

    elif((a != b) and (a != c) and (b != c)):
        tipotriangulo = 'Triangulo Escaleno'

else: 
    print('Triangulo não existe')


#saida

print(tipotriangulo)
