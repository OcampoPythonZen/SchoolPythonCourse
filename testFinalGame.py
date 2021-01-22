from tkinter import *
import random


window = Tk()
window.title('The Candy-Frog Game')


canvas = Canvas(window, width=400, height=400, bg='black')
canvas.pack()


title = canvas.create_text(200, 200, text='The Frog Monster',
                           fill='white', font=('Helvetica', 30))
directions = canvas.create_text(200, 300, text='Collect candy \
but avoid the red ones', fill='white', font=('Helvetica', 15))

score = 0
score_display = Label(window, text="Score :" + str(score))
score_display.pack()

level = 1
level_display = Label(window, text="Level :" + str(level))
level_display.pack()

player_image = PhotoImage(file="greenChar.gif")
mychar = canvas.create_image(200, 360, image=player_image)

candy_list = []  # list containing all candy created, empty at start
bad_candy_list = []  # list containing all bad candy created, empty at start
candy_speed = 2  # initial speed of falling candy
candy_color_list = ['red', 'yellow', 'blue', 'green', 'purple', 'pink',
                    'white']


def make_candy():
    # pick a random x position
    xposition = random.randint(1, 400)
    # pick a random color
    candy_color = random.choice(candy_color_list)
    # create a candy of size 30 at random position and color
    candy = canvas.create_oval(
        xposition, 0, xposition+30, 30, fill=candy_color)
    # add candy to list
    candy_list.append(candy)
    # if color of candy is red - add it to bad_candy_list
    if candy_color == 'red':
        bad_candy_list.append(candy)
    # schedule this function to make candy again
    window.after(1000, make_candy)

def move_candy():
    # loop through list of candy and change y position
    for candy in candy_list:
        canvas.move(candy, 0, candy_speed)
        # check if end of screen - restart at random position
        if canvas.coords(candy)[1] > 400:
            xposition = random.randint(1, 400)
            canvas.coords(candy, xposition, 0, xposition+30, 30)
    # schedule this function to move candy again
    window.after(50, move_candy)

def update_score_level():
    # use of global since variables are changed
    global score, level, candy_speed
    score = score + 1
    score_display.config(text="Score :" +
                         str(score))
    # determine if level needs to change
    # update level and candy speed
    if score > 5 and score <= 10:
        candy_speed = candy_speed + 1
        level = 2
        level_display.config(text="Level :" +
                             str(level))
    elif score > 10:
        candy_speed = candy_speed + 1
        level = 3
        level_display.config(text="Level :" +
                             str(level))

def end_game_over():
    window.destroy()

def end_title():
    canvas.delete(title)  # remove title
    canvas.delete(directions)  # remove directions

def collision(item1, item2, distance):
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    overlap = xdistance < distance and ydistance < distance
    return overlap

def check_hits():
    # check if it hit a bad candy - need to end game
    for candy in bad_candy_list:
        if collision(mychar, candy, 30):
            game_over = canvas.create_text(200, 200, text='Game Over', fill='red', font=('Helvetica', 30))
            # end game but after user can see score
            window.after(2000, end_game_over)
            # do not check any other candy, window to be destroyed
            return
    # check if it hit any good candy
    for candy in candy_list:
        if collision(mychar, candy, 30):
            canvas.delete(candy)  # remove from canvas
            # find where in list and remove and update score
            candy_list.remove(candy)
            update_score_level()
    # schedule check Hits again
    window.after(100, check_hits)


move_direction = 0  # track which direction player is moving

def check_input(event):
    global move_direction
    key = event.keysym
    if key == "Right":
        move_direction = "Right"
    elif key == "Left":
        move_direction = "Left"

def end_input(event):
    global move_direction
    move_direction = "None"

def move_character():
    if move_direction == "Right" and canvas.coords(mychar)[0] < 400:
        canvas.move(mychar, 10, 0)
    if move_direction == "Left" and canvas.coords(mychar)[0] > 0:
        canvas.move(mychar, -10, 0)
    window.after(16, move_character)  # Move character at 60 frames per second

canvas.bind_all('<KeyPress>', check_input)  # bind key press
canvas.bind_all('<KeyRelease>', end_input)  # bind all keys to circle

window.after(1000, end_title)  # destroy title and instructions
window.after(1000, make_candy)  # start making candy
window.after(1000, move_candy)  # start moving candy
window.after(1000, check_hits)  # check if character hit a candy
window.after(1000, move_character)  # handle keyboard controls

window.mainloop()
