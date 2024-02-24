lista_alunos = []

with open('dados.txt', 'r') as arquivo_inicial:
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
    media = (int(lista_alunos[aluno][1]) + int(lista_alunos[aluno][2]) + int(lista_alunos[aluno][3])) / 3
    print(media)    
    nome = lista_alunos[aluno][0]
    if media >= 7:
        final = "APROVADO"
    else:
        final = "REPROVADO"
    return nome, media, final
 
with open("dados.processados.txt", "w") as arquivo_final:
    media0 = calculo_notas(0)
    arquivo_final.write(f"{media0[0]} - {media0[1]} - {media0[2]}\n")
    
    media1 = calculo_notas(1)
    arquivo_final.write(f"{media1[0]} - {media1[1]} - {media1[2]}\n")
    
    media2 = calculo_notas(2)
    arquivo_final.write(f"{media2[0]} - {media2[1]} - {media2[2]}\n")
    
    
print(f"O(a) aluno(a) {media0[0]} teve média {media0[1]} e está {media0[2]}")

print("\n-------------------")    

if media0[1] > media1[1] and media0[1] > media2[1]:
    maior_media = media0[1]
    
elif media1[1] > media0[1] and media1[1] > media2[1]:
    maior_media = media1[1]

else:
    maior_media = media2[1]
    
print(f"\nA maior média foi: {maior_media}")
        