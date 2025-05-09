#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR
num = int(input("Digite um numero para saber se é PAR: "))
if  num % 2 == 0:
    print(f"o numero {num} é PAR")
else:
    print(f"o numero {num} é  IMPAR")