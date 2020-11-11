
def draw_hexa_turtle():
    # make 36 hexagons, each 10 degrees apart
    for n in range(36):
        # make hexagon by repeating 6 times
        for i in range(6):
            # shelly.color(colors[i])  # pick color at position i
            shelly.color(random.choice(colors))
            shelly.forward(100)
            shelly.left(60)
        # add a turn before the next hexagon
        shelly.right(10)


def draw_circles_turtle():
    shelly.penup()
    shelly.color('orange')
    for j in range(36):
        shelly.forward(220)
        shelly.pendown()
        shelly.circle(10)
        shelly.penup()
        shelly.backward(220)
        shelly.right(10)


if __name__ == "__main__":
    # make a geometric rainbow pattern
    import turtle  # import turtle library
    import random
    # pick order of colors for the hexagon
    colors = ['red', 'yellow', 'blue', 'orange', 'cyan', 'purple']
    # Instantiation, when I use a Class established, a copy made of it
    shelly = turtle.Turtle()
    shelly.shape('turtle')
    shelly.speed(9)
    turtle.bgcolor('black')  # turn background black bgcolor
    draw_hexa_turtle()
    draw_circles_turtle()
    shelly.hideturtle()
