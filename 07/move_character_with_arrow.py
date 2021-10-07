from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

def update_character():
    global x, y
    global char_x, char_y

    char_x = (1-0.01)*char_x + 0.01 * x
    char_y = (1 - 0.01) * char_y + 0.01 * y

    dist = (x-char_x)**2 + (y-char_y)**2
    if dist < 10**2:
        x, y = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)

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

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(x, y)
    update_character()
    if right == True:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, char_x, char_y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, char_x, char_y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()




