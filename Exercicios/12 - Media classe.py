'''
Algoritmo "Média turma"
Descrição   : Faça um programa que receba duas notas de seis alunos. 
                Calcule e mostre:
            	A média aritmética das duas notas de cada aluno; e
            	A mensagem que está na tabela a seguir:
                    Média Aritmética	Mensagem
                    Até 3	            Reprovado 
                    Entre 3 e 7 	    Exame
                    De 7 para cima	    Aprovado

            	O total de alunos aprovados;
            	O total de alunos de exame;
            	O total de alunos reprovados;
            	A média da classe.
'''
#=======================================================================
#variaveis
aluno = 0
qtdaluno = 6
alunosaprovados = 0
alunosreprovados = 0
alunosexame = 0
mediaclasse = 0
somamedia = 0 

#Aluno 1 
while aluno < qtdaluno:
    aluno = aluno + 1
    #Aluno X
    nota1 = float(input(f'Digite a primeira nota aluno{aluno}:'))
    nota2 = float(input(f'Digite a segunda nota aluno {aluno}:'))
    media = (nota1 + nota2) /2
    somamedia = somamedia + media

    if(media)<= 3:
        print('Reprovado')
        alunosreprovados += 1 #alunosreprovados = alunosreprovados + 1
        
    elif (media) > 3 and (media) <=7:
        print ('Exame')
        alunosexame += 1 #alunosexame = alunosexame + 1
        
    else:
        print('Aprovado')
        alunosaprovados +=1 #alunosaprovados = alunosaprovados + 1
    
mediafinal = round((somamedia/aluno),2)
        
print (f'Media final da turma: {mediafinal}')
print (f'Qauntidade de alunos Reprovados: {alunosreprovados}')
print (f'Qauntidade de alunos Exame: {alunosexame}')
print (f'Qauntidade de alunos Aprovados: {alunosaprovados}')

























'''
#=================================================================
    #Aluno 2
nota1 = float(input('Digite a primeira nota do aluno 2:'))
nota2 = float(input('Digite a segunda nota aluno 2:'))
media = (nota1 + nota2) /2

if(media)<= 3:
    print('Reprovado')
elif (media) > 3 and (media) <=7:
    print ('Exame')
else:
    print('Aprovado')
        
#=================================================================
    #Aluno 3 

nota1 = float(input('Digite a primeira nota aluno3:'))
nota2 = float(input('Digite a segunda nota aluno3:'))
media = (nota1 + nota2) /2

if(media)<= 3:
        print('Reprovado')
elif (media) > 3 and (media) <=7:
        print ('Exame')
else:
    print('Aprovado')
        
#=================================================================
#   Aluno 4 

nota1 = float(input('Digite a primeira nota aluno4:'))
nota2 = float(input('Digite a segunda nota aluno4:'))
media = (nota1 + nota2) /2

if(media)<= 3:
        print('Reprovado')
elif (media) > 3 and (media) <=7:
        print ('Exame')
else:
    print('Aprovado')
#=================================================================
#   Aluno 5 

nota1 = float(input('Digite a primeira nota aluno5:'))
nota2 = float(input('Digite a segunda nota aluno5:'))
media = (nota1 + nota2) /2

if(media)<= 3:
        print('Reprovado')
elif (media) > 3 and (media) <=7:
        print ('Exame')
else:
    print('Aprovado')
#=================================================================
#   Aluno 6 

nota1 = float(input('Digite a primeira nota aluno6:'))
nota2 = float(input('Digite a segunda nota aluno6:'))
media = (nota1 + nota2) /2

if(media)<= 3:
        print('Reprovado')
elif (media) > 3 and (media) <=7:
        print ('Exame')
else:
    print('Aprovado')
'''