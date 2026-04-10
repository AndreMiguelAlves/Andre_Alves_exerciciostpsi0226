num = (int(input("Digite um número : ")))

print(f"Tabuada do {num} :")

for i in range(1,10):
    resultado = num *i
    print(f"{num} x {i} = {resultado}")
