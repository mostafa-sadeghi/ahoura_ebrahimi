# import turtle


# def draw_square():
#     for i in range(4):
#         pen.forward(100)
#         pen.left(90)

# def draw_triangle():
#     for i in range(3):
#         pen.forward(100)
#         pen.left(120)

# screen = turtle.Screen()
# screen.setup(700, 500)
# screen.title("my app")
# pen = turtle.Pen()

# # draw_square()
# draw_triangle()


# exercise 1 : تعداد اضلاع از ورودی گرفته شود



# turtle.done()


#################################################################
# sample 2

import turtle

screen = turtle.Screen()
screen.setup(700, 500)
screen.title("my app")
pen = turtle.Pen()
pen.fillcolor("red")

def draw_shape(sides):
    pen.begin_fill()
    for num in range(sides):
        
        pen.forward(100)
        pen.left(360/sides)
    pen.end_fill()

draw_shape(5)

# exercise 2: علاوه بر تعداد اضلاع، اندازه(طول) ضلع نیز از ورودی گرفته شود
# exercise 3: امکان اینکه شکل توپر و یا توخالی باشد نیز وجود داشته باشد
# exercise 4: امکان انتخاب رنگ کشیدن شکل نیز وجود داشته باشد





turtle.done()