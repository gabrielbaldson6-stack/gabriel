with open("exame.txt", "r", encoding="utf-8") as arquivo:
    alunos = arquivo.readlines()

for aluno in alunos:
    dados = aluno.strip().split(";")

    nome = dados[0]
    media_anterior = float(dados[1])

    nota_exame = float(input(f"Digite a nota do exame de {nome}: "))

    media_final = (media_anterior + nota_exame) / 2

    if media_final >= 5:
        with open("aprovados.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome}; Média: {media_final:.2f}; Aprovado após exame\n")

        print(f"{nome}: Aprovado após exame")

    else:
        with open("reprovados.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome}; Média: {media_final:.2f}; Reprovado após exame\n")

        print(f"{nome}: Reprovado após exame")