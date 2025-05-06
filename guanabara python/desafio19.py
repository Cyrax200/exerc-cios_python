#Sorteando  um item na lista
import random
alunos = []
for _ in range(4):
    aluno = str(input("Digite o nome de um aluno: "))
    alunos.append(aluno)
sorteado = random.choice(alunos)
print(f"O nome sorteado foi ___{sorteado}___")


