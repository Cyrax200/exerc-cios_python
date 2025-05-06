#Sorteando uma ordem na lista
import random
alunos = []
for _ in range(4):
    aluno =  str(input("Digite o nome de um aluno: "))
    alunos.append(aluno)
random.shuffle(alunos)
print(alunos)