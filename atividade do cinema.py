
while True:
    print("\n===== SISTEMA DE AVALIAÇÃO DO CINEMA =====")
    print("1. Cadastrar avaliação")
    print("2. Listar avaliações")
    print("3. Consultar estatísticas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        idade = int(input("Digite a idade do cliente: "))

        print("Avaliações disponíveis:")
        print("1. Ótimo")
        print("2. Bom")
        print("3. Regular")
        print("4. Péssimo")

        escolha = input("Escolha a avaliação: ")

        if escolha == "1":
            avaliacao = "Ótimo"
        elif escolha == "2":
            avaliacao = "Bom"
        elif escolha == "3":
            avaliacao = "Regular"
        elif escolha == "4":
            avaliacao = "Péssimo"
        else:
            print("Opção inválida!")
            continue

        with open("avaliacoes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{idade};{avaliacao}\n")

        print("Avaliação cadastrada com sucesso!")

    elif opcao == "2":
        print("\n===== AVALIAÇÕES CADASTRADAS =====")

        try:
            with open("avaliacoes.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()

            if len(linhas) == 0:
                print("Nenhuma avaliação cadastrada.")
            else:
                for i, linha in enumerate(linhas, start=1):
                    dados = linha.strip().split(";")

                    idade = dados[0]
                    avaliacao = dados[1]

                    print(
                        f"Cliente {i} - Idade: {idade} "
                        f"- Avaliação: {avaliacao}"
                    )

        except FileNotFoundError:
            print("Nenhuma avaliação cadastrada.")

    elif opcao == "3":
        print("\n===== ESTATÍSTICAS DAS AVALIAÇÕES =====")

        try:
            with open("avaliacoes.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()

            if len(linhas) == 0:
                print("Nenhuma avaliação cadastrada para consultar.")
            else:
                clientes = []

                for linha in linhas:
                    dados = linha.strip().split(";")

                    idade = int(dados[0])
                    avaliacao = dados[1]

                    clientes.append((idade, avaliacao))

                total = len(clientes)

                print(f"Total de respondentes: {total}")

                print("Ótimo:", sum(1 for c in clientes if c[1] == "Ótimo"))
                print("Bom:", sum(1 for c in clientes if c[1] == "Bom"))
                print("Regular:", sum(1 for c in clientes if c[1] == "Regular"))
                print("Péssimo:", sum(1 for c in clientes if c[1] == "Péssimo"))

                mais_velho = max(clientes, key=lambda c: c[0])
                mais_novo = min(clientes, key=lambda c: c[0])

                print("\nRespondente mais velho:")
                print(f"Idade: {mais_velho[0]} anos")
                print(f"Avaliação: {mais_velho[1]}")

                print("\nRespondente mais novo:")
                print(f"Idade: {mais_novo[0]} anos")
                print(f"Avaliação: {mais_novo[1]}")

        except FileNotFoundError:
            print("Nenhuma avaliação cadastrada para consultar.")

    elif opcao == "4":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida! Escolha de 1 a 4.")
