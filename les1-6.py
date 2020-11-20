a = int(input("Начальный результат:"))
b = int(input("Конечный результат:"))
day = 0
while True:
    day = day + 1
    a = a * 1.1
    # print(day,"-й день:{:.2f}.".format(a))
    if a >= b:
        break
print(f"На {day}-й день спортсмен достиг результата - не менее {b} км.")