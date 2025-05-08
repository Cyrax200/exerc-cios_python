#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: "))
contagem  = frase.count('a')
letra = 'a'
print(frase)
print(f"A frase possue {contagem} letras a ")
print(f"A primeira letra a encontrasse posição: {frase.find(letra)}")
print(f"A ultima letra a encontrasse posição: {frase.rfind(letra)}")

if frase.find(letra) == -1:
    print("Não há letra (a) no nome informado")


