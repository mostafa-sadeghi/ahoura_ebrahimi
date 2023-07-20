import string
from random import shuffle


def create_secret_number(num_of_digits):
    my_numbers = list(string.digits)
    shuffle(my_numbers)
    result = ""
    for d in my_numbers[:num_of_digits]:
        result += d

    return result


def get_help(user_guess, secret_number):
    pass
"""
اگر کاربر درست حدس زده باشد
پیغام برنده را نمایش دهد
اگر سه رقم غلط باشد
bagel

اگر رقم درست باشد ولی سرجایش نباشد
pico

اگر رقم درست باشد و سرجایش باشد
fermi
را نمایش دهد
"""