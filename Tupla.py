def maiorValor(msg, *num):
    maior = 0
    for dados in num:
        if dados > maior:
            maior = dados
    print(msg, maior)
maiorValor('O maior valor é:',2,6,9,12,16,50,20,22,24,25)