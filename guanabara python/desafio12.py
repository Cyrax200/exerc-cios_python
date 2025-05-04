#Calculando Desconto
produto = float(input("Digite o valor do produto: "))
desconto =  produto * (5 / 100)
valor_total = produto - desconto
print(f"Você recebeu de desconto R$: {desconto:.2f} , seu produto vai sair no valor de R$: {valor_total:.2f}")