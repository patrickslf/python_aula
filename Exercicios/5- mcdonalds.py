'''
Autor: Patrick Santos
Data: 28/05/2024
Versão: 1.0
DESCRIÇÃO   : Escreva um algoritimo para exibir o nome do lanche de acordo
        com o numero inserido pelo usuário, seguindo a tabela abaixo:
               
                    N°      Lanche
                    1       Big Mac
                    2       Quarteirão
                    3       McChicken
                    4       Cheddar McMelt
                    5       McFish

'''
#================================================================
#variaveis
lanche = 0
lanche_escolhido = ''
#entrada
print('*******************************************************')
print ('Bem vindo ao Mc Donalds, o que gostaria de pedir hoje?')
print('N° Lanche\n1. Big Mac\n2. Quarteirão\n3. McChicken\n4. Cheddae MacMelt\n5. McFish') #'\n'seria como se fosse o enter
lanche = int(input('Digite o número do lanche desejado:'))

#processamento
if(lanche == 1):
    lanche_escolhido = 'BigMac'

elif (lanche == 2):
    print('Quarteirão')

elif (lanche == 3):
    print('McChicken')

elif (lanche == 4):
    print('Cheddar McMelt')

elif (lanche == 5):
    print ('McFish')
else:
    print ('Opção inválida')

print ('Seu pedido está sendo preparado. Obrigado por escolher o McDonalds!')