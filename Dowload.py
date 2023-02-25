import pygame as pg
from Setting import SCREEN_WIDTH, SCREEN_HEIGH


# Image
background_img = pg.image.load('res/fon.png')
background_img = pg.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGH))

icon_img = pg.image.load("res/icon.ico")

