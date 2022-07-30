# import colorgram
# colors = colorgram.extract('hirst.jpg', 30)
# # print(colors)
#
# rgb_colours = []
# for col in colors:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     rgb_matrix = (r, g, b)
#     rgb_colours.append(rgb_matrix)
#
# print(rgb_colours)

import turtle
import random

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
              (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
              (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203),
              (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

turtle.colormode(255)
aklu = turtle.Turtle()
aklu.speed("fastest")
aklu.penup()
aklu.hideturtle()

aklu.setheading(225)
aklu.forward(300)
aklu.setheading(0)

for here in range(10):
    aklu.dot(20, random.choice(color_list))
    for _ in range(9):
        aklu.forward(50)
        aklu.dot(20, random.choice(color_list))
    aklu.backward(450)
    aklu.left(90)
    aklu.forward(50)
    aklu.right(90)

my_screen = turtle.Screen()
my_screen.exitonclick()
