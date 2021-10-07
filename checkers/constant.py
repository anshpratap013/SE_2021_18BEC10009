import pygame

WIDTH,HEIGGHT = 800,800
ROWS,COLS = 5,5
SQUARE_SIZE = WIDTH//COLS

#rgb
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,255,0)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44,25))
