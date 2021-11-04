from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90  #위치 정함
        self.image = load_image('run_animation.png')
        self.frame = 0

    def update(self):
        self.x += 5
        self.frame = (self.frame+1)%8

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 599  #위치 정함
        self.shape = random.randint(0,1)
        if self.shape == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.vel = random.randint(20,50)

    def update(self):
        if self.y > 40:
            self.y -= self.vel
        else:
            self.y = 40

    def draw(self):
        self.image.draw(self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()

team = [Boy() for i in range(1,11+1)]
balls = [Ball() for i in range(1, 20+1)]


running = True
# game main loop code

while running:
    handle_events()

    #game logic
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

    #game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.05)


# finalization code
close_canvas()