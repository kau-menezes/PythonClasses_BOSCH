lista = []

with open("texto_escrito.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        print(linha)
        linha = linha.split(" ")
        print(linha)
        
        # PARA CRIAR UMA LISTA SOMENTE COM OS ITENS:
        
        lista = lista + linha
        print(lista)
        
        # PARA CRIAR UMA LISTA DE LISTAS:
        
        # lista.append(linha)
        # print(lista)