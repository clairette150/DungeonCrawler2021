import pygame


class Bar:
    def __init__(self, value, color, x, y, width, height, surface):
        pygame.draw.rect(surface, (1,0,0), (x,y,width,height))
        pygame.draw.rect(surface, color, (x,y,width,height/100*value))

