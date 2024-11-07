

from turtle import *        # importing everything(*) from turtle library

# setting for balloon size and colors
balloon_diameter = 50       # diameter of balloon
balloon_pop_diameter = 130  # diameter of balloon in its maximum size
balloon_colors = ["green", "red", "yellow"]  # Color selection for balloons
color_index = 0             # Index to keep track of the current balloon color
inflation_rate = 10         # Amount the balloon inflates per key press


def create_balloon():       # Creating function to draw balloon
    color(balloon_colors[color_index])          # choosing different color for the balloon
    dot(balloon_diameter)   # dot draws a circle with the given diameter parameter

def pump_balloon():         # creating function to inflate balloon
    global balloon_diameter, color_index # accessing outside variable to use inside using global and color index for choosing different colors 
    balloon_diameter += inflation_rate  # increasing balloon size by +10
    create_balloon()        # drawing balloon after

    if balloon_diameter >= balloon_pop_diameter:    # using conditions to make the balloon pop when it reaches certain size
        clear()             # removes / clears the drawing to dissapear the balloon
        balloon_diameter = 40   # making diameter back to 40
        write("Popped!", align="center")    # it shows "popped!" in the screen in center

        # Move to the next color in the sequence (green to red to yellow)
        color_index = (color_index + 1) % len(balloon_colors)  # Cycle through colors

# function to deflate the balloon
def deflate_balloon():
    global balloon_diameter
    balloon_diameter -= inflation_rate      # decreasing the balloon size
    if balloon_diameter < 40:               # prevents the balloon fron going below 40 
        balloon_diameter = 40

    clear()                                 # clears the screen before drawing deflated balloon
    create_balloon()    # redraws the balloon with updated size

# Creating function to adjust the balloon size each time button is pressed
def adjust_inflation_rate(amount):
    global inflation_rate
    inflation_rate = amount     # setting the inflation rate to the given amount

# initial setup to create first balloon and listen to "UP" key press
create_balloon()

onkey(pump_balloon, "Up")   # Up key listens to the pump_balloon function to inflate balloon
onkey(deflate_balloon, "Down")  # Down key deflates the balloon
onkey(lambda: adjust_inflation_rate(5), "Right")    # change inflation when pressed Right key
onkey(lambda: adjust_inflation_rate(15), "Left")    # change inflation when pressed Left key

listen()                    # it listens key press



done()
 
