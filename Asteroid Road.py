import pygame
from pygame import *
from random import randint


class Asteroid:
    colour = '#757799'
    size = 20
    v = 0


class GoldenAsteroid:
    colour = '#494024'
    size = 15
    v = -5


def GivePos(D):
    a, b = randint(0, 800), randint(0, 640)
    for i in D:
        x, y = i
        if (a - x) < 50 and (b - y) < 50:
            a, b = randint(0, 800), randint(0, 640)
    x, y = D[0]
    if (a - x) < 50 and (b - y) < 50:
        a, b = randint(0, 800), randint(0, 640)


WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#1d1e33"


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Asteroid Road")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))
    running = True
    x_pos = 200
    v = 20
    while running:
        for i in pygame.event.get():
            if i.type == QUIT:
                raise SystemExit
            screen.blit(bg, (0, 0))
            Asteroid_Count = 0
            pygame.draw.circle(screen, Asteroid.colour, (200, 200), Asteroid.size)
            pygame.draw.circle(screen, GoldenAsteroid.colour, (400, 200), GoldenAsteroid.size)
            pygame.display.update()


if __name__ == "__main__":
    main()
