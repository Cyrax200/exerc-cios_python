#Informar se a palavra SANTOS esta na cidade digitada
cidade = input("Digite o nome de uma cidade: ")
cidade = cidade.lower()
palavra = "SANTOS"
palavra = palavra.lower()

if palavra in cidade:
    print("A palavra Santos esta na cidade digitada ")
else:
    print("A palavra Santos não se encontra na cidade digitada ")





