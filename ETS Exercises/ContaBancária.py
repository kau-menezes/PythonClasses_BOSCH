class Conta:
    def __init__(self, numero, agencia):
        self.numero = int(input("Digite o número da conta: "))
        self.agencia = int(input("Digite a agência da conta: "))
        print("NUMERO" + self.numero)
        print("AGENCIA" + self.agencia)
    
    def ContaCriada():
        print("Conta Criada!")
        
    def Tipo():
        pass
    
class Poupança(Conta):
    def __init__(self, numero, agencia):
        super().__init__(numero, agencia)
        
    def Tipo():
        super().ContaCriada()
        print("Tipo: POUPANÇA")
    
class Corrente(Conta):
    def __init__(self, numero, agencia):
        super().__init__(numero, agencia)
        
    def Tipo():
        super().ContaCriada()
        print("Tipo: CORRENTE")
    
class Salario(Conta):
    def __init__(self, numero, agencia):
        super().__init__(numero, agencia)
        
    def Tipo():
        super().ContaCriada()
        print("Tipo: SALÁRIO")
        
# tipo = int(input("Digite a conta que deseja abrir.\n\n[1] Poupança\n[2] Corrente\n[3] Salário\n\nR: "))

# if tipo == 1:
#     conta = Poupança(Conta)
#     conta.Tipo()
    
# elif tipo == 2:
#     conta = Corrente(Conta)
#     conta.Tipo()
    
# else:
#     conta = Salario(Conta)
#     conta.Tipo()
    
conta = Poupança(Conta)