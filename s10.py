# for i in [2,4,6,7,4,2]:
#     print(i)

# for s in 'python':
#     print(s.upper(), end=' ')

# print()

# string = 'python'
# print(string[:3])

# برنامه ای بنویسید که نا م کاربر را از ورودی دریافت نماید
# و تک تک کارکترهای آن را با یک فاصله و با حروف بزرگ نمایش دهد


# exercise 1:
# MONTHS = "JanFebMarAprMay"
# کاربر عددی را وارد می نماید و برنامه می بایست اسم ماه را نمایش دهد.
# مثال:
# user input = 1    => output : Jan 
# months_list = []

# for i in range(len(MONTHS)//3):
#     months_list.append(MONTHS[i*3:i*3+3])

# print(months_list)

# month_number = int(input('enter month number: '))
# print("month number is:",months_list[month_number-1])





# month_number = int(input('enter month number: '))
# if month_number == 1:
#     print(MONTHS[:3])
# elif month_number == 2:
#     print(MONTHS[3:6])
# elif month_number == 3:
#     print(MONTHS[6:9])
# elif month_number == 4:
#     print(MONTHS[9:12])
# elif month_number == 5:
#     print(MONTHS[12:15])




# for i in range(3):
#     print("a")

# for j in range(3):
#     print("b")

# for i in range(3):
#     print("a")

#     for j in range(3):
#         print("b")

# exercise 2:
# برنامه ای بنویسید که پنج عدد از ورودی دریافت نماید و حاصل جمع آن ها را محاسبه و نمایش دهد
# در حلقه فور شما درگیر 
# i )
# (i =0   i< 5)
# نمی شوید

# result = 0

# for i in range(5):
#     new_number = int(input('enter a number: '))
#     result += new_number

# print(result)

#  یک برنامه بنویسید که 5 عدد از ورودی بگیرد و تعداد عدد 100 وارد شده را نمایش دهد


count = 0

for i in range(5):
    new_number = int(input('enter a number: '))
    if new_number == 100:
        count += 1

print(count)