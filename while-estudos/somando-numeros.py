soma = 0
while True:
    numero = float(input("Digite um número (ou 0 para parar)"))
    
    if numero == 0:
        break #finaliza o loop
    else:
        soma += numero 

print(f"A soma dos numeros é: {soma}")