from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
def draw_arrow():
    global x, y
    x, y = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)

def follow_arrow():
    global x, y
    global char_x, char_y
    global right
    global stop
    if x >= char_x:
        right = True
    else:
        right = False

    if right == True:
        if char_x < x:
            char_x += 1
        if char_y < y:
            char_y += 1
        elif char_y > y:
            char_y -= 1
        if char_x == x and char_y == y:
            stop = True
    else:
        if char_x > x:
            char_x -= 1
        if char_y < y:
            char_y += 1
        elif char_y > y:
            char_y -= 1
        if char_x == x and char_y == y:
            stop = True

open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y= random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)
char_x, char_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

right = True
stop = False

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(x, y)
    follow_arrow()
    if right == True:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, char_x, char_y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, char_x, char_y)
    update_canvas()
    frame = (frame + 1) % 8
    if stop == True:
        draw_arrow()
        stop = False
    handle_events()

close_canvas()




