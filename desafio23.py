#Informar unidade , dezena , centena e milhar de um numero digitado
num = int(input("digite um numero de  0 a 9999: "))
u = num// 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"UNIDADE {u}")
print(f"DEZENA {d}")
print(f"CENTENA {c}")
print(f"MILHAR {m}")