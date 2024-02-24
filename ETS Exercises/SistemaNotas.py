lista_alunos = []

with open('./ETS Exercises/dados.txt', 'r') as arquivo_inicial:
    for linha in arquivo_inicial:
        linha = linha.strip()
        linha = linha.split(",")
        print(linha)
        lista_alunos.append(linha)
        
    print(arquivo_inicial.read())
    
print(lista_alunos)    


def calculo_notas(aluno):
    # for aluno in range(len(lista_alunos)):
    final = None
    media = (float(lista_alunos[aluno][1]) + float(lista_alunos[aluno][2]) + float(lista_alunos[aluno][3])) / 3
    print(media)    
    nome = lista_alunos[aluno][0]
    if media >= 7:
        final = "APROVADO"
    else:
        final = "REPROVADO"
    return nome, media, final


with open("./ETS Exercises/dados.processados.txt", "w") as arquivo_final:
    media0 = calculo_notas(0)
    arquivo_final.write(f"{media0[0]} - {media0[1]} - {media0[2]}\n")
    
    media1 = calculo_notas(1)
    arquivo_final.write(f"{media1[0]} - {media1[1]} - {media1[2]}\n")
    
    media2 = calculo_notas(2)
    arquivo_final.write(f"{media2[0]} - {media2[1]} - {media2[2]}\n")
    
    print(f"O(a) aluno(a) {media0[0]} teve média {round(media0[1], 2)} e está {media0[2]}")
    print(f"O(a) aluno(a) {media1[0]} teve média {round(media1[1], 2)} e está {media1[2]}")
    print(f"O(a) aluno(a) {media2[0]} teve média {round(media2[1], 2)} e está {media2[2]}")

print("\n-------------------")    

medias = [calculo_notas(0)[1],calculo_notas(1)[1],calculo_notas(2)[1], ]
maior_media = 0
print(medias)

for i in medias:
    if i > maior_media:
        maior_media = i

print(f"\nA maior média foi: {round(maior_media, 2)}")
        