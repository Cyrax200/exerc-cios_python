#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#  mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
multa = 7.0
velocidade_max = 80
velocidade = float(input("Digite a velocidade que você passou no Radar: "))
pag_multa = (velocidade - 80) * 7
if velocidade > velocidade_max:
    print(f"você foi multado , você deve pagar: R${pag_multa:.2f}")
else:
    print(f"continue na velocidade permitida")