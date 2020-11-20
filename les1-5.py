rev = int(input("Введите выручку вашей фирмы: "))
cost = int(input("Введите убытки вашей фирмы: "))
res = rev - cost
if res > 0:
    print(f"Ваша фирма заработала {res} рублей.")
    eff = res / rev * 100
    # print(f"Рентабельность вашей фирмы:  %.")
    print("{:.2f} %.".format(eff))
    num = int(input("Введите количество сотрудников: "))
    eff_1 = rev / num
    print("Средняя прибыль на одного сотрудника:{:.2f}.".format(eff_1))
elif res == 0:
    print("Ваша фирма самоокупается.")
else:
    print(f"Ваша фирма потеряла {(res * -1)} рублей.")
