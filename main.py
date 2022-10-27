"""
#Ex1
preco = float(input('Digite o valor do produto: '))
percentual = float(input('Digite o percentual de desconto (0 - 100)%: '))
desconto = preco * (percentual / 100)
valorFinal = preco - desconto
print('O valor do desconto é: {} \n '
      'O valor final do produto é: {}' .format(desconto, valorFinal))

#Ex2
kmPercorrido = int(input('Digite a quantidade de KMs percorridos: '))
diasAlugados = int(input('Qual foi a quantidade de dias alugados? '))
precoKM = kmPercorrido * 0.15
precoDia = diasAlugados * 60
precoTotal = precoKM + precoDia
print('O valor a pagar é: {}' .format(precoTotal))

#Ex3
frase = input('Digite uma frase: ')
tamanhoFrase = len(frase)
frase2 = frase[: tamanhoFrase // 2]
print(frase2[-2 :])

#Ex4
valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))
if(valor1 > valor2):
    print('O primeiro número é maior que o segundo')

#Ex5
valor = int(input('Digite um valor: '))
parImpar = valor % 2
if(parImpar == 0):
    print('O número é par')
else:
    print('O número é ímpar')

#Ex6
materia1 = float(input('Digite a primeira nota: '))
materia2 = float(input('Digite a segunda nota: '))
materia3 = float(input('Digite a terceira nota: '))
media = (materia1 + materia2 + materia3) / 3
print('A média é: {}' .format(media))
if(media >= 7):
    print('O aluno foi aprovado')
else:
    print('O aluno foi reprovado')

#Ex7
maca, laranja, banana = 2.3, 3.6, 1.85
print('Escolha uma opção:\n'
       '1 - Maçã\n'
       '2 - Laranja\n'
       '3 - Banana')
opcao = int(input('Qual sua escolha? '))
if(opcao == 1):
    qtdFrutas = int(input('Digite a quantidade de maçãs: '))
    preco = qtdFrutas * maca
elif(opcao == 2):
    qtdFrutas = int(input('Digite a quantidade de laranjas: '))
    preco = qtdFrutas * laranja
else:
    qtdFrutas = int(input('Digite a quantidade de bananas: '))
    preco = qtdFrutas * banana
print('O valor a pagar é: {}' .format(preco))

#Ex8
nome = input('Digite um nome: ')
idade = int(input('Digite a idade: '))
if(nome == 'Wendel'):
    print('Meu nome é {}, tenho {} anos' .format(nome, idade))
elif(idade < 18):
    print('A pessoa é de menor')
elif(idade > 100):
    print('A pessoa teve uma vida longa')

# Ex9
lado1 = int(input('Digite um valor: '))
lado2 = int(input('Digite outro valor: '))
lado3 = int(input('Digite um terceiro valor: '))
if (lado1 > 0 and lado2 > 0 and lado3 > 0):
    if (lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2):
        if (lado1 == lado2 and lado1 == lado3):
            print("O triângulo é equilátero")
        elif (lado1 != lado2 and lado1 != lado3):
            print('O triângulo é escaleno')
        else:
            print('O triângulo é isósceles')
    else:
        print('Os lados não formam um triângulo')
else:
    print('Os lados não formam um triângulo')

#Ex10
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
print('Escolha uma das operações:\n'
      'Adição\n'
      'Subtração\n'
      'Multiplicação\n'
      'Divisão')
operacao = input('Digite a operação: ')
if(operacao == 'Adição'):
    soma = valor1 + valor2
    print('O resultado da adição é: {}' .format(soma))
elif(operacao == 'Multiplicação'):
    multiplicacao = valor1 * valor2
    print('O resultado da multiplicação é: {}' .format(multiplicacao))
elif(operacao == 'Subtração'):
    if(valor1 > valor2):
        subtracao = valor1 - valor2
        print('O resultado da adição é: {}'.format(subtracao))
    else:
        subtracao = valor2 - valor1
        print('O resultado da adição é: {}'.format(subtracao))
elif(operacao == 'Divisão'):
    if(valor2 != 0):
        divisao = valor1 / valor2
        print('O resultado da adição é: {}'.format(divisao))
    else:
        divisao = valor2 / valor1
        print('O resultado da adição é: {}'.format(divisao))
else:
    print('Operação inexistente!')

# Ex11
kwh = int(input('Digite a quantidade de kwh consumida: '))
print('Qual o tipo de instalação:\n'
      'R - Residência\n'
      'I - Industria\n'
      'C - Comércio')
tipo = input('Digite o tipo de instalação: ')
if(tipo == 'R' or tipo == 'r'):
    if (kwh <= 500):
        preco = 0.4
    else:
        preco = 0.65
elif(tipo == 'I' or tipo == 'i'):
    if (kwh <= 1000):
        preco = 0.55
    else:
        preco = 0.6
elif(tipo == 'C' or tipo == 'c'):
    if (kwh <= 5000):
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Tipo de instalção inválida!')
if(tipo == 'R' or tipo == 'r' or tipo == 'I' or tipo == 'i' or tipo == 'C' or tipo == 'c'):
    print('O preço a pagar é: {}'.format(kwh * preco))
else:
    print('Tipo de instalção inválida!')

#Ex12
limInferior = int(input('Digite o limite inferior: '))
limSuperior = int(input('Digite o limite superior: '))
while(limInferior <= limSuperior):
    if(limInferior % 2 == 0):
        print(limInferior, end=" ")
    limInferior += 1
else:
    print('Fim do while!')

#Ex13
cont = 1
soma = 0
while(cont <= 5):
    nota = float(input('Digite a {}ª nota: ' .format(cont)))
    soma += nota
    cont += 1
media = soma / 5
if(media < 6):
    print('O aluno reprovou, sua média é: {}' .format(media))
else:
    print('O aluno aprovou, sua média é: {}'.format(media))

#Ex14
valor = int(input('Digite um valor: '))
while(valor <= 0):
    print('O valor é negativo ou igual a zero, tente novamente\n'
          'Valor = {}' .format(valor))
    valor = int(input('Digite um valor: '))
else:
    print('O valor é positivo, fim do while\n'
          'Valor = {}'.format(valor))

#Ex15
frase = input('Digite uma frase/palavra: ')
while True:
    print('Você digitou "{}"' .format(frase))
    if(frase == 'sair'):
        print('Você encerrou o programa digitando "{}"'.format(frase))
        break
    else:
        frase = input('Digite outra frase/palavra: ')

#Ex16
while True:
    nome = input('Digite seu nome: ')
    if(nome == 'Wendel'):
        senha = input('Digite sua senha: ')
        if (senha == 'Wendel1234@'):
            print('Acesso Concedido!')
            break
        else:
            print('Senha incorreta, tente novamente!')
            continue
    else:
        print('Nome incorreto, tente novamente!')
        continue

#Ex17
nome = '' #string vazia: False
while not nome: #'not nome' = True
    nome = input('Digite um nome: ') #a variável 'nome' deixa de ser vazia, portanto True e o while vira False
valor = int(input('Digite um valor: '))
if valor: #int ou float != 0: True
    print('Valor diferente de zero!')
else:
    print('Você digitou zero!')

#Ex18
soma = 0
cont = 0
for x in range(1, 101,1):
    if(x % 2 == 0):
        soma += x
        cont += 1
media = soma / cont
print('A média de números pares de 1 à 100 é: {}' .format(media))

#Ex19
cont = 1
tabuada = 1
while(tabuada <= 10):
    print('Tabuada do {}:'.format(tabuada))
    for x in range(1, 11):
        mult = cont
        mult *= x
        print(mult, end = " ")
        if(x == 10):
            print("\n")
    cont += 1
    tabuada += 1

#Ex20
#A)
cont = 3
print("A) While: ")
while(cont <= 12):
    print(cont, end = " ")
    cont += 1

print("\nFor: ")
for x in range(3, 13):
    print(x, end=" ")

#B)
cont1 = 0
print("\n\nB) While: ")
while(cont1 < 9):
    print(cont1, end = " ")
    cont1 += 2

print("\nFor: ")
for x in range(0, 9,2):
    print(x, end=" ")

#Ex21
print('Qual opção você deseja fazer?\n'
      '1 - Soma\n'
      '2 - Subtração\n'
      '3 - Multiplicação\n'
      '4 - Divisão\n'
      '5 - Sair')
while True:
    opcao = int(input('Digite uma opção: '))
    if(opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5):
        print('\nVocê digitou uma opção inválida!\n'
              'Tente novamente!\n')
        continue
    elif(opcao == 5):
        print('Você saiu!')
        break
    else:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
        if(opcao == 1):
            soma = valor1 + valor2
            print('O resultado da soma é: {}\n'.format(soma))
        elif(opcao == 2):
            subtracao = valor1 - valor2
            print('O resultado da subtração é: {}\n'.format(subtracao))
        elif(opcao == 3):
            multiplicacao = valor1 * valor2
            print('O resultado da multiplicação é: {}\n'.format(multiplicacao))
        else:
            divisao = valor1 / valor2
            print('O resultado da divisão é: {}\n'.format(divisao))

#Ex22
while True:
    valor = int(input('Digite um valor: \n'))
    if (valor > 0):
        # R$100
        cedula100 = valor // 100
        valor -= cedula100 * 100
        # R$50
        cedula50 = valor // 50
        valor -= cedula50 * 50
        # R$20
        cedula20 = valor // 20
        valor -= cedula20 * 20
        # R$10
        cedula10 = valor // 10
        valor -= cedula10 * 10
        # R$5
        cedula5 = valor // 5
        valor -= cedula5 * 5
        # R$1
        cedula1 = valor
        print('Cédula de R$100: {}\n'
              'Cédula de R$50: {}\n'
              'Cédula de R$20: {}\n'
              'Cédula de R$10: {}\n'
              'Cédula de R$5: {}\n'
              'Cédula de R$1: {}\n'.format(cedula100, cedula50, cedula20, cedula10, cedula5, cedula1))
    elif(valor < 0):
        print('Você digitou uma opção inválida!\n'
              'Tente novamente!')
        continue
    else:
        print('Você saiu!')
        break

#Ex23
opcao = ''
somaIdade = 0
mediaIdade = 0
totalPessoas = 0
totalArrecadado = 0
print('Escolha uma opção:\n'
      'Consultar valor do ingresso:\n'
      'Sair')
while True:
    opcao = input('Digite sua opção: ')
    if(opcao == 'consultar'):
        idade = int(input('Digite sua idade: '))
        if(idade < 3):
            preco = 0
        elif(idade <= 12):
            preco = 15
        else:
            preco = 30
        totalPessoas += 1
        totalArrecadado += preco
        somaIdade += idade
        mediaIdade = somaIdade / totalPessoas
    elif(opcao == 'sair'):
        print('Você saiu!\n')
        print('Total de Pessoas: {}\n'
              'Total Arrecadado: {}\n'
              'Média das Idades: {:.2f}' .format(totalPessoas, totalArrecadado, mediaIdade))
        break
    else:
        print('Opção inválida!\n'
              'Tente novamente!')
        continue

#Ex24
def soma(x, y, z):
    soma = x + y + z
    print(soma)
def soma(x = 0, y = 0, z = 0):
    soma = x + y + z
    print(soma)
soma(1, 2, 3)
soma(1, 2)
soma(1)
soma()

#Ex25
def destacarFrase(frase):
    tamanhoFrase = len(frase)
    print('+' + '-' * tamanhoFrase + '+\n'
          '|' + frase + '|\n'
          '+' + '-' * tamanhoFrase + '+')
destacarFrase('Teste do Exercício')

#Ex26
def validar(frase, valorMin, valorMax):
    tamanhoFrase = len(frase)
    if(tamanhoFrase >= valorMin and tamanhoFrase <= valorMax):
        return frase
    else:
        return 'O tamanho da frase não está dentro do intervalo!'
print(validar('Wendel Tavares', 1, 10))

#Ex27
def soma(x = 0, y = 0):
    '''
    Função que retorna o somatório de até 2 valores numéricos quaisquer.
    Todos os parâmetros são opcionais.

    :param x: valor numérico opcional
    :param y: valor numérico opcional
    :return: retorna a soma dos parâmetros
    '''
    return x + y
print(soma(2, 3))
help(soma)

#Ex28
global num
def fatorial(num, valida):
    '''
    Função que calcula o fatorial de um número qualquer, através da variável 'num'.
    Antes disso há uma validação para ver se o número digitado é maior que zero, através da outra função 'validar'.
    :param num: número positivo
    :param valida: função que faz a validação
    :return: retorna o número se positivo
    '''
    if(valida(num)):
        fat = 1
        for x in range(1, num + 1):
            fat *= x
        return '\nCalculando Fatorial...\n' \
               '{}! = {}'.format(num, fat)
    else:
        return 'Valor inválido!'
def validar(num):
    if(num >= 0):
        return True
print('Escolha uma opção:\n'
      '1 - Calcular Fatorial\n'
      '2 - Sair')
while True:
    opcao = int(input('\nDigite uma opção: '))
    if(opcao == 1):
        x = int(input('Digite um número: '))
        print(fatorial(x, validar))
        continue
    elif(opcao == 2):
        print(('Você saiu!'))
        break
    else:
        print('Opção inválida3!')
#help(fatorial)

#Ex29
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

#Ex30
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')

print(mochila[-2:])
print(mochila[0])
print(mochila[1:3])

for item in mochila:
    print('Minha mochila tem: {}'.format(item))

tam = len(mochila)
for item in range(0, tam):
    print('Minha mochila tem: {}'.format(mochila[item]))

def soma(*num): # O '*' pega todos os dados passados como parâmetros e joga na variável 'num'. Transformando 'num' em uma tupla
    somar = 0
    print('Tupla: {}'.format(num))
    for dados in num:
        somar += dados
    return somar
print('Resultado: {}\n'.format(soma(1, 2, 3))) # Podemos passar infinitos parâmetros na função 'soma'
print('Resultado: {}'.format(soma(1, 2, 3, 4, 5, 6)))"""

#Ex31
"""mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista:', mochila)

mochila[2] = 'Laranja'
print('Lista:', mochila)

mochila.append('Ovos') # Adiciona um dado no final da lista
print('Lista:', mochila)

mochila.insert(1, 'Canivete') # Adiciona um dado em determinada posição
print('Lista:', mochila)

print(mochila[-2:])
print(mochila[2:6])
print(mochila[3:])

del mochila[5] # Exclui um dado em determinada posição
print('Lista: ', mochila)

mochila.remove('Canivete') # Exclui um determindado dado independente de sua posição
print('Lista: ', mochila)

x = [5, 7, 9, 11]
y = x # Faz como que as 2 variáveis ocupem o "mesmo espaço" de memória, possuindo os mesmos valores
print(x)
print(y)

y[0] = 2 # Modifica as 2 listas
print(x)
print(y)

x = [5, 7, 9, 11]
y = x[:] # Cria uma cópia da lista "x"
print(x)
print(y)

y[0] = 2 # Modifica somente a lista "y"
print(x)
print(y)"""

#Ex32
"""mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[1][-3:]) # Dupla Indexação: 1º índice é referente ao item da lista, já o 2º se refere ao caracter da string

for item in mochila:
    for letra in item:
        print(letra, end = '')
    print()

for i in range(0, len(mochila)):
    for j in range(0, len(mochila[i])):
        print(mochila[i][j], end = '')
    print()

mochila = [['Cebola', 0.39], ['Tomate', 0.49], ['Maçã', 0.89]]
print(mochila[0][0])
for item1 in mochila:
    for item2 in item1:
        print(item2, end=' ')
    print()

item = []
mercado = []
for x in range(3):
    item.append(input('Digite o nome do produto: '))
    item.append(int(input('Digite a quantidade comprada: ')))
    item.append(float(input('Digite o valor unitário do produto: ')))
    mercado.append(item[:])
    item.clear()
print(mercado)

mercado = []
soma = 0
for x in range(3):
    nome = input('Digite um nome: ')
    qtd = int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor unitário: '))
    mercado.append([nome, qtd, valor])
for item in mercado:
    print('| Produto | Quantidade | Valor Unitário | Valor Final |\n'
          '|   {}    |     {}     |       {}       |      {}     |\n'.format(item[0], item[1], item[2],item[1] * item[2]))
    soma += (item[1] * item[2])
print('Total a pagar: {}'.format(soma))

#Ex33
linguagens = ('Rust', 'TypeScript', 'Python', 'Kotlin', 'Go', 'Julia', 'Dart', 'C#', 'Swift', 'JavaScript')
for dados in range(0, len(linguagens)):
    print(dados + 1,end = ': ' + linguagens[dados] + '\n')
print(linguagens[:3])
print(linguagens[-5:])
cont = 0
while(linguagens[cont] != 'Python'):
    cont += 1
print('Python está na {}ª posição das linguagens mais amadas'.format(cont + 1))

#Ex34
def maiorNumero(mensagem, *nums):
    maior = 0
    for maiorNum in range(0, len(nums)):
        if(nums[maiorNum] > maior):
            maior = nums[maiorNum]
    print(mensagem, maior)
maiorNumero('Maior número:',5,1,4,2,9,10)

#Ex35
try:
    listaNota = []
    cont = 0
    soma = 0
    nota = 0
    while True:
        cont += 1
        nota = float(input('Digite {}ª nota: '.format(cont)))
        if (nota < 0):
            print('Valor inválido!\n'
                  'O programa encerrou...')
            break
        listaNota.append(nota)
        soma += nota
        media = soma / cont
    print('Lista: ', listaNota)
    print('A média das notas é: {}'.format(media))
except ZeroDivisionError:
    print('Digite uma nota válida!')

#Ex36
def buscar(lista, dado):
    try:
        global cont
        cont = 0
        while(lista[cont] != dado):
            cont += 1
        if(lista[cont] == dado):
            return cont
    except:
        return -1
dado = input('Digite uma cor: ')
cor = ['Amarelo', 'Azul', 'Vermelho', 'Verde']
if(buscar(cor, dado) >= 0 ):
    print('O índice que o dado "{}" foi encontrado é: {}'.format(dado, cont))
else:
    print('Dado não encontrado!')"""

#Ex37
try:
    lista = []
    imc = lambda peso, altura: peso / (altura ** 2)
    while True:
        nome = input('Digite o seu nome: ')
        peso = float(input('Digite o seu peso: '))
        altura = float(input('Digite a sua altura: '))
        lista.append([nome, peso, altura, imc(peso, altura)])
        continuar = input('Deseja continuar? (S/N) ')
        if(continuar in 'Nn'):
            break
    maior = 0
    menor = 99
    totalCad = len(lista)
    for item in lista:
        if(item[3] >= maior):
            maior = item[3]
        if(item[3] < menor):
            menor = item[3]
    print(lista)
    print('Total de Cadastros: {}\n'
          'Maior IMC: {:.2f}\n'
          'Menor IMC: {:.2f}'.format(totalCad, maior, menor))
except:
    print('Deu ruim!')