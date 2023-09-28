age = 13
# if age > 18:
#     print("you are adult")

# if age < 18:
#     print("you are kid")

# if age == 13:
#     print("you are teenager")
#     print("something else")

# if age != 14:
#     print("blalalall")

# ==    !=    >     <       >=      <=
# exe1 :
'''
برنامه ای بنویسید که نام و سه نمره دانش آموزی را از ورودی دریافت نماید و معدل او را محاسبه کند
اگر معدل او از 19 بیشتر بود
Ali's Grade is A
را پر ینت نماید

'''

age = 3

# if age < 8:
#     print("You are kid")
# elif age >= 8 and age < 18:
# elif 8 <= age < 18:
#     print("you are junior")
# else:
#     print("you are adult")

# exercise 2 :
'''
برنامه بالا را به گونه ای تغییر دهید که چنانچه
سن فرد بین هشت و سیزده بود
junior
و اگر بین سیزده و هجده بود
teenager
و اگر بزرگتر از هجده بود 
adult
را نمایش دهد

'''

user_name = input('enter username: ')
if user_name == 'admin' or user_name == 'root':
    print("login success")
    print("welcome")
else:
    print("username is not valid")
    print("permission denied")


# به برنامه بالا چک کردن پسور د را هم اضافه نمائید
PASSWORD = '@admin@123'