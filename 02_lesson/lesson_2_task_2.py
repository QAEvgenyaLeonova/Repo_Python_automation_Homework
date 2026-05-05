def is_year_leap(number):
    return number % 4 == 0

age_number = int(input('Введите год: '))
result = is_year_leap(age_number)
print(f'Год: {age_number} {result}')