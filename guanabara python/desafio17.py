#Catetos e Hipotenusa
from math import hypot
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hi = hypot(cateto_adjacente,cateto_oposto)
print(f"A ipotenusa vai medir: {hi:.2f}")

