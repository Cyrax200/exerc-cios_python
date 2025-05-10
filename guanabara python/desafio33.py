#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n = []
for i  in range(3):
    num = int(input("Informe um numero: "))
    n.append(num)
print(*n,sep = ", ")
print(f"O maior numero é {max(n)}")
print(f"O menor numero é {min(n)}")


