#Calc simples em py


def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero!"
    return num1 / num2

def main():
    print("Bem-vindo à Calculadora!")
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    operacao = input("Digite o número da operação desejada (1/2/3/4): ")

    if operacao in ['1', '2', '3', '4']:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            resultado = somar(numero1