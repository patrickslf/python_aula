'''
Descrição   : Faça um programa que adicione alunos ao sistema da escola 
              (array) ou remova um aluno especifico.
              Nesse sistema deve estar previsito um menu com três opções:
              #===================================
              Sistema SENAI
              1 - Adicionar aluno:
              2 - Remover aluno:
              3 - Apresentar alunos
              4 - Sair
              Insira a opção desejada: 
              #===================================   
              Adicionar aluno
              Insira o nome do aluno:
              #===================================   
              Remover aluno
              Insira o nome do aluno para ser removido:
              #===================================   
              Alunos no sistema
              ['João', 'Pedro','Luana']
              #===================================   
'''

#variaveis:

addaluno = 0
deletealuno = 0 
apresentar = 0
#processamento

alunos =['João', 'Pedro', 'Luana']
while True:
    menu = 0
    print('=-'*30)
    print ('Sistema SENAI.\n 1 - Adicionar aluno: \n 2 - Remover aluno: \n 3 - Apresentar alunos \n 4 - Sair')
    print('=-'*30)
    menu = int(input('INSIRA A OPÇÃO DESEJADA:.')) 
    print('=-'*30)
    if menu == 1:
        addaluno = input('INSIRA O NOME DO ALUNO:')
        alunos.append(addaluno)
        print('Aluno adicionado com sucesso!')
        print('=-'*30)
        print('\n'*2)
        
    elif menu ==2:
        deletealuno = input('INSIRA O NOME DO ALUNO PARA SER REMOVIDO:')
        alunos.remove(deletealuno)
        print('Aluno removido com sucesso!')
        print('=-'*30)
        print('\n'*2)
        
    elif menu == 3:
        print ('ALUNOS CADASTRADOS NO SISTEMA:')
        print(alunos)
        print('Esses são todos os alunos no sistema:')
        print('\n'*2)

    else:
        print ('Saindo...')
        break

