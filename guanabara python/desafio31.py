#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Escreva a distancia da sua viagem em: "))
preco1 = 0.50
preco2 = 0.45
if distancia  <= 200:
    print(f" o preço da sua passagem será: R${distancia * preco1:.2f}")
else:
    print(f" o preço da sua passagem será: R${distancia * preco2:.2f}")
