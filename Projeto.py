nota1 = 0
nota2 = 0
media_a = 0
soma_a = 0
media_c = 0
soma_c = 0
count_c = 0
apr = 0
rep = 0
rec = 0
for x in range (1,7):
    nota1 = float(input("\nDigite a primeira nota do aluno "+str(x)+": "))
    nota2 = float(input("\nDigite a segunda nota do aluno "+str(x)+": "))
    soma_a = nota1 + nota2
    media_a = soma_a / 2
    soma_c += media_a
    print("\nA média do aluno ",x," é: ",media_a)
    if(media_a < 3):
        print("\nO aluno foi Reprovado")
        rep += 1
    elif(media_a < 7):
        print("\nO aluno está em Recuperação")
        rec += 1
    else:
        print("\nO aluno foi Aprovado")
        apr += 1
    count_c += 1
print("\nO total de alunos aprovados é: ",apr)
print("\nO total de alunos em Recuperação é: ",rec)
print("\nO total de alunos Reprovados é: ",rep)
media_c = soma_c / count_c
print("\nA média da classe é: ",media_c)