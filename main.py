import pygame as pg
from Setting import *
from Dowload import *

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))
pg.display.set_caption("Diary")
pg.display.set_icon(icon_img)
clock = pg.time.Clock()

def draw_game():
    screen.blit(background_img, (0, 0))

running = True
while running:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

    draw_game()

    clock.tick(FPS)
    pg.display.flip()
pg.quit()
