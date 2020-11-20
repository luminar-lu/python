num = int(input("Введите целое положительное число: "))
maximum = []
while True:
    x = num % 10
    maximum.append(x)
    num = num // 10
    if num == 0:
        break
print(f"Наибольшая цифра введенного числа: {max(maximum)}")

