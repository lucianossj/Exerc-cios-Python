frase=input("Digite a sua frase: ")
if (len(frase) < 0) or (len(frase) > 100):
	print("A frase deve conter um número de caracteres entre 1-100.")
else:
    palavras = frase.split(" ")

    print('Frase: ' + frase)
    print('Número de palavras: ' + str(len(palavras)))

    fraseInversa = palavras[::-1]

    print(str(fraseInversa).replace("[","",1).replace("]","",1).replace("'","",len(palavras)*2).replace(",","",len(palavras)-1))
