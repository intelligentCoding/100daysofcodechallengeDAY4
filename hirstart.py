import random
# import colorgram
import turtle as t


# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r, g, b)
#     rgb_colors.append(color)
# print(rgb_colors)
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(241, 228, 89), (24, 24, 61), (183, 73, 38), (144, 17, 31), (39, 29, 21),
              (214, 145, 85), (124, 159, 216), (204, 73, 115), (68, 26, 35), (55, 92, 138), (37, 45, 126),
              (23, 33, 23), (161, 21, 14), (142, 57, 80), (71, 78, 32), (67, 113, 74), (100, 98, 192),
              (141, 178, 161), (207, 77, 62), (144, 213, 191), (98, 168, 76), (192, 141, 156), (49, 85, 26),
              (156, 210, 221), (225, 172, 184), (175, 185, 221)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

dots_number = 100
for dot in range(1, dots_number + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot % 10 == 0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = t.Screen()
screen.exitonclick()


