#Solicita ao usuário que insira uma lista de nomes separados por vírgula 
nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")

#Intera sobre os nomes e os imprime
for nome in nomes:
    print("Olá,", nome.strip()) #strip( remove espaço em branco extras)
