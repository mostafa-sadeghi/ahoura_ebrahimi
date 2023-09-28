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
    if user_guess == secret_number:
        return "You got it"

    string = ""
    for i in range(len(user_guess)):
        if user_guess[i] == secret_number[i]:
            string += "Fermi, "

        elif user_guess[i] in secret_number:
            string += "Pico, "

    if not len(string):
        return "Bagels"
    else:
        return string
