# Exercício 5 : 

num1 = int(input("Digite primeiro número : "))
num2 = int(input("Digite segundo número : "))
num3 = int(input("Digite terceiro número : "))



if num1 <= num2 and num2 <= num3:
    print("Crescente:", num1, num2, num3)

elif num1 <= num3 and num3 <= num2:
    print("Crescente:", num1, num3, num2)

elif num2 <= num1 and num1 <= num3:
    print("Crescente:", num2, num1, num3)

elif num2 <= num3 and num3 <= num1:
    print("Crescente:", num2, num3, num1)

elif num3 <= num1 and num1 <= num2:
    print("Crescente:", num3, num1, num2)

else:
    print("Crescente:", num3, num2, num1)



if num1 >= num2 and num2 >= num3:
    print("Decrescente:", num1, num2, num3)

elif num1 >= num3 and num3 >= num2:
    print("Decrescente:", num1, num3, num2)

elif num2 >= num1 and num1 >= num3:
    print("Decrescente:", num2, num1, num3)

elif num2 >= num3 and num3 >= num1:
    print("Decrescente:", num2, num3, num1)

elif num3 >= num1 and num1 >= num2:
    print("Decrescente:", num3, num1, num2)

else:
    print("Decrescente:", num3, num2, num1)


# Exercício 6 : 

nome = input("Digite o nome do cliente: ")
compra = float(input("Digite o valor da compra: "))

if compra <= 200:
    desconto = compra * 0.10
elif compra <= 500:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20

    total = compra - desconto

print(f"Nome: {nome}")
print(f"Compra: {compra:.2f}€")
print(f"Desconto: {desconto:.2f}€")
print(f"Total a pagar: {total:.2f}€")

