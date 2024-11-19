def verificarTime(numero):
    if numero % 2 == 0:
        print("Você está no time azul")
    else:
        print("Você está no time amarelo")


numero_usuario = int(input("Digite um número: "))
verificarTime(numero_usuario)
