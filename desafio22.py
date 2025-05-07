#Informar nome  maiusculo , minusculo,quantas letras tem o primeiro nome.
nome = input("Digite seu nome completo: ")
print(f"Seu nome com Letras maiusculas: {nome.upper()}")
print(f"Seu nome com Letras minusculas: {nome.lower()}")
print(f"Seu nome tem {len(nome.replace(" ", ""))} LETRAS")
print(f"O seu primeiro nome tem {len(nome.split()[0])} LETRAS")


