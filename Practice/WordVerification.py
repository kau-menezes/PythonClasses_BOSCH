with open("texto_escrito.txt", "w+") as arquivo:
    texto_usuario = input("Escreva o texto que deseja verificar.\n\nR: ")
    arquivo.write(texto_usuario)

palavras_usuario = texto_usuario.split(" ")
contador = 0
palavras_distintas = []

for palavras in range(len(palavras_usuario)):
    for words in range(len(palavras_usuario)): 
            if palavras_usuario[palavras] != palavras_usuario[words]:
                #  if palavras_usuario[palavras] in ...


                 palavras_distintas.append(palavras_usuario[palavras])
                 contador+=1

print(contador)
print(palavras_distintas)