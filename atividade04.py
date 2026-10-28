arquivos = ["aprovados.txt", "reprovados.txt"]

for nome_arquivo in arquivos:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        alunos = arquivo.readlines()

    print(f"\n--- {nome_arquivo.upper()} ---")

    for aluno in alunos:
        print(aluno.strip())