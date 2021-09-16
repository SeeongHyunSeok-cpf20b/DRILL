import math
import random
from pico2d import *



open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def move_rec():
    lap = 0
    x = 400
    y = 90
    while lap < 1:
        clear_canvas_now()
        grass.draw_now(400, 30)
        if (y == 90 and 20 <= x and x<780):
            character.draw_now(x ,y)
            x+=2
            if (x == 400):
                lap += 1
        elif (x == 780 and 90 <= y and y < 550):
            character.draw_now(x ,y)
            y+=2
        elif (y == 550 and 20 < x and x <= 780):
            character.draw_now(x ,y)
            x-=2
        elif (x == 20 and 90 < y and y <= 550):
            character.draw_now(x ,y)
            y-=2
        delay(0.01)


radius = 200

def convert_to_pi(ang):
    return ang / 360 * 2 * math.pi

def calculate_loc_x(ang):
    x = 400 + radius * math.sin(convert_to_pi(ang))
    return x

def calculate_loc_y(ang):
    y = 90 + radius - radius * math.cos(convert_to_pi(ang))
    return y
    
    
def move_cir():
    angle = 0
    while angle < 360:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(calculate_loc_x(angle),calculate_loc_y(angle))
        angle +=2
        delay(0.01)


grass.draw_now(400, 30)
character.draw_now(400 ,90)
while True:
    num = random.randint(0,1)
    if (num == 0):
        move_rec()
    else :
        move_cir()


    

