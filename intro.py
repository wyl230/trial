# import pgzrun
# # from pgzero import screen
# # from pgzrun import *
# # from pgzero.actor import *
# # from pgzero.animation import *
# # # from pgzero.__main__ import *
# # from pgzero.builtins import *
# # # from pgzero.builtins import *
# # # from pgzero.builtins import *
# # from pgzero.game import *
# from import * 
# WIDTH = 1200
# HEIGHT = 800
# alien = Actor('718',)
# alien.pos = 0, 0
# t = 333
# colors = [(128, 1, 1), (123, 123, 342)]
# box = [Rect((20, 20), (100, 100))]

# role1 = Actor('rec') 
# def draw():
#     screen.clear()
#     screen.draw.line((111, 111), (t, t), (111, 111, 111))
#     screen.draw.rect(box[0], colors[0])
#     # screen.blit('719',(10,50))
#     # screen.fill((128,0,0))
#     role1.draw() 
#     alien.draw()


# def update():
#     global t
#     alien.left += 5  
#     role1.left += 9 
#     t += 3
#     if alien.left > WIDTH or role1.left > WIDTH:
#         alien.right = 0
#         role1.right = 0


# def p():
#     print(12)


# def on_mouse_down(pos, button):
#     if alien.collidepoint(pos):
#         clock.schedule_unique(p, 1.0)
#     else:
#         clock.schedule_unique(p, 1.0)


import math 
from stars import * 
from random import * 
import pgzrun 





def draw():
    draw_stars() 

    
def update(dt):
    update_stars(dt) 
    

# Jump-start the star field
# for _ in range(30):
#     update(0.5)
# for _ in range(5):
#     update(1 / 60)
pgzrun.go()