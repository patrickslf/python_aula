'''
<<<<<<< HEAD
Descrição   : Crie uma matriz e apresente ela no final da execução, aonde 
            existe duas colunas [Tipo, Nome] e 4 linhas preenchidas com
            o tipo do animal e seu respectivo nome

            #   Tipo Nome
            0   Gato Frajola
            1   Cão  Coragem
            2   Passarinho  Pica-pau
            3   Urso Ursinho Pooh
'''
tabela_petshop = [
                    ['#','Tipo','Nome'],
                    ['0','Gato','Frajola'],
                    ['1','Cão','Coragem'],
                    ['2','Passarinho','Pica-pau'],
                    ['3','Urso','Ursinho Pooh']
                ]

for linha in range(5):
    linha_completa = ''
    for coluna in range(3):
        linha_completa += tabela_petshop[linha][coluna] + ' | '
    print(f'{linha_completa}')
=======

Descição    : Crie uma matriz e apresente ela no final da execução, aonde 
            existe duas colunas [tipo, nome] e 4 linhas preenchidas com 
            o tipo do animal e seu respectivo nome.

            #   Tipo    Nome
                Gato    Garfield
                Cão     Scooby Doo
                Passaro Pica-Pau
                Urso    Catatau

'''

#tipo = ['Gato', 'Cão', 'Passaro', 'Urso']
#nome = ['Garfield', 'Scooby-Doo', 'Pica-Pau', 'Catatau']

#tabela = [tipo, nome]
#print(tabela [1][1])



tabela_petshop = [
                    ['#', 'tipo', 'Nome'],
                    ['0', 'Gato', 'Garfield'],
                    ['1', 'Cão', 'Scooby-doo'],
                    ['2', 'Passaro', 'Pica-pau'],
                    ['3', 'Urso', 'Catatau'],
                ]

for linha  in range(5):
    linhacompleta = ''
    for coluna in range(3):
        linhacompleta += tabela_petshop[linha][coluna] + '|'
    print(f'{linhacompleta}')
>>>>>>> 818b347fdd85fe1c523c52e8a98ad19e642baffd
