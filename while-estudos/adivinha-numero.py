import random

#Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

tentativas = 0
adivinhou = False

while not adivinhou:
    tentativa = int(input("Adivinhe o número (entre 1 e 100): "))
    tentativas += 1
    
    if tentativa == numero_secreto:
        print(f"Boa, vocÊ adivinhou o número {numero_secreto} em {tentativas} tentativas")
        adivinhou = True
    elif tentativa < numero_secreto:
        print("Tenta mais pra cima")
    else:
        print("Alto de mais, talvez mais em baixo")
    