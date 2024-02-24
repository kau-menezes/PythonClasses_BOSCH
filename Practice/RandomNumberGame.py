import random

highest_score = 0

while True:

    score = 0
        
    while True:

        pc_pick = int(random.randint(1, 10))    
        
        print(pc_pick)
        
        user_pick = int(input("\n---\nDigite um número:\n\nR: "))
        
        choice = int(input("\nEscolha entre:\n\n[1] ÍMPAR\n\n[2] PAR\n\nR: "))
        
        verification_print = pc_pick + user_pick
        
        verification = 0
        
        if verification_print % 2 == 0:
            verification = 2
            
        else:
            verification = 1
            
        if choice == verification:
            
            print("\nVocê ganhou! :)")
            score =+ 1
            print(f"\nSeu número: {user_pick} | Número do oponente: {pc_pick} | Soma: {verification_print}")
            
        else:
            
            print("\nVocê perdeu! :(")
            print(f"Sua pontuação: {score}")
            print(f"Seu recorde: {highest_score}")  
            print(f"\nSeu número: {user_pick} | Número do oponente: {pc_pick} | Soma: {verification_print}")
            
            answer = ""
            while answer not in "SN":
                answer = str(input("\n\nDeseja jogar novamente? Digite 'SIM' ou 'NÃO'")).uper[0]
            
            if answer == "N":
                print("\nJogo encerrado.")
                print(f"Seu recorde: {highest_score}")  
                break
        
            elif answer == "S":
                continue
                    
        if score > highest_score:
            highest_score = score    
        
    
