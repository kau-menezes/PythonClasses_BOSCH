while True:
    print('\n### CALCULADORA! ###')
    print("Digite dois números diferentes de zero.")
    
    try:  
        num1 = float(input('\nPrimeiro número:\nR: '))
        num2 = float(input('\nSegundo número:\nR: '))
        break   
    except ValueError:
        print('\nFavor digitar dois números!\n')
            
    
print('\n\nDigite a opção da operação que deseja realizar:\n\n[1] Adição\n\n[2] Subtração\n\n[3] Multiplicação\n\n[4] Divisão\n')  
choice = int(input('\nR: '))   
    
def operacoes(choice):
    global num1
    global num2
    sinal = None
    
    try:
        if choice == 1:
            resultado = num1+num2
            sinal = "+"
    
        if choice == 2:
            resultado = num1-num2
            sinal = "-"
            
        if choice == 3:
            resultado = num1*num2
            sinal = "*"
            
        if choice == 4:
            resultado = num1/num2
            sinal = "/"
            
        if choice > 4 or choice < 0:
            raise Exception("\n\nDigite uma opção válida!")
                
    except ZeroDivisionError:
        print('Não é possível realizar uma divisão por zero!')
            
        try:
            num2 =  num2 = float(input('\nSegundo número:\nR: '))
            resultado = num1/num2
        except ValueError:
            print('\nFavor digitar um número!!!\n')
            
    return  resultado, sinal
            
operacoes(choice)
print(f'\n### RESULTADO ###\n\n{num1} {operacoes(choice)[1]} {num2} = {operacoes(choice)[0]}')
    
while True:
    try:
        answer = int(input('\n\nDeseja realizar uma nova conta?\n\n[1] Sim \n\n[2] Não\n\nR: '))
        if answer == 1:
            continue
            break
        
        elif answer ==2:
            print('\nPrograma encerrado.')
            break
                
    except ValueError:
        print("Favor, digite uma das opções acima!")