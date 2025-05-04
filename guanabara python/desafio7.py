notas = []
for _ in range(2):
    nota =float(input("Digite a nota do aluno: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print(media)

