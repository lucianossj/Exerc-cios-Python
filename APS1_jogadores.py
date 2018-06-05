import sys

menu = True

def opcoesMenu(op):
	
	if op == "1":
		cadastroJogador()
	elif op == "2":
		delecaoJogador()
	elif op == "3":
		listarJogadores()
	elif op == "4":
		sair()
	else:
		erroMenu()

def cadastroJogador():
	print('\n\n.:: Cadastrar Jogador ::.')
	nome = input('Qual o nome do Jogador? - ')
	apelido = input('Qual o apelido do Jogador? - ')

	cadastrarJogador(nome, apelido)

def delecaoJogador():
	print('\n\n.:: Deletar Jogador ::.')
	apelido = input("Qual o apelido do Jogador que deseja deletar? - ")

	pesquisarJogador(apelido)

def listarJogadores():
    print('\n\n.:: Lista de Jogadores ::.\n')

    jogadores = open('jogadores.txt', 'r')
       
    for linha in jogadores:
        print(linha)

    jogadores.close()

def sair():
	print("\n\nEncerrado...\nAté mais!")
	sys.exit()
	
def erroMenu():
	print('ERRO!!! Selecione um opção válida.')

def cadastrarJogador(nome, apelido):

    jogadores = open('jogadores.txt', 'r')
    conteudo = jogadores.readlines()
    jogador = '\n' + nome + ' > ' + apelido
    conteudo.append(jogador)

    jogadores = open('jogadores.txt', 'w')
    jogadores.writelines(conteudo)

    jogadores.close()

    print('\n\nJogador cadastrado com sucesso!!!\n\n')

def pesquisarJogador(apelido):
    with open('jogadores.txt','r') as f:
        conteudo = f.readlines()
    for i in conteudo:
        if apelido in i:
                print(i)
                deletarJogadorArquivo(i.index)
                print('\n\nJogador removido com sucesso!!!\n\n')
                return
    print('\n\nERRO!!!Jogador não encontrado.\n')

def deletarJogadorArquivo(linhaRemocao):
    with open('jogadores.txt', 'r') as f:
    	conteudo = f.readlines()
    with open('jogadores.txt', 'w') as f:
    	for i in conteudo:
    		if conteudo.index(i) == linhaRemocao:
    			f.write('')
    		else:
    			f.write(i)

while(menu):

    print('\n .:: APS1 ::.\n1 - Cadastrar jogador\n2 - Deletar jogador\n3 - Listar jogadores\n4- Sair')
    op = input('\nEscolha uma opção: ')

    opcoesMenu(op)
 
