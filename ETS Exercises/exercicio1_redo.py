import re

with open ("clientes.txt", "r") as arquivo:
    texto = arquivo.read()
    lista_nomes = texto.splitlines()

lista_nomes_debugados = []
for nome in lista_nomes:
    nome = re.split(r"[~_!*#$%12-@)\\&(+?.']+",lista_nomes[lista_nomes.index(nome)])
    
    # print(nome) // transforma o nome em uma lista, separando os itens pelos carateres acima
    nome_juntinho = "".join(nome).title()
    # print(nome_juntinho)juna os itens da lista e os coloca numa variavel do tipo str
    # adiciona a variavel em outra lista
    lista_nomes_debugados.append(nome_juntinho)
    # reseta a variavel para o loop continuar
    nome_juntinho = 0
    
print(f'LISTA RECUPERADA:\n')

for i in lista_nomes_debugados:
    print(i)
    
print(f'Total de nomes recuperados: {len(lista_nomes_debugados)}') 