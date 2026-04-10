limite = int(input("Digite o limite superior: "))

contador = 0  

print("Números perfeitos encontrados:")

for num in range(1, limite + 1):
    soma_divisores = 0
    # somar divisores próprios
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    if soma_divisores == num:
        print(num)
        contador += 1

print(f"Total de números perfeitos até {limite}: {contador}")