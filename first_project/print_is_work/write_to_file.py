# Открываем файл для записи
with open("расписание.txt", "w", encoding="utf-8") as flight_file:
# Теперь вывод пойдёт не на экран, а в файл
    print("Расписание рейсов на 18 февраля", file=flight_file)
    print("SU123 - 10:05 - Москва", file=flight_file)
    print("BA456 - 11:30 - Лондон", file=flight_file)
    print("AF789 - 13:15 - Париж", file=flight_file)

print("Расписание сохранено в файл!")  # А вот это уже попадёт на табло, а не в файл
with open("журнал_событий.txt", "a", encoding="utf-8") as flight_file:
    print("10:00 - Начало регистрации на рейс SU123", file=flight_file)
    print("10:15 - Открыт выход 15", file=flight_file)