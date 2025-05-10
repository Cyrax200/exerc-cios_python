#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o valor do seu salário: "))
if salario > 1250:
    print(f"Seu novo salário vai passar a ser: R${((10 / 100) * salario) + salario:.2f}")
else:
    print(f"Seu novo salário vai passar a ser: R${((15/100) * salario) + salario:.2f}")