import os
import sys
import random
    
def consiste(mens,ini,fim):
    tam=ini-1
    while tam<ini or tam>fim:
        mensagem=mens+"["+str(ini)+"-"+str(fim)+"]:"
        nome=input(mensagem)
        tam=len(nome)
    return nome

def lejogadores():
    try:
        arquivo=open("jogadores.txt","r")
        lista=arquivo.readlines()
        arquivo.close()
    except:
        lista=[]
    return lista

def cadjogadores(lista):
    nomejog=""
    repete=True
    nomejog=consiste("Jogador",3,20)
    while repete:
        repete=False
        apeljog=consiste("Apelido",3,5)
        for linha in lista:                    
            listalinha=linha.split("*")
            if listalinha[1]==(" "+apeljog+"\n"): repete=True
        if repete: print("Esse apelido já existe!")
        lista.append(nomejog+" * "+apeljog+"\n")
    return lista

def consisteop():
    op="0"
    while op!="1" and op!="2" and op!="3":
        op=input("1>Deleta 2>Altera 3>Nada:")
    return op

def editajogadores(lista):
    apeljog=consiste("Apelido",3,5)
    pos=0
    for linha in lista:                    
        listalinha=linha.split("*")
        if listalinha[1]==(" "+apeljog+"\n"):
            print(linha,end="")
            op=consisteop()
            if op=="1": del lista[pos]
            if op=="2":
                nome=consiste("Jogador",3,20)
                lista[pos]=nome+" *"+listalinha[1]
        pos+=1
    return lista

def listarjogadores():
    print('\n\n - Lista de Jogadores - \n')

    jogadores = open('jogadores.txt', 'r')
       
    for linha in jogadores:
        print(linha)

    jogadores.close()

def gravajogadores(lista):
    arquivo=open("jogadores.txt","w")
    arquivo.writelines(lista)
    arquivo.close()

def menujogadores():

    print('\n\n==============================\n\n - Cadastro de jogadores -\n\n1 - Cadastrar jogador\n2 - Alterar jogador\n3 - Listar jogadores\n4 - Voltar')
    op = input('\nEscolha uma opção: ')

    opcoesmenujogadores(op)

def opcoesmenujogadores(op):
	
    if op == "1":
        gravajogadores(cadjogadores(lejogadores()))
    elif op == "2":
        gravajogadores(editajogadores(lejogadores()))
    elif op == "3":
        listarjogadores()
    elif op == "4":
        menu = True
    else:
        print('ERRO!!! Selecione uma opção válida.')

def lepalavras():
    try:
        arquivo=open("palavras.txt","r")
        lista=arquivo.readlines()
        arquivo.close()
    except:
        lista=[]
    return lista

def cadpalavras(lista):

    palavra=""
    repete=True
    palavra=consiste("Palavra",3,10)
    while repete:
        repete=False
        significado=consiste("Significado",3,50)
        for linha in lista:                    
            listalinha=linha.split(">")
            if listalinha[0] ==(" "+significado+"\n"): repete=True
        if repete: print("Esse significado já existe!")
        lista.append(palavra+" > "+significado+"\n")
    return lista

def excluipalavras(lista):
    palavra=consiste("Palavra",3,10)
    pos=0
    
    for linha in lista:                    
        listalinha=linha.split(" > ")

        #print("TESTE DELEÇÃO: "+listalinha[0]+" - "+palavra+" - "+str(pos))
        
        if listalinha[0]==(palavra):
            print(linha,end="")
            del lista[pos]
            print("\n\nDeletada com sucesso!!!\n\n")
        pos+=1
    return lista

def listarpalavras():
    print('\n\n - Lista de Palavras - \n')

    palavras = open('palavras.txt', 'r')
       
    for linha in palavras:
        print(linha)

    palavras.close()

def sortearpalavra():

    palavras = open('palavras.txt', 'r')
    palavrasarray = []
       
    for linha in palavras:
        palavrasarray.append(linha)

    index = random.randint(0, len(palavrasarray) - 1);
    palavrasorteada = palavrasarray[index]

    palavras.close()

    return palavrasorteada
	
def gravapalavras(lista):
    arquivo=open("palavras.txt","w")
    arquivo.writelines(lista)
    arquivo.close()
        
def menupalavras():

    print('\n\n==============================\n\n - Cadastro de palavras -\n\n1 - Cadastrar palavra\n2 - Excluir palavra\n3 - Listar palavras\n4 - Voltar')
    op = input('\nEscolha uma opção: ')

    opcoesmenupalavras(op)

def opcoesmenupalavras(op):
	
    if op == "1":
        gravapalavras(cadpalavras(lepalavras()))
    elif op == "2":
        gravapalavras(excluipalavras(lepalavras()))
    elif op == "3":
        listarpalavras()
    elif op == "4":
        menu = True
    else:
        print('ERRO!!! Selecione uma opção válida.')

apeljoglogado = ""

def loginjogador(lista):
    apeljog=consiste("Apelido",3,5)
    achou=""
    for linha in lista:                    
        listalinha=linha.split("*")
        if listalinha[1]==(" "+apeljog+"\n"):
            print(listalinha[0])
            achou=apeljog
    return achou

def lelogs():
    try:
        arquivo=open("logs.txt","r")
        lista=arquivo.readlines()
        arquivo.close()
    except:
        lista=[]
    return lista

def gravalogs(lista):

    arquivo=open("logs.txt","w")
    arquivo.writelines(lista)
    arquivo.close()

def cadlog(lista, apelido, log):

    data = log[0]
    hora = log[1]
    conceito = log[2]
    	
    lista.append(data + " > " + hora + " > " + apelido + " > Conceito " + conceito + "\n")
	
    return lista

def jogadas():

    for x in range(100):
        print()

    print("\n\nCOMEÇOU!!!\n\n")

    palavrasorteada = sortearpalavra()
    palavraarray = palavrasorteada.split(" > ")

    palavra = palavraarray[0].lower().strip()
    significado = palavraarray[1]

    print("A dica é: "+ significado +"\n")

    erros = 0
    conceito = 'A'
    quantvogais = 0
    quantconsoantes = 0
    
    vogais = "aeiou"

    for letra in palavra:
            
        if letra.lower() not in vogais:
            quantconsoantes = quantconsoantes + 1

    quantvogais = len(palavra) - quantconsoantes

    palavravogais = palavra

    for letra in palavravogais:

        if letra.lower() not in vogais:
            palavravogais = palavravogais.replace(letra, '*')

    while True:
        tentativa = input("Qual é a palavra? ").lower()

        if(palavra == tentativa):

            if(erros == 0):
                print("\n\n==============================\n        VOCÊ ACERTOU!\n==============================")
                print("       Conceito A!!! \n==============================")

            elif(erros == 1):
                print("\n\n==============================\n        VOCÊ ACERTOU!\n==============================")
                print("       Conceito B!!! \n==============================")

                conceito = 'B'

            elif(erros == 2):
                print("\n\n==============================\n        VOCÊ ACERTOU!\n==============================")
                print("       Conceito C!!! \n==============================")

                conceito = 'C'
            
            break
        
        else:

            erros = erros + 1
            
            if(erros == 1):

                print("\n\nVOCÊ ERROU!!! \n\nA palavra contém " + str(quantvogais) + " vogais e "+ str(quantconsoantes) + " consoantes.")

            elif (erros == 2):

                print("\n\nVOCÊ ERROU!!! \n\nA palavra é "+palavravogais)

            else:

                print("\n\n==============================\n        VOCÊ ERROU!\n==============================")
                print("       Conceito D!!! \n     A palavra é "+ palavra.upper() + "\n==============================")

                conceito = 'D'

                break

    from datetime import datetime
    now = datetime.now()

    data = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute)

    log = [data, hora, conceito]

    return log
	
def iniciarjogo():

    apelido = loginjogador(lejogadores())

    if apelido != "":
        log = jogadas()
        gravalogs(cadlog(lelogs(), apelido, log))
    
    else: print ("JOGADOR NÃO CADASTRADO")    
    
def opcoesmenuprincipal(op):
    if op == "1":
        iniciarjogo()
    elif op == "2":
        menujogadores()
    elif op == "3":
        menupalavras()
    elif op == "4":
        print("\n\nEncerrado...\nAté mais!")
        sys.exit()
    else:
        print('ERRO!!! Selecione uma opção válida.')

menu = True

while(menu):

    print('\n\n==============================\n\n .:: JOGO DA FORCA ::.\n\n1 - Iniciar Jogo\n2 - Cadastro de jogadores\n3 - Cadastro de palavras\n4 - Sair')
    op = input('\nEscolha uma opção: ')

    opcoesmenuprincipal(op)
