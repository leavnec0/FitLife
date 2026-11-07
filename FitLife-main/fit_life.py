
import sys


def fit_life():
    """Рассчитывает ИМТ и количество воды."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    introduction = "Добро пожаловать в FitLife"
    user_name = input("Введите ваше имя: ")
    user_age = int(input("Введите ваш возраст: "))

    greeting = (
        f"{introduction}, {user_name.title()}! "
        f"Вам {user_age} лет."
    )

    weight = float(input("Введите ваш вес в килограммах: "))
    height = float(
        input("Введите ваш рост в метрах, применяя точку: ")
    )

    bmi = round(weight / (height ** 2), 1)
    bmi_text = f"Ваш индекс массы тела: {bmi}"

    water_l = round((weight * 30) / 1000, 2)
    water_text = (
        f"Вам необходимо пить {water_l} литров воды в день."
    )

    recommendation = (
        "Придерживайтесь этих рекомендаций и будете здоровы!"
    )

    result = (
        f"{greeting}\n"
        f"{bmi_text}\n"
        f"{water_text}\n"
        f"{recommendation}"
    )

    print(f"{result}")

    return result


fit_life()
