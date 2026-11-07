def fit_life():
    """Рассчитывает ИМТ и количество воды."""
    introduction = "Добро пожаловать в FitLife"
    user_name = input("Введите ваше имя: ")
    user_age = int(input("Введите ваш возраст: "))

    greeting = f"{introduction}, {user_name.title()}! Вам {user_age} лет."

    weight = float(input("Введите ваш вес в килограммах: "))
    height = float(input("Введите ваш рост в метрах, применяя точку: "))
    bmi = weight / (height ** 2)
    bmi = round(bmi, 1)
    bmi_text = f"Ваш индекс массы тела: {bmi}"

    water_ml = weight * 30
    water_l = water_ml / 1000
    water_l = round(water_l, 2)
    water_text = f"Вам необходимо пить {water_l} литров воды в день."

    recommendation = "Придерживайтесь этих рекомендаций и будете здоровы!"
    result = f"{greeting}\n{bmi_text}\n{water_text}\n{recommendation}"
    print(f"{result}")
    return result


fit_life()
