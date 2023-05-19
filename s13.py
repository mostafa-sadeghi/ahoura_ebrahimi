import random
HANDS = ("r", "p", "s")
round = 1
user_score = 0
computer_score = 0
while True:
    print(f"round {round}")
    # getting player and computer hand
    computer_hand = random.choice(HANDS)
    user_hand = input("Enter your choice (`r`, `p`, `s`): ")
    # display hands
    print("user's hand:", user_hand)
    print("computer's hand:", computer_hand)
    # check the winner
    if user_hand == 'r':
        if computer_hand == 'p':
            print("computer wins.")
            computer_score += 1
        elif computer_hand == 's':
            print('user wins.')
            user_score += 1
        elif computer_hand == 'r':
            print('both equal')
    elif user_hand == 'p':
        if computer_hand == 's':
            print("computer wins.")
            computer_score += 1
        elif computer_hand == 'r':
            print('user wins.')
            user_score += 1
        elif computer_hand == 'p':
            print('both equal')
    elif user_hand == 's':
        if computer_hand == 'r':
            print("computer wins.")
            computer_score += 1
        elif computer_hand == 'p':
            print('user wins.')
            user_score += 1
        elif computer_hand == 's':
            print('both equal')
    print("####################################")
    print("user score:", user_score)
    print("computer score:", computer_score)
    print("####################################")
    if input('Do you want to continue?(y or n): ') == 'n':
        break
    round += 1
# exercise : اضافه کردن شرط امتیاز 3 برای بازیکن  و  کامپیوتر