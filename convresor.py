numero_usuario = input("Digite o número a ser convertido.\n\nR: ")

# dicionario_binario = {

#     "0" : "00110000", 
#     "1" : "00110001",
#     "2" : "00110010",
#     "3" : "00110011",
#     "4" : "00110100",
#     "5" : "00110101",
#     "6" : "00110110", 
#     "7" : "00110111", 
#     "8" : "00111000",
#     "9" : "00111001"
# }

lista_binario = [["0", "00110000"], ["1", "00110001"], ["2", "00110010"], ["3", "00110011"], ["4", "00110100"], ["5", "00110101"], ["6", "00110110"], ["7", "00110111"], ["8", "00111000"], ["9", "00111001"]  ]

algarismos = []

for i in numero_usuario:
    algarismos.append(i)

# print(algarismos)  

for algarismo in range(len(algarismos)):
    for numeros in range(len(lista_binario)):
        if algarismos[algarismo] == lista_binario[numeros][0]:
            algarismos[algarismo] = lista_binario[numeros][1]

# print(algarismos)

# print(f"O número convertido é: {''.join(algarismos)}")

print("O número convertido é:")

for i in algarismos:
    print(i, end=" ")

