import os

caminho_arquivo = "tarefas.txt"

# Ler tarefas do arquivo, se existir
if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        listaTarefas = [linha.strip() for linha in f.readlines()]
else:
    listaTarefas = []


def mostrar_lista(lista):
    if lista:
        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}- {tarefa}")
    else:
        print("Nenhuma tarefa cadastrada.")


entradaUm = int(input("Você quer:\n"
                      "1- Adicionar uma tarefa\n"
                      "2- Remover uma tarefa\n"
                      "3- Ver todas as tarefas\n"))


salvar = False  # flag para saber se precisa salvar


if entradaUm == 1:
    tarefa = input("Qual tarefa você quer adicionar? ")
    listaTarefas.append(tarefa)
    print("Tarefa adicionada! Segue nova lista: ")
    mostrar_lista(listaTarefas)
    salvar = True


if entradaUm == 2:
    for i, tarefa in enumerate(listaTarefas, start=1):
        print(f"{i}- {tarefa}")

    numero = int(input("Digite o número da tarefa que você quer remover: "))

    if 1 <= numero <= len(listaTarefas):
        listaTarefas.pop(numero - 1)  
        print("Tarefa removida! Segue nova lista: ")
        mostrar_lista(listaTarefas)
        salvar = True
    else:
        print("Número inválido.")

if entradaUm == 3:
    mostrar_lista(listaTarefas)


# Só salva se adicionou ou removeu
if salvar:
    with open(caminho_arquivo, "w") as f:
        for tarefa in listaTarefas:
            f.write(tarefa + "\n")