# ela é chique

class Calc:
    def __init__(self):
        while True:
            try:
                self.num1 = int(input("Digite o número 1: "))
                self.num2 = int(input("Digite o número 2: "))
                break
            except ValueError:
                print("\nPor favor, digite um número!!")

    def Sum(self):
        result = self.num1 + self.num2
        print(f"\nA soma é {result}")
        return result
    
    def Subtraction(self):
        result = self.num1 - self.num2
        print(f"\nA diferença é de {result}")
        return result
    
    def Multiplication(self):
        result = self.num1 * self.num2
        print(f"\nO produto é {result}")
        return result 
    
    def Division(self):
        result = self.num1 / self.num2
        print(f"\nO resultado da divisão é {result}")
        return result
    
class Scientific_Calc(Calc):
    def __init__(self):
        super().__init__()
        
    def SqrRoot(self):
        result1 = self.num1 ** 2
        result2 = self.num2 ** 2
        print(f"\nO primeiro número elevado ao quadrado é {result1} e o segundo elevado ao quadrado é {result2}")
        return result1, result2
    
class Error (Exception):
    pass

calc= Calc()

try: 
    op = int(input("\nDigite a operação que deseja realizar.\n\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Potenciação\nR: "))
    
    if op < 1 or op > 6:
        raise Error

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