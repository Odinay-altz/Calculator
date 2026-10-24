print("=== КАЛЬКУЛЯТОР ===")

num1 = float(input("Введи первое число: "))
operation = input("Введи действие (+, -, , /): ")
num2 = float(input("Введи второе число: "))

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "":
    result = num1 * num2

elif operation == "/":
    if num2 == 0:
        print("На ноль делить нельзя")
        exit()
    result = num1 / num2

else:
    print("Неизвестное действие")
    exit()

print("Результат:", result)