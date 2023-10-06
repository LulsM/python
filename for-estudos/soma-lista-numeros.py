#Solicita uma lista de numeros separador por espaços
numeros=input("Digite uma lista de números separados por espaços: ").split()

soma = 0

#Intera/percorre sobre os números e os soma
for numero in numeros:
    soma += float(numero)
    
print(f"A soma dos números é: {soma}")