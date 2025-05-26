lista = []
sair = "nao"

while sair == "nao":
    print("Deseja adicionar um item na lista?")
    resposta1 = input("sim ou nao: ")
    if resposta1 == "sim":
        item = input("Digite o nome do item a ser adicionado: ")
        lista.append(item)
        print("Lista atual:", lista)
    else:
        print("Deseja excluir um item da lista?")
        resposta2 = input("sim ou nao: ")
        if resposta2 == "sim":
            item = input("Digite o nome do item a ser removido: ")
            if item in lista:
                lista.remove(item)
                print("Lista atual:", lista)
            else:
                print("Item não encontrado na lista.")
        else:
            print("Deseja finalizar?")
            sair = input("sim ou nao: ")
print("Programa finalizado. Lista final:", lista)