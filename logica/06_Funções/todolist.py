from cores import *

tarefas = []

def menu():
    print ("\n" + FRENTE_AMARELO + "__MENU__" + RESET)
    print ("1- Adicionar tarefa")
    print ("2- Listar Tarefas")
    print ("3- Remover tarefa")
    print ("4 - Sair")

def adicoinarTarefa():
    tarefa = input("Digite o nome da tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa Adicionada!")

def listarTarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada")
    else:
        for numero, tarefa in enumerate(tarefas, start=1):
            print(numero, "-", tarefa)

def removerTarefa():
    listarTarefas()

    if len(tarefas) > 0:
        numero = int(input("Digite o número da tarefa a remover: "))

        if 1 <= numero <= len(tarefas):
            tarefas.pop(numero- 1)
            print("Tarefa removida!")
        else:
            print("número inválido")

opcao = ""

while opcao != "4":
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicoinarTarefa()
    elif opcao == "2":
        listarTarefas()
    elif opcao == "3":
        removerTarefa()
    elif opcao == 4:
        print ("Até logo!")
    else:
        print("Opção inválida!")