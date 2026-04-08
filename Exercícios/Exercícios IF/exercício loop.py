
pares = 0
impares = 0


for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))

    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1 


print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
