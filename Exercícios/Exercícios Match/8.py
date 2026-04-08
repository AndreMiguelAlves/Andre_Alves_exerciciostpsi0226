opc = input("Operação(soma,subtrai,multiplica ou divide): ").lower()
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

match opc:
    case "soma":
        print(round(num1 + num2))
    case "subtrai":
        print(round(num1 - num2))
    case "multiplica":
        print(round(num1 * num2))
    case "divide":
        print(round(num1 / num2))
    case _:
        print("operação inválida!")
