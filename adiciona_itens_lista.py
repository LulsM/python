lista = []

while True:
    num = int(input("Digite um numero: "))
    if num == 0:
        break
    lista.append(num)
print(lista)

for item in lista:
    print(item)