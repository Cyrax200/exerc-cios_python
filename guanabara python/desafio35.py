#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
p = float(input("Digite o primeiro segmento: "))
s = float(input("Digite o primeiro segmento: "))
t = float(input("Digite o primeiro segmento: "))

if p < s +  t and s < p + t and  t < p + s:
    print("os segmentos a cima podem formar um triangulo: ")
else:
    print("Os segmentos não podem formar um triangulo")

