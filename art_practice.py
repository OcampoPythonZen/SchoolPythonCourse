

if __name__ == "__main__":
    # Im calling the turtle library
    import turtle
    import time
    # instantiation of turtle library asigned to the shelly var
    shelly = turtle.Turtle()
    # shape turtle draw
    shelly.shape('turtle')
    # speed to the turtle

    for n in range(36):
        for i in range(1):
            shelly.speed(4)
            shelly.forward(120)
            shelly.right(90)
            shelly.forward(40)
            shelly.right(90)
            shelly.forward(100)
            shelly.left(90)
            shelly.forward(40)
            shelly.left(90)
            shelly.forward(40)
            shelly.right(90)
            shelly.forward(40)
            shelly.right(90)
            shelly.forward(40)
            shelly.left(90)
            shelly.forward(40)
            shelly.left(90)
            shelly.forward(100)
            shelly.right(90)
            shelly.forward(40)
            shelly.right(90)
            shelly.forward(140)
            shelly.right(90)
            shelly.forward(200)
            shelly.right(90)
            shelly.forward(20)
        shelly.right(10)
