def month_to_season(number_month):
    if 3 <= number_month <= 5:
        return 'Весна'
    elif 6 <= number_month <= 8:
        return 'Лето'
    elif 9 <= number_month <= 11:
        return 'Осень'
    else:
        return 'Зима'

time_year = int(input('Введите номер месяца: '))
result = month_to_season(time_year)
print(f' Время года:  {result}')