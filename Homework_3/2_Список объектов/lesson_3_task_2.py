'''from smartphone import Smartphone

catalog = [
    Smartphone('Apple iPhone', '14', '+7999 777 77 77'),
    Smartphone('Samsung Galaxy', 's23', '+7933 888 88 88'),
    Smartphone('Huawei', 'P50', '+7998 666 66 66'),
    Smartphone('Xiaomi Redmi Note', '11', '+7977 222 22 22'),
    Smartphone('Google Pixel', '7', '+7913 999 99 99')
]

for phone in catalog:
    print(f'{phone.phone_brand} - {phone.phone_model}. {phone.sub_number}')
    '''

from smartphone import Smartphone

catalog = [Smartphone('Apple iPhone', '14', '+7999 777 77 77'),
           Smartphone('Huawei', 'P50', '+7998 666 66 66'),
           Smartphone('Honor', 'x8', '+79994704714')]

for Smartphone_object in catalog:
    print(f'Марка телефона: {Smartphone_object.marka}, Модель телефона: {Smartphone_object.model}, Номер телефона: {Smartphone_object.number}')