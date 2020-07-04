import math 
from random import * 
import pgzrun  # 导入pgzero的模块运行工具pgzrun
# pgzrun会自动引入下列对象，但显式导入可以方便编辑器补全、提示
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.clock import clock
from pgzero.screen import Screen
from pgzero.rect import Rect 
screen: Screen  # 类型标注

import time  # 导入time模块
WIDTH = 1000 
HEIGHT = 1000 * 9 // 16 
ACCEL = 1.0 
DRAG = 0.9 
TRAIL_LENGTH = 2 
MIN_WRAP_FACTOR = 0.1 
BOUNDS = Rect(0,0,WIDTH,HEIGHT) 
FONT = 'eunomia_regular'

warp_factor = MIN_WRAP_FACTOR 
centerx = WIDTH // 2 
centery = HEIGHT // 2 
stars = [] 

class Star:
    __slots__ = (
        'pos','vel','brightness','speed','position_history' 
    )

    def __init__(self,pos,vel):
        self.pos = pos 
        self.vel = vel 
        self.brightness = 10 
        self.speed = math.hypot(*vel) 

    @property
    def end_pos(self):
        x,y = self.pos 
        vx,vy = self.vel 

        return (
            x - vx * warp_factor * TRAIL_LENGTH / 60,
            y - vy * warp_factor * TRAIL_LENGTH / 60,
        )

def f():
    return randint(0,255) 
lastc = (1,1,1) 
def draw_stars():
    global lastc 
    screen.clear() 
    
    color = (f(),f(),f()) 
    if randint(1,60) != 1:
        color = lastc 
    lastc = color 
    for star in stars:
        b = star.brightness 
        cur_color = (int(i*b/5) for i in color) 
        # color = (b*2,b*2,b*2) 
        # color = (1,111,11) 
        screen.draw.line(star.end_pos,star.pos,color) 


def update_stars(dt):
    global stars,warp_factor 
    warp_factor = (
        MIN_WRAP_FACTOR + (warp_factor - MIN_WRAP_FACTOR) * DRAG ** dt 
    )


    while len(stars) < 300:
        # Pick a direction and speed
        angle = uniform(-math.pi, math.pi)
        speed = 255 * uniform(0.3, 1.0) ** 2

        # Turn the direction into position and velocity vectors
        dx = math.cos(angle)
        dy = math.sin(angle)
        d = uniform(25 + TRAIL_LENGTH, 100)
        pos = centerx + dx * d, centery + dy * d
        vel = speed * dx, speed * dy

        stars.append(Star(pos, vel))

    # Update the positions of stars
    for s in stars:
        x, y = s.pos
        vx, vy = s.vel

        # Move according to speed and warp factor
        x += vx * warp_factor * dt
        y += vy * warp_factor * dt
        s.pos = x, y

        # Grow brighter
        s.brightness = min(s.brightness + warp_factor * 200 * dt, s.speed)

        # Get faster
        s.vel = vx * 2 ** dt, vy * 2 ** dt

    # Drop any stars that are completely off-screen
    stars = [
        star
        for star in stars
        if BOUNDS.collidepoint(star.end_pos)
    ]

# pgzrun.go() 