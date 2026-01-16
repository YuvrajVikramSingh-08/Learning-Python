import random
import turtle as t

color_list = ["green", "dark green", "forest green", "lime", "lime green", "light green", "pale green", "sea green",
              "medium sea green", "dark sea green", "spring green", "olive", "olive drab", "yellow", "light yellow",
              "gold", "goldenrod", "dark goldenrod", "khaki", "dark khaki", "blue", "dark blue", "light blue",
              "sky blue", "navy", "royal blue", "steel blue", "dodger blue", "cornflower blue", "cadet blue",
              "deep sky blue", "powder blue", "midnight blue", "aquamarine", "turquoise", "dark turquoise",
              "pale turquoise", "crimson", "dark red", "firebrick", "indian red", "maroon", "pink", "hot pink",
              "deep pink", "light pink", "pale violet red", "purple", "medium purple", "dark orchid",
              "dark violet", "blue violet", "plum", "lavender", "thistle"]

timmy = t.Turtle()
timmy.shape("turtle")
t.colormode(255)
timmy.speed("fastest")
timmy.pensize(10)

direction = [0, 90, 180, 270]

def random_walk(n):
    for i in range(n):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        timmy.setheading(random.choice(direction))
        timmy.forward(20)
        timmy.pencolor(random_color)

random_walk(300)

screen = t.Screen()
screen.exitonclick()
