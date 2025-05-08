#Encontrar o nome SILVA no nome completo que o usuario digitar
nome = str(input("Digite seu nome completo: "))
nome = nome.lower()
palavra = "SILVA"
palavra = palavra.lower()
if palavra in nome:
    print("o seu nome tem Silva")
else:
    print("Seu nome não tem a palavra Silva")
