import re

def normalize_phone(phone_number):
    digits = re.sub(r'\D', '', phone_number)
    if len(digits) == 10:
        return '+38' + digits
    elif len(digits) == 12 and not digits.startswith('38'):
        return '+' + digits
    elif len(digits) == 11 and digits.startswith('0'):
        return '+38' + digits[1:]
    elif len(digits) == 9:
        return '+380' + digits
    else:
        return '+' + digits

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
