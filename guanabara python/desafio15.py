dias_aluguel = int(input("Digite quantos dias você alugou o carro: "))
quant_km = int(input("Digite a quantidade de KM percorrido: "))
print(f" Você pagara o valor de : {(dias_aluguel * 60) + (quant_km * 0.15)}")
