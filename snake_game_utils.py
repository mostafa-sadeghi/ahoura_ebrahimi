from turtle import Screen, Turtle


def generate_turtle_object(shape, color):
    turtle_object = Turtle()
    turtle_object.shape(shape)
    turtle_object.color(color)
    turtle_object.penup()
    turtle_object.speed('normal')
    return turtle_object


def make_screen():
    display_surface = Screen()
    display_surface.bgcolor('blue')
    display_surface.title('Snake Game')
    display_surface.setup(width=600, height=600)
    display_surface.tracer(0)
    return display_surface


def move_snake(snake_head):
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


def reset(head, bodies):
    head.goto(0, 0)
    head.direction = ""
    for body in bodies:
        body.ht()

    bodies.clear()
