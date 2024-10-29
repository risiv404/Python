salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

obsh_capital = 0

for month in range(months):
    if month > 0:
        spend *= (1 + increase)

    nehvat = spend - salary

    if nehvat > 0:
        obsh_capital += nehvat

obsh_capital = round(obsh_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", obsh_capital)
