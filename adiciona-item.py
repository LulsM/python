compra = []

while True:
    item = str(input("Itens de compra:"))
    print("Digite parar para finalizar")
    if item == 'parar':
        break
    compra.append(item)
    
for item in compra:
    print(item)
print(compra)