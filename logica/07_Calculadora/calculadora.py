from cores import *

def menu():
    print("\n" + FRENTE_VERMELHO + "__CALCULADORA__" + RESET)
    print("1 - SOMA")
    print("2 - DIVISÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - SUBTRAÇÃO")
    print("0 - SAIR")

def soma(numero1, numero2):
    return numero1 + numero2

def divisao(numero1, numero2):
    if numero2 == 0:
        return "Erro: não é possível dividir por zero!"
    return numero1 / numero2

def multi(numero1, numero2):
    return numero1 * numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

operador = ""

while operador != "0":
    menu()
    operador = input("Escolha uma opção: ")

    if operador == "0":
        print("Encerrando a calculadora...")
        break

    if operador in ["1", "2", "3", "4"]:
        numero1 = float(input("Informe o número 1: "))
        numero2 = float(input("Informe o número 2: "))

        if operador == "1":
            print("Resultado:", soma(numero1, numero2))
        elif operador == "2":
            print("Resultado:", divisao(numero1, numero2))
        elif operador == "3":
            print("Resultado:", multi(numero1, numero2))
        elif operador == "4":
            print("Resultado:", subtracao(numero1, numero2))
    else:
        print("Opção inválida!")