# shoppingList = ""
# '''
# 1. egg
# 2. apple
# 3. banana
# '''
# product = "mashroom"
# shoppingList = shoppingList + product  # shoppingList += product

# product2 = "apple"
# shoppingList = shoppingList + '\n' + product2

# print(shoppingList)

# print(shoppingList[0])


# shoppingList = "mashroom\napple"
# print()  # apple
# print()  # mashroom


# shopping_list = []

# shopping_list.append("apple")
# shopping_list.append("banana")
# shopping_list.append("mashroom")

# print(shopping_list)
# print("1.", shopping_list[0])
# print("2.", shopping_list[1])
# print("3.", shopping_list[2])

# برنامه ای بنویسید که نام چهار دانش آموز را از ورودی دریافت نماید و در لیستی ذخیره کند
# از لیست بالا اولین اسم و آخرین اسم را جداگانه پرینت کنید

# students = []
# s1 = input('enter student name: ')
# students.append(s1)
# s1 = input('enter student name: ')
# students.append(s1)
# s1 = input('enter student name: ')
# students.append(s1)
# s1 = input('enter student name: ')
# students.append(s1)
# print(students)
# print(students[0])
# print(students[-1])

# all_students = input('enter student`s names with space:> ')
# my_list = all_students.split()
# print(my_list)
# print(my_list[0])
# print(my_list[-1])


# برنامه ای بنویسید که چهار عدد را از ورودی دریافت نماید و در لیست ذخیره کند
# مجموع اعداد لیست را پرینت نماید.


# students = ['a', 'b', 'c', 'd']

# del students[1]
# print(students)

# students.remove('c')
# print(students)


# exercise 1 : برنامه ای بنویسید که اسامی چهار نفر را ازووردی دریافت نماید و نفر سوم را از لیست حذف کند

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[0:3])
# print(numbers[3:6])

# exercise 2 از لیست بالا برش های زیر را ایجاد نمائید
'''
[2,3,4]
[6,7]
[5,6,7,8]
[3,4,5]
[8,9]
'''

# my_list = [[1,2], 'a',2, True]
# print(my_list[0])
# print(my_list[1])

# string = 'abcd' * 5
# print(string)

# string1 = 'a'
# string2 = 'b'
# print(string1 + string2)

# list1 = [1,2] * 5
# print(list1)

# list2 = ['a','b']
# list3 = ['c','d']
# print(list2 + list3)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::2])
# exercise 3   از لیست بالا عدد های زوج را فقط نمایش دهید
print(numbers[3:8:3])
