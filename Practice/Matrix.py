vertical = int(input("Digite a altura que deseja na matriz:\n\nR: "))
horizontal = int(input("\nDigite a largura que deseja na matriz:\n\nR: "))

for i in range(vertical):
    print('\n   ')
    for j in range(horizontal):
        print("X", end='     ')