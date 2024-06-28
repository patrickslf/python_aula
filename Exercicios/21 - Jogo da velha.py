'''
Descrição: Faça um Jogo da velha
'''

idosa = [['1','2','3'],
         ['4','5','6'],
         ['7','8','9']]
rodadas = 0
jogador = 'X'
def mostrar_vencedor(vencedor):#vencedor escopo local da função
    print('Temos um vencedor!', vencedor)
    
while rodadas < 9:
    linhacomplementar = '-------------'
    posicao = input(f'jogador {jogador} escolha uma posição:')
    posicao_encontrada = False
    for linha in range(3):
        linha_completa = ''
        for coluna in range(3):
            if posicao == idosa[linha][coluna]:
                idosa[linha][coluna] = jogador
                posicao_encontrada = True
            linha_completa += idosa [linha][coluna] + ' | '
        print(f' {linha_completa}')
        print(linhacomplementar)
    if posicao_encontrada == True:
        rodadas = rodadas + 1
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'
    else:
        print('posicao não encontrada')

    if (idosa [0][0] == idosa [0][1] == idosa [0][2]): #linha 1
        mostrar_vencedor(idosa [0][0])
        break
    elif(idosa [1][0] == idosa [1][1] == idosa [1][2]): # linha 2
        mostrar_vencedor(idosa [1][0])
        break
    elif(idosa [2][0] == idosa [2][1] == idosa [2][2]): # linha 3
        mostrar_vencedor(idosa [2][0]) 
        break    
    elif(idosa [0][0] == idosa [1][0] == idosa [2][0]): #coluna 1
        mostrar_vencedor(idosa [0][0]) 
        break
    elif(idosa [0][1] == idosa [1][1] == idosa [2][1]): #coluna 2
        mostrar_vencedor(idosa [0][1])
        break
    elif(idosa [0][2] == idosa [1][2] == idosa [2][2]): #coluna 3
        mostrar_vencedor(idosa [0][2]) 
        break
    elif(idosa [0][0] == idosa [1][1] == idosa [2][2]): #diagonal 1
        mostrar_vencedor(idosa [0][0])
        break    
    elif(idosa [0][2] == idosa [1][1] == idosa [2][0]): #diagonal 1
        mostrar_vencedor(idosa [0][2])
        break 
else:
    print('Velha, tente novamente!')