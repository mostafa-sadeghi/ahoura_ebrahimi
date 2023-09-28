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

def draw_shape(sides, length, fill, fill_color):
    if fill == True:
        pen.fillcolor(fill_color)
        pen.begin_fill()
    for num in range(sides):
        
        pen.forward(length)
        pen.left(360/sides)
    if fill == True:
        pen.end_fill()

shape_number_of_sides = int(turtle.textinput("iput side number","How many sides?"))
length_of_side = int(turtle.textinput('input length',"enter side length"))
fill_or_not = turtle.textinput('input fill or no', 'Fill or Not?(f or n)')
fill_color = ''
if fill_or_not == 'f':
    fill_color = turtle.textinput('input color','which color?')
    fill = True
else:
    fill = False
draw_shape(shape_number_of_sides, length_of_side, fill, fill_color)

# exercise 2: علاوه بر تعداد اضلاع، اندازه(طول) ضلع نیز از ورودی گرفته شود
# exercise 3: امکان اینکه شکل توپر و یا توخالی باشد نیز وجود داشته باشد
# exercise 4: امکان انتخاب رنگ کشیدن شکل نیز وجود داشته باشد





turtle.done()