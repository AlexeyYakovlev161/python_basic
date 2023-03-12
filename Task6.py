"""
На платформе: Задача №4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
"""

crane_sum = int(input("Введите число журавликов: "))
if crane_sum % 6 == 0:
    Peter_sergey_sum = crane_sum / 6
    Kate_sum = crane_sum / 6 * 4
    print(
        f"Петя и Сергеи сделали по {int(Peter_sergey_sum)} журавликов, а Катя сделала {int(Kate_sum)} журавликов")
elif crane_sum % 6 == 1:
    Peter_sergey_sum = crane_sum // 6
    Kate_sum = crane_sum // 6 * 4 + 1
    print(
        f"Петя и Сергеи сделали по {int(Peter_sergey_sum)} журавликов, а Катя сделала {int(Kate_sum)} журавликов")
elif crane_sum % 6 == 2:
    Peter_sergey_sum = crane_sum // 6
    Kate_sum = crane_sum // 6 * 4 + 2
    print(
        f"Петя и Сергеи сделали по {int(Peter_sergey_sum)} журавликов, а Катя сделала {int(Kate_sum)} журавликов")
elif crane_sum % 6 == 3:
    Peter_sergey_sum = crane_sum // 6
    Kate_sum = crane_sum // 6 * 4 + 3
    print(
        f"Петя и Сергеи сделали по {int(Peter_sergey_sum)} журавликов, а Катя сделала {int(Kate_sum)} журавликов")
else:
    print("Если дети начинают работать вместе, то такое количество журавликов у них не выходит")