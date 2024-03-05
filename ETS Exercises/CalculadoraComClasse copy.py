# ela é chique
while True:
            try:
                num1 = int(input("Digite o número 1: "))
                num2 = int(input("Digite o número 2: "))
                break
            except ValueError:
                print("\nPor favor, digite um número!\n")

class Calc:
    def Sum(self):
        result = num1 + num2
        print(f"A soma é {result}")
        return result
    
    def Subtraction(self):
        result = num1 - num2
        print(f"A diferença é de {result}")
        return result
    
    def Multiplication(self):
        result = num1 * num2
        print(f"O produto é {result}")
        return result 
    
    def Division(self):
        result = num1 / num2
        print(f"O resultado da divisão é {result}")
        return result
    
class Scientific_Calc(Calc):
    def SqrRoot(self):
        result1 = num1 ** 2
        result2 = num2 ** 2
        print(f"O primeiro número elevado ao quadrado é {result1} e o segundo elevado ao quadrado é {result2}")
        return result1, result2
    
class Error (Exception):
    print("Digite uma opção válida")
    pass

calc= Calc()

while True:
    try: 
        op = int(input("\nDigite a operação que deseja realizar.\n\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Potenciação\n\nR: "))

        if op < 1 or op > 6:
            raise Error
            pass
        
        else:
            break

    except ValueError:
        print("Digite uma das opções acima.")
    
if op == 1:
    calc.Sum()
    
elif op == 2:
    calc.Subtraction()
    
elif op == 3:
    calc.Multiplication()
    
elif op == 4:
    calc.Division()
    
elif op == 5:
    calculadora = Scientific_Calc()
    calculadora.SqrRoot()