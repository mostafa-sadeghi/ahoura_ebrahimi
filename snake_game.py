from turtle import Screen, Turtle
from time import sleep

display_surface = Screen()
display_surface.bgcolor('blue')
display_surface.title('Snake Game')
display_surface.setup(width=600, height=600)


def generate_turtle_object(shape, color):
    turtle_object = Turtle()
    turtle_object.shape(shape)
    turtle_object.color(color)
    turtle_object.penup()
    turtle_object.speed('fastest')
    return turtle_object


def move_snake():
    if snake_head.direction == "up":
        snake_head_y_position = snake_head.ycor()
        snake_head.sety(snake_head_y_position + 20)
    # بقیه جهت ها
    # TODO


def change_direction_to_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"
# TODO نوشتن توابع برای سایر جهت ها


def change_direction_to_left():
    pass
    # TODO


def change_direction_to_down():
    pass
    # TODO


def change_direction_to_right():
    pass
    # TODO


snake_head = generate_turtle_object("square", "black")
snake_head.direction = ""
# Exercise تعیین پوزیشن رندم برای غذا
food = generate_turtle_object("circle", "red")
food.goto(100, 100)

display_surface.listen()
display_surface.onkeypress(change_direction_to_up, "w")
display_surface.onkeypress(change_direction_to_left, "a")
display_surface.onkeypress(change_direction_to_down, "s")
display_surface.onkeypress(change_direction_to_right, "d")


running = True
while running:
    display_surface.update()
    move_snake()
    sleep(0.2)
