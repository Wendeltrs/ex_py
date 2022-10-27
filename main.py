def existeArquivo(arquivo):
    try:
        verifica = open(arquivo, 'rt')
        verifica.close()
    except:
        return False
    else:
        return True

def criarArquivo(arquivo):
    try:
        criar = open(arquivo, 'wt+')
        criar.close()
    except:
        print('Erro ao criar um novo arquivo!')
    else:
        print('Arquivo {} criado com sucesso!'.format(arquivo))

def cadastrar(arquivo, nome, console):
    try:
        cadastrar = open(arquivo, 'at')
    except:
        print('Erro ao realizar o cadastro!')
    else:
        while True:
            continuar = input('Deseja continuar? (S/N)')
            if(continuar == 'S'):
                cadastrar.write('{} '.format(nome) + '{}\n'.format(console))
                nome = input('Digite o nome do jogo: ')
                console = input('Digite o console do jogo: ')
                continue
            elif(continuar == 'N'):
                cadastrar.write('{} '.format(nome) + '{}\n'.format(console))
                break
            else:
                print('Valor inválido!')
    finally:
        cadastrar.close()

def listar(arquivo):
    try:
        listar = open(arquivo, 'rt')
    except:
        print('Erro ao listar o arquivo!')
    else:
        #listar.read()
        cont = 0
        for dados in listar.readlines():
            cont += 1
            print(cont, end = ':' + dados)
    finally:
        listar.close()

def menu():
    print('Escolha uma opção:\n'
          '1 - Cadastrar nome e console\n'
          '2 - Listar\n'
          '3 - Sair')

arquivo = input('Digite o nome do arquivo: ')
if(existeArquivo(arquivo)):
    print('O arquivo foi localizado!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arquivo)
while True:
    menu()
    opcao = int(input('\nDigite uma opção: '))
    if(opcao == 1):
        nome = input('Digite o nome do jogo: ')
        console = input('Digite o console do jogo: ')
        cadastrar(arquivo, nome, console)
    elif(opcao == 2):
        listar(arquivo)
    elif(opcao == 3):
        print('Você saiu!')
        break
    else:
        print('Opção inválida!')
