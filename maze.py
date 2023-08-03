import turtle

main_surface = turtle.Screen()
main_surface.setup(600, 600)

tiles_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

for i in range(len(tiles_map)):
    for j in range(len(tiles_map[i])):
        if tiles_map[i][j] == 1:
            player = turtle.Turtle()
            player.penup()
            player.speed("fastest")
            player.shape("square")
            player.goto(-290 + (j * 20), 290)


running = True
while running:
    main_surface.update()
