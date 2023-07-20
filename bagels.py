from bagels_config import message, NUM_DIGITS, MAX_GUESSES
from bagels_utils import create_secret_number

number_of_user_guesses = 1
print(message)
secret_number = create_secret_number(NUM_DIGITS)

print("secret number is generated!!!")

while number_of_user_guesses < MAX_GUESSES:
    user_guess = input(f"enter a {NUM_DIGITS}digits number: ")
    help = get_help(user_guess, secret_number)
    number_of_user_guesses += 1



