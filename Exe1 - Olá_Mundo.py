#==========================================================
#Autor: Patrick Santos
#Data: 23/05/2024
#Versão: 1.0
#DESCRIÇÃO: Algoritimo que recebe o nome de usuario
#           e exibe uma frase de saudação concatenada com
#           a entrada do usuário.
#==========================================================


#Observações:
#           a) para iniciar um comentario utiliza-se '#'
#           b) No visul studio utilizar o comando 'cntrl' + ';'
#               para comentar um bloco de codigo
#==========================================================
#Inicio

dadoVazio = ''#variavel atribuida com um valor vazio

#entrada
nome= input ('Qual o seu nome?')
#Processamento
mensagem = 'Olá seja bem-vindo!'
frase = mensagem + nome
#Saida
print(frase)
#==========================================================