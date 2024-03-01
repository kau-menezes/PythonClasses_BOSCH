import argparse

parser = argparse.ArgumentParser(description='Verificação de Palavras Distintas!')

parser.add_argument('--file ', action='store' , dest='file_path', required='True', help='Digite o nome do arquivo que deseja verificar.' )

parser.add_argument('--word_to_be_searched ', action='store' , dest='word', required='True', help='Digite a palavra que deseja verificar.' )

arguments = parser.parse_args()

arquivo = arguments.file_path
palavra = arguments.word

with open(arquivo, "w+") as arquivo:
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
                    
print(f'\nExistem "{contador}" palavras distintas nessa frase.')

count = 0

for palavras in range(len(palavras_usuario)):
    if palavra == palavras_usuario[palavras]:
        count+= 1

print(f'\nA palavra: "{palavra}" aparece {count} vezes no texto.')