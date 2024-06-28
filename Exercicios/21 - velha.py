'''
Descição    : Faça um jogo da velha.

'''
velha = [ ['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']
        ]

rodadas = 0
jogador1 = 'X'
while rodadas <9:
    posicao = input(f'Jogador {jogador1} Selecione uma posição:')
    posicao_encontrada = False
    linhacomplementar = '------  -----  ------'  
    for linha in range (3):
        linhacompleta = ''
        for coluna in range (3):
            if posicao == velha[linha][coluna]:
                velha[linha][coluna] = jogador1 
                posicao_encontrada = True
            #linhacompleta = linhacompleta + clsvelha [linha][coluna] + '|'
            linhacompleta += '   |' + velha [linha][coluna] + '|'
        print(linhacompleta)
        print(linhacomplementar)
    if posicao_encontrada == True:
        rodadas = rodadas + 1
        if jogador1 == 'X':
         jogador1 = 'O'
        else:
            jogador = 'X' 
    else:
         print('Posição não encontrada')