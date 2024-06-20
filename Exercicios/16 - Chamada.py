'''
Descrição : Faça um programa que insira o numero da chamada 
            do aluno e apresente o nome dele.

'''


#============================================================
'''
alunospython = ['Luana', 'Gustavo', 'Danielle', 'Felipe', 'João', 'Thiago', 'Vitor', 'José', 'Arthur', 'Predro', 'Mauricio', #Array
                'Davi', 'Kauan', 'Andrei', 'Lucas', 'Diego', 'JOão', 'Ana', 'Vinicius', 'Adriel', 'Patrick', 'Bruno']
'''
#1° Exemplo
'''
aluno = 0
aluno = int(input('Digite o número do aluno:'))
print (alunospython [aluno])
'''
#Para fazer com que o programa apresente o nome do aluno digitando o número, basta criar um 'print' e acrescentar a variavel'Array' 
# onde contém os dados que deverão ser apresentados e acrescentar a variavel que será inserida o valor desejado dentro de'[]'.

#============================================================
alunospython = ['Luana', 'Gustavo', 'Danielle', 'Felipe', 'João', 'Thiago', 'Vitor', 'José', 'Arthur', 'Predro', 'Mauricio', #Array
                'Davi', 'Kauan', 'Andrei', 'Lucas', 'Diego', 'JOão', 'Ana', 'Vinicius', 'Adriel', 'Patrick', 'Bruno']

while True:
    aluno = 0
    aluno = int(input('Digite o número do aluno:'))
    print (alunospython [aluno])

    continuar = input ('Digite S para sair e C para continuar:')
    if continuar == 'S':
        print ('Até mais!')
        break
    elif continuar == 'C':
        print (continuar)
        