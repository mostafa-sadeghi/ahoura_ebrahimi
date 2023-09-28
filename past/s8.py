# اعضای تاپل قابل تغییر نیستند
# numbers = (2,5,8,0,6)# Type error
# print(type(numbers))
# numbers[0] = 100

# print(numbers[0])
# print(numbers[:3])

# numbers = [1,2,3,4,5]
# numbers[0] = 100
# print(numbers)

# دیکشنری
# dictionary

# favorite_sports = ["football","basketball","tennis","pingpong"]

favorite_sports = {}
# favorite_sports['ahura'] = "tennis"
# favorite_sports["erfan"] = "basketball"

# print(favorite_sports)
# print("ahura likes", favorite_sports["ahura"])
# print("erfan likes", favorite_sports["erfan"])

# name = input('enter a name: ')
# sport = input('enter a sport name: ')
# favorite_sports[name] = sport
# name = input('enter a name: ')
# sport = input('enter a sport name: ')
# favorite_sports[name] = sport
# print(favorite_sports)
# print("ahura likes", favorite_sports["ahura"])
# print("erfan likes", favorite_sports["erfan"])

# برنامه ای بنویسید که نام، نا مخانوادگی و سن سه دانش آموز را از ورودی بگیرد و 
# مشخصات هر دانش آموز را در یک دیکشنری ذخیره نماید و سپس هر یک از دیکشنری ها را داخل لیستی اضافه کند
# در نهایت اطلاعات هریک از دانش آموزان را از درون لیست نمایش دهد.

# student = {}
# all_students = []
# name = input('enter a name: ')
# age = input('enter the age: ')
# student['name'] = name
# student['age'] = age
# all_students.append(student)
# print(all_students)


# all_animals = []
# name = input('enter anima`s name: ')
# info = input('enter animal`s information: ')
# age = input('enter animal`s age: ')
# animal = {}
# animal['name'] = name
# animal['info'] = info
# animal['age'] = age
# all_animals.append(animal)


# name = input('enter anima`s name: ')
# info = input('enter animal`s information: ')
# age = input('enter animal`s age: ')
# animal = {}
# animal['name'] = name
# animal['info'] = info
# animal['age'] = age
# all_animals.append(animal)

# print(all_animals)

# print(all_animals[0]['name'])

# my_dict = {'id':1, 'name':'reza','age':11}
# print(my_dict)
# my_dict['age'] = 12
# print(my_dict)
# del my_dict['age']
# print(my_dict)


import turtle
s = turtle.Screen()
s.bgcolor('orange')
# s.register_shape("triangle1", ((0,0), (10,10), (-10,10)))
s.register_shape('strawberry.gif')
# s.bgpic('mario.png')
p = turtle.Pen()
p.shape('strawberry.gif') # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
p.shapesize(2)
p.pensize(5)
p.color('red','green')
p.speed('fast') # fastest  fast  normal slow  slowest
p.penup()
p.goto(200,200)
p.pendown()
# draw a triangle
p.begin_fill()
p.forward(100)
p.left(120)
p.stamp()
p.forward(100)
p.left(120)
p.stamp()
p.forward(100)
p.left(120)
p.stamp()
p.end_fill()
p.hideturtle()
p.setheading(30)
p.fd(83)

s.exitonclick()
# exercise 2 : کشیدن مربع
# کشیدن پنجضلعی
# کشیدن شش ضلعی
# کشیدن هفت ضلعی
# کشیدن هشت ضلعی 
# کشیدن نه ضلعی


