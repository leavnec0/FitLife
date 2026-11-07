introduction = "Доброе пожаловать в FitLife"
user_name = input("Как вас зовут? ")
user_age = int(input("Сколько вам лет? "))

print (f"{introduction}, {user_name.title()}! Вам {user_age} лет." )

weight = float(input("Введите ваш вес в килограммах: "))
height = float(input("Введите ваш рост в метрах, применяя точку: "))

bmi = weight / (height ** 2) 
bmi = round(bmi, 1)
print(f"Ваш индекс массы тела: {bmi}")

water_ml = weight * 30
water_l = water_ml / 1000
print(f"Вам необходимо пить {water_l} литров воды в день.")
water_l = round(water_l, 2)

print(f"Придерживайтесь этих рекомендаций, чтобы оставаться здоровым!")