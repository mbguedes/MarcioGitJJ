def exibir_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    print("Bem-vindo ao programa de tabuada!")
    numero = int(input("Digite o número para ver a tabuada: "))
    exibir_tabuada(numero)

main()