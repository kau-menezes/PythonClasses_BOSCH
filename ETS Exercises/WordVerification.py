# trocar o local de abertura e escrita do arquivo nas linhas 3 e 18

with open("./ETS Exercises/texto_escrito.txt", "w+") as arquivo:
    texto_usuario = input("Escreva o texto que deseja verificar.\n\nR: ")
    arquivo.write(texto_usuario)

palavras_usuario = texto_usuario.split(" ")
contador = 0
palavras_distintas = []

for palavras in range(len(palavras_usuario)):
    for words in range(len(palavras_usuario)): 
            if palavras_usuario[palavras] != palavras_usuario[words]:
                if not palavras_usuario[palavras] in palavras_distintas:
                    palavras_distintas.append(palavras_usuario[palavras])
                    contador+=1

with open("./ETS Exercises/palavras_distintas.txt", "w+") as arquivo:
    palavras_distintas = "\n".join(palavras_distintas) 
    arquivo.write(palavras_distintas)

print(f'\nExistem "{contador}" palavras distintas nessa frase.')

count = 0

palavra_usuario = input("\nDigite a palavra que deseja verificar.\n\nR: ")

for palavras in range(len(palavras_usuario)):
    if palavra_usuario == palavras_usuario[palavras]:
        count+= 1

print(f"\nA palavra: {palavra_usuario} aparece {count} vezes no texto.")
