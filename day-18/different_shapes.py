from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("cyan")

color_list = ["green", "dark green", "forest green", "lime", "lime green", "light green", "pale green", "sea green",
              "medium sea green", "dark sea green", "spring green", "olive", "olive drab", "yellow", "light yellow",
              "gold", "goldenrod", "dark goldenrod", "khaki", "dark khaki", "blue", "dark blue", "light blue",
              "sky blue", "navy", "royal blue", "steel blue", "dodger blue", "cornflower blue", "cadet blue",
              "deep sky blue", "powder blue", "midnight blue", "aquamarine", "turquoise", "dark turquoise",
              "pale turquoise", "crimson", "dark red", "firebrick", "indian red", "maroon", "pink", "hot pink",
              "deep pink", "light pink", "pale violet red", "purple", "medium purple", "dark orchid",
              "dark violet", "blue violet", "magenta", "plum", "lavender", "thistle"]

def draw_shapes(number_of_sides):
    timmy.pencolor(random.choice(color_list))
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        timmy.forward(80)
        timmy.right(angle)

for i in range(3, 20):
    draw_shapes(i)


screen = Screen()
screen.exitonclick()