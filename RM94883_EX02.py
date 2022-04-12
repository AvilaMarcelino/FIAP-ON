#Votação para escolher qual dia da semana é o melhor para a realização das lives.

dias_semana = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']
votos_dias=[]
for dia in dias_semana:
    votos_dias.append(int(input("Insira quantos votos recebeu a {}: ".format(dia))))

maior_qtd_voto = 0
dia_com_maior_voto = ''

for x in range(5):
    if(maior_qtd_voto < votos_dias[x]):
        maior_qtd_voto = votos_dias[x]
        dia_com_maior_voto = dias_semana[x]

''' ou usando While
index = 0
while(index < 5):
    if (maior_qtd_voto < votos_dias[index]):
        maior_qtd_voto = votos_dias[index]
        dia_com_maior_voto = dias_semana[index]
    index+=1'''

print('O Dia com maior voto é {}, com {} votos' .format(dia_com_maior_voto, maior_qtd_voto))






