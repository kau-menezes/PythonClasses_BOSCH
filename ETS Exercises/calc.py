
def game():
        n1= int(input("\nDigite o primeiro número:\nR: "))

        n2= int(input("\nDigite o segundo número:\nR: "))

        operator = int(input("Selecione a operação que deseja realizar:\n\n[1] Adição\n\n[2] Subtração\n\n[3] Multipicaçãp\n\n[4] Divisão\n\nR: "))
        result = 0
            
        if operator == 1:
            result = n1 + n2
            print(f"O resultado é {result}")
            
                
        elif operator == 2:
            result = n1 - n2
            print(f"O resultado é {result}")
            
            
        elif operator ==3:
            result = n1 * n2
            print(f"O resultado é {result}")
            
            
        elif operator == 4:
            result = n1 / n2
            print(f"O resultado é {result}")
            
            
        else:
            print("Por favor, digite uma opção válida\n")

while True:
    
    game()
    
    answer = int(input("Deseja realizar uma nova conta?\n\n[1] Sim\n\n[2] Não\n\nR: "))

    if answer == 1: 
        game()
        
    else:
        print("\nn\Programa encerrado.")
        break        