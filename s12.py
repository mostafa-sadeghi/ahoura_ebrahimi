# students = [
#     {
#         'id': 1,
#         'name': 'erfan',
#         'course': 'python'
#     },
#     {
#         'id': 2,
#         'name': 'ahoura',
#         'course': 'python'
#     }
# ]
# exercise 1:   با کمک حلقه فور و نیز حلقه وایل اسامی دانش آموزان را از لیست بالا نمایش دهید
# print(students[0]['name'])
# exercise 2: یک دانش آموز جدید به لیست اضافه کنید و سپس کل لیست را پرینت کنید
# exercise 3: کلیه مشخصات دانش آموز دوم را پرینت کنید یعنی اسمش در یک خط، و ...


# done = True
# while done:
    
#     quit = input('Do you want to quit?(y or n) ')
#     if quit == 'y':
#         done = False
#     if quit != 'n' and quit != 'y':
#         print("The value is not valid!!!")



import random

# for i in range(50):
#     my_number = random.randrange(50)
#     print(my_number)

# print(random.randrange(100,201))

ACTIONS = ["rock", "paper", "scissors"]
# print(random.choice(ACTIONS))

random_index = random.randrange(3)
print(ACTIONS[random_index])