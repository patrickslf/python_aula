'''
Descrição   : Escreva um algoritmo para exibir o nome do mês por extenso
                de acordo com o número que o representa:
                        1	    Janeiro
                        2	    Fevereiro
                        3	    Março
                        4	    Abril
                        5	    Maio
                        6	    Junho
                        7	    Julho
                        8	    Agosto
                        9	    Setembro
                        10	    Outubro
                        11	    Novembro
                        12	    Dezembro

'''
#==========================================================================

#Variavel
mes = 0
mes_escolhido = ''
#entrada
print('*******************************************************')
print('Qual o mês do seu aniversário:')
print ('\n1. Janeiro \n2. Fevereiro \n3. Março \n4. Abril \n5. Maio \n6. Junho \n7. Julho \n8. Agosto \n9. Setembro \n10. Outubro \n11. Novembro \n12. Dezembro')
mes = int(input('Digite o mês escolhido:'))
#processamento
if (mes == 1):
    mes_escolhido = 'Janeiro.'
elif (mes == 2):
    mes_escolhido = 'Fevereiro.'
elif (mes == 3): 
    mes_escolhido = 'Março'
else:
    mes_escolhido = 'Opção inválida.'

#saida
print ('Você faz aniversário em', mes_escolhido)