''''

Autor: Patrick Santos
Data: 07/06/2024
Versão: 1.0
DESCRIÇÃO: Estudo da estrutura de repetição "While"

'''

#========================================================
indice = 1 
while indice < 23:
    print (indice,'Patrick')
    indice = indice + 1 #indice += 1
#========================================================
indice_2 = 10
while indice_2 > 0:
    print(indice_2, 'Patrick')
    indice_2 = indice_2 - 1
#========================================================
indice3 = 1
while True:
    print(indice3)
    indice3 = indice3 + 1 
    if indice3 == 5:
        break
#========================================================


troca = 0
tentativas = 3
senhapadrao = 'senai115'
while True:
    senha = input('Digite a senha de acesso para iniciar o programa:')
    if senha == senhapadrao:
        
        print('Seja bem vindo ao Senai Suiço-Brasileiro.')
        
        troca = input('Escolha a opção desejada \n 1 - Alterar sua senha cadastrada. \n 2 - Voltar ao menu principal.')
    
    else:
        tentativas = tentativas - 1
        print('Você só possui mais', tentativas, 'tentativas')
        if tentativas <= 0:
            print('Acesso bloqueado, entre em contato com a central de relacionamento.')
            break