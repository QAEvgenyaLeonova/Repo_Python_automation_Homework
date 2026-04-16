'''from address import Address
from mailing import Mailing


to_address = Address(
    mail_city = '644058',
    city = 'Omsk',
    street = 'Molodogvardeiskaia',
    home = '11',
    flat = '65'
)


from_address = Address(
    mail_city = '354340',
    city = 'Adler',
    street ='Pavlika Morozova',
    home ='43',
    flat ='5'
)

mailing = Mailing(
    to_address = to_address,
    from_address = from_address,
    cost = 500,
    track = '5547895646123'
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.home} - {mailing.from_address.flat} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.home} - {mailing.to_address.flat}. "
      f"Стоимость {mailing.cost} рублей.")
'''

from address import Address
from mailing import Mailing


mailing_from = Address(
    '354340',
    'Adler',
    'Pavlika Morozova',
    '43',
    '5'
)

mailing_to = Address(
    '644058',
    'Omsk',
    'Molodogvardeiskaia',
    '11',
    '65'
)

mailing = Mailing(
    to_address = mailing_to,
    from_address = mailing_from,
    cost = 1000,
    track = '64405822266658'
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.home} - {mailing.from_address.flat} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.home} - "
      f"{mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")

'''
Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.
'''