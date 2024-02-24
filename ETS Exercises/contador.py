# import time

# def contador (a, b, c):
#     print("\n--- CONTADOR ---\n")
    
#     print(f"| INÍCIO: {a} | FIM: {b} | PASSO: {c}\n ")
    
#     if c < 0:
#         for i in range (a, b-1, c):
#             print(i)
            
            
#     else:     
#         for i in range (a, b + 1, c):
#             print(i)
        
        
# def contador_timer(x, y, z):
    
#     if z < 0:
#         print("\nERRO! Tempo não pode ser negativo:")
    
    
#     print("\n--- CONTADOR ---\n")
    
#     print(f"| INÍCIO: {x} | FIM: {y} | PASSO: {z}\n ")
    
#     for i in range (x, y + 1, z):
#         print(i)
#         time.sleep(z)
    
#     print("\n\nCronômetro encerrado.")
               
# contador(1, 21, 1)

# contador(20, 0, -2)

# contador(105, 0, -5)

# contador(96, 52, 2)

# contador(3, 41, 1)

# contador(75, 15, -5)

# contador(390, 10, -10)

# x = int(input("\nDigite de quantos segundos deseja iniciar a contagem\nR: "))

# y = int(input("\nDigite em quantos segundos deseja encerrar a contagem:\nR: "))

# z = int(input("\nDigite de quantos em quantos segundos deseja que o cronômetro conte:\nR: "))

# contador_timer(x, y, z)

import math

def operacoes (a):
        
    factorial = math.factorial(a)
    
    sqr_root = math.sqrt(a)
    
    inverse = 1/a
    
    exp = a**2

    return {"Fatorial" : factorial, "Raiz Quadrada" : sqr_root, "Inverso": inverse, "Potenciação" : exp}

while True:
    
    a = int(input("\nDigite o número que deseja calcular:\nR: "))
    
    operacoes(a)

    result = operacoes(a)
    
    for i in result:
        print(f"\n{i}:{result[i]}\n")
    
    ans_loop = 'a'
    
    while ans_loop not in '12':
        ans_loop = input("Deseja calcular novamente?\n\n[1] Sim\n\n[2] Não\n\nR: ")
        
    if ans_loop == '2': 
        print("\nPrograma encerrado.\n")
        break
        
    
    elif ans_loop == 1:
        continue
    