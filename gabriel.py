
# Cadastro das notas dos alunos

with open("notas.txt", "a", encoding="utf-8") as arquivo:
    while True:
        nome = input("Digite o nome do aluno: ")

        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        nota3 = float(input("Digite a nota 3: "))

        arquivo.write(f"{nome};{nota1};{nota2};{nota3}\n")

        continuar = input("Deseja cadastrar outro aluno? (s/n): ")

        if continuar.lower() != "s":
            break

print("Notas salvas com sucesso!")
