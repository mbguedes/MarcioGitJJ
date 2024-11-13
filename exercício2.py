def obter_dados():
    nome = input("Digite seu nome: ")
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))
    idade = int(input("Digite sua idade: (Use números reais)"))

    print(f"\nInformações do usuário:")
    print(f"Nome: {nome}")
    print(f"Altura: {altura} metros")
    print(f"Idade: {idade} anos")

obter_dados()