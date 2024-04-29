def recomendar_plano(consumo_mensal):
    
  if consumo_mensal <= 10:

    return "Plano Essencial Fibra - 50Mbps"

  elif consumo_mensal <= 20:

    return "Plano Prata Fibra - 100Mbps"

  else:
    return "Plano Premium Fibra - 300Mbps"

consumo = float(input("Qual o consumo?: "))

plano_recomendado = recomendar_plano(consumo)

print("O plano recomendado para o seu consumo é:", plano_recomendado)

#Detalhe importante que vale resaltar, pelo desafio no site, o código da diversos erros e é necessaria varias alterações
#quando alterado ao maximo, é verificado que o print tem que ser simples e o input vazio, só assim passa no desafio