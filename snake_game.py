from turtle import Screen
from time import sleep
from random import randint
from snake_game_utils import *


display_surface = make_screen()


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
    for i in range(len(snake_bodies) - 1, 0, -1):
        x = snake_bodies[i-1].xcor()
        y = snake_bodies[i-1].ycor()
        snake_bodies[i].goto(x, y)

    if len(snake_bodies) > 0:
        headx = snake_head.xcor()
        heady = snake_head.ycor()
        snake_bodies[0].goto(headx, heady)

    move_snake(snake_head)
    sleep(0.2)
