''''

Autor: Patrick Santos
Data: 25/06/2024
Versão: 1.0
DESCRIÇÃO: Estudo do tipo de dado Array (Vetor)

'''


aluno_sala = ['Luana', 'Gustavo', 'Daniele']
aluno_sala.append('Felipe')
print (aluno_sala)

print(aluno_sala[2])

for indice in range (4):
    print (aluno_sala[indice])

for  aluno in aluno_sala:
    print (aluno)


            #    0      1         2 
cabecalho = ['Nome', 'Idade', 'Matricula']
        #    0         1      2
dado_um = ['Pele', 'Eterno', '10']

print (dado_um[0]) # -> Pelé
#=====================================================================           
#Matriz -> um Array com array dentro

             # 0         1
tabela = [cabecalho, dado_um]
print(tabela [1][0]) # -> Pelé


#[      0        1          2
# 0  ['Nome', 'Idade', 'Matricula'],  
# 1  ['Pelé', 'Eterno', '   10   ']