tipo_assinatura = str(input("Insira seu tipo de assinatura: "))
faturamento_anual = float(input("Insira seu faturamento anual: "))

if tipo_assinatura.upper() == ("BASIC"):
   pagar = faturamento_anual * 0.3
   print("Valor a pagar: {}".format(pagar))
elif tipo_assinatura.upper() == ("SILVER"):
   pagar = faturamento_anual * 0.2
   print("Valor a pagar: {}".format(pagar))
elif tipo_assinatura.upper() == ("GOLD"):
   pagar = faturamento_anual * 0.1
   print("Valor a pagar: {}".format(pagar))
elif tipo_assinatura.upper() == ("PLATINUM"):
   pagar = faturamento_anual * 0.05
   print("Valor a pagar: {}".format(pagar))


#RM94883_EX02
dias_semana = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']
votos_dias=[]
for dia in dias_semana:
    votos_dias.append(int(input("Insira quantos votos recebeu a {}: ".format(dia))))

maior_qtd_voto = 0
dia_com_maior_voto = ''

index = 0
while(index < 5):
    if (maior_qtd_voto < votos_dias[index]):
        maior_qtd_voto = votos_dias[index]
        dia_com_maior_voto = dias_semana[index]
    index+=1

print('O Dia com maior voto é {}, com {} votos' .format(dia_com_maior_voto, maior_qtd_voto))









