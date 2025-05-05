#Seno, Cosseno  e Tangente
from math import radians,sin,cos,tan
angulo = float(input("Digite um angulo: "))
rad = radians(angulo)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)
print(f"O angulo de  {angulo} tem o Seno de  {seno:.2f} ")
print(f"O angulo de  {angulo} tem o cosseno de  {cosseno:.2f} ")
print(f"O angulo de  {angulo} tem a tangente de  {tangente:.2f}")

print("FINAL")
