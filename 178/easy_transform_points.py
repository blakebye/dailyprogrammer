# used trig for rotate()
import math

# collect starting point
x, y = map(float, raw_input("Give starting x and y, separated by a space: ").split())

# translate x, y by a, b
def translate(a, b):
    global x
    global y
    x += a
    y += b

# rotate x, y by c radians, clockwise around the point a, b
def rotate(a, b, c):
    global x
    global y
    delta_x = x - a
    delta_y = y - b
    hypot_length = (delta_x ** 2 + delta_y ** 2) ** .5
    # fixes divide by 0 with hardcoded cases
    if delta_x == 0:
        if delta_y == 0:
            return
        elif delta_y > 0:
            starting_angle = math.pi / 2
        else:
            starting_angle = 3 * math.pi / 2
    # do trig to find starting angle
    else:
        starting_angle = math.atan(delta_y / delta_x)
    # correct for quadrant 2 and quadrant 3 angles
    if delta_x < 0:
        starting_angle += math.pi
    # clockwise is negative radians
    new_angle = starting_angle - c
    y = b + math.sin(new_angle) * hypot_length
    x = a + math.cos(new_angle) * hypot_length

# reposition x, y linearly relative to a, b by scale of c
def scale(a, b, c):
    global x
    global y
    delta_x = x - a
    delta_y = y - b
    # you can scale x and y components independently
    x = a + (delta_x * c)
    y = b + (delta_y * c)

def reflect(axis):
    global x
    global y
    # just make the opposite component negative
    if axis == 'X':
        y = -y
    elif axis == 'Y':
        x = -x

def finish():
    print "(%f, %f)" % (x, y)
