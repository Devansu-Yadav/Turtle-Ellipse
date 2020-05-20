import turtle
import math


def ellipse(a, b, angle, angle_unit):
    myturtle = turtle.Turtle()

    if angle_unit == 'd':
        r = angle * 0.875
    # We are multiplying by 0.875 because for making a complete ellipse we are plotting 315 pts according
    # to our parametric angle value

    elif angle_unit == "r":
        r = (angle * 0.875 * 57.296)
    # Converting radian to degrees.

    for i in range(int(r)):
        if i == 0:
            myturtle.up()
        else:
            myturtle.down()
        myturtle.setposition(a*math.cos(i/50), b*math.sin(i/50))
# Angle unit can be degree or radian


turtle.done()