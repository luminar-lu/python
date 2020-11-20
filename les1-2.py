print("Введите время в секундах:")
num = int(input())
hours = num // 3600
minutes = num % 3600 // 60
seconds = num % 60
print(f"Время  в формате ЧЧ:ММ:СС : {hours}:{minutes}:{seconds}")

