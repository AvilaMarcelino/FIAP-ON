#O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus
# calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve
# ao longo do ano.

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











