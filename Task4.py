"""
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""

revenue = int(input("Введите значение выручки фирмы: "))
costs = int(input("Введите значение издержек фирмы: "))
if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue
    print(
        f"Ваша фирма работает с прибылью: {profit}. Рентабельность выручки {profitability}")
    employees_sum = int(input("Введите численность сотрудников фирмы: "))
    profit_employee = profit / employees_sum
    print(
        f"Прибыль фирмы в расчёте на одного сотрудника: {int(profit_employee)}.")
else:
    print(f"Ваша фирма работает с убытком")
