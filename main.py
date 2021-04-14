"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
    * до часа: <m> мин <s> сек;
    * до суток: <h> час <m> мин <s> сек;
    * *до месяца, до года, больше года: по аналогии.
"""

print("Данная программа позволит Вам совершить точный перевод из секунд в иные единицы времени "
      "(минуты, часы, дни и т.д.)")
while True:
    duration = input("Введите желаемое количество секунд: ")

    if duration.isdigit():
        duration = int(duration)
        answer = ""
        for i in range(6):
            # Соотношение секунд к другим временным переменным
            time_ratio = [31104000, 2592000, 86400, 3600, 60, 1]

            if (duration // time_ratio[i]) != 0:
                # Получение целой единицы времени
                whole = duration // time_ratio[i]
                # Обновление оставшегося промежутка времени
                duration = duration % time_ratio[i]
                # Определяем название единицы времени
                if i == 0:
                    time_variable = " г. "
                elif i == 1:
                    time_variable = " мес. "
                elif i == 2:
                    time_variable = " дн. "
                elif i == 3:
                    time_variable = " час. "
                elif i == 4:
                    time_variable = " мин. "
                elif i == 5:
                    time_variable = " сек. "
                # Запись ответа в строку
                answer = answer + str(whole) + time_variable
        print(answer)
