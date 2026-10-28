
# Leitura das notas e classificação dos alunos

with open("notas.txt", "r", encoding="utf-8") as arquivo:
    alunos = arquivo.readlines()

with open("aprovados.txt", "w", encoding="utf-8") as aprovados, \
     open("exame.txt", "w", encoding="utf-8") as exame, \
     open("reprovados.txt", "w", encoding="utf-8") as reprovados:

    for linha in alunos:
        dados = linha.strip().split(";")

        nome = dados[0]
        nota1 = float(dados[1])
        nota2 = float(dados[2])
        nota3 = float(dados[3])

        media = (nota1 + nota2 + nota3) / 3

        resultado = (
            f"Aluno: {nome} | "
            f"Notas: {nota1}, {nota2}, {nota3} | "
            f"Media: {media:.2f}\n"
        )

        if media >= 7:
            aprovados.write(resultado)

        elif media >= 5:
            exame.write(resultado)

        else:
            reprovados.write(resultado)

print("Classificacao concluida!")
print("Consulte os arquivos gerados.")
