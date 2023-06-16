from turtle import Screen, Turtle
from time import sleep
from random import randint
from snake_game_utils import *

display_surface = Screen()
display_surface.bgcolor('blue')
display_surface.title('Snake Game')
display_surface.setup(width=600, height=600)
display_surface.tracer(0)


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
    if snake_head.direction == "down":
        snake_head_y_position = snake_head.ycor()
        snake_head.sety(snake_head_y_position - 20)
    if snake_head.direction == "right":
        snake_head_x_position = snake_head.xcor()
        snake_head.setx(snake_head_x_position + 20)
    if snake_head.direction == "left":
        snake_head_x_position = snake_head.xcor()
        snake_head.setx(snake_head_x_position - 20)


'''Do not touch'''


def change_direction_to_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def change_direction_to_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def change_direction_to_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def change_direction_to_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


'''Do not touch'''


def change_food_position():
    random_x_position = randint(-270, 270)
    random_y_position = randint(-270, 270)
    food.goto(random_x_position, random_y_position)


snake_head = generate_turtle_object("square", "black")
snake_head.direction = ""

food = generate_turtle_object("circle", "red")
change_food_position()

display_surface.listen()
display_surface.onkeypress(change_direction_to_up, "Up")
display_surface.onkeypress(change_direction_to_left, "Left")
display_surface.onkeypress(change_direction_to_down, "Down")
display_surface.onkeypress(change_direction_to_right, "Right")


def my_func(x, y):
    snake_head.ondrag(None)
    # snake_head.setheading(snake_head.towards(x,y))
    snake_head.goto(x, y)

    snake_head.ondrag(my_func)


snake_head.ondrag(my_func)

snake_bodies = []
running = True
while running:
    display_surface.update()

    if snake_head.distance(food) < 20:
        change_food_position()
        new_tail = generate_turtle_object("square", "grey")
        snake_bodies.append(new_tail)
    # TODO
    move_snake()
    sleep(0.2)
