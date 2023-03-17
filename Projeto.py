somaMedia = 0
count = 0
apr = 0
rep = 0
rec = 0
for x in range (1,7):
    nota1 = float(input("\nDigite a primeira nota do aluno {}: ".format(x)))
    nota2 = float(input("\nDigite a segunda nota do aluno {}: ".format(x)))
    somaNota = nota1 + nota2
    mediaNota = somaNota / 2
    somaMedia += mediaNota
    print("\nA média do aluno {} é: {}".format(x, mediaNota))
    if(mediaNota < 3):
        print("\nO aluno foi Reprovado")
        rep += 1
    elif(mediaNota < 7):
        print("\nO aluno está em Recuperação")
        rec += 1
    else:
        print("\nO aluno foi Aprovado")
        apr += 1
    count += 1
print("\nO total de alunos aprovados é: {}\n"
      "O total de alunos em Recuperação é: {}\n"
      "O total de alunos Reprovados é: {}".format(apr, rec, rep))
mediaTurma = somaMedia / count
print("\nA média da classe é: ",mediaTurma)
