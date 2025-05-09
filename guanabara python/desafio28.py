#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#  O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
num = random.randint(0,5)
user = int(input("escreva um numero de 0 a 5 para tentar advinhar o numero que o computador escolheu: "))
if num == user:
    print(f"você acertou, o computador escolheu o numero {num}")
else:
    print(f"você errou, o computador pensou no numero {num}")
