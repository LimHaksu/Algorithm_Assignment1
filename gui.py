import pygame, sys
from pygame.locals import *

BOXSIZE = 40
GAPSIZE = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


def showMaze_final(original, explored,path, rows, cols):
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1300, 700), 0, 32)
    DISPLAYSURF.fill(YELLOW)
    pygame.display.set_caption('Maze')
    for j in range(rows):
        for i in range(cols):
            if original[j][i] == 0:
                pygame.draw.rect(DISPLAYSURF, WHITE, (i*(BOXSIZE+GAPSIZE), j*(BOXSIZE+GAPSIZE), BOXSIZE, BOXSIZE))
            else:
                pygame.draw.rect(DISPLAYSURF, BLACK, (i*(BOXSIZE+GAPSIZE), j*(BOXSIZE+GAPSIZE), BOXSIZE, BOXSIZE))
    for node in explored:
        pygame.draw.rect(DISPLAYSURF, GREEN, (node.x*(BOXSIZE+GAPSIZE), node.y*(BOXSIZE+GAPSIZE), BOXSIZE, BOXSIZE))

    for node in path:
        pygame.draw.rect(DISPLAYSURF, BLUE, (node.x*(BOXSIZE+GAPSIZE), node.y*(BOXSIZE+GAPSIZE), BOXSIZE, BOXSIZE))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()

def showMaze(original, explored, rows, cols):
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1300, 700), 0, 32)
    DISPLAYSURF.fill(YELLOW)
    pygame.display.set_caption('Maze')
    for j in range(rows):
        for i in range(cols):
            if original[j][i] == 0:
                pygame.draw.rect(DISPLAYSURF, WHITE, (i*(BOXSIZE+GAPSIZE), j*(BOXSIZE+GAPSIZE), BOXSIZE, BOXSIZE))
            else:
                pygame.draw.rect(DISPLAYSURF, BLACK, (i*(BOXSIZE+GAPSIZE), j*(BOXSIZE+GAPSIZE), BOXSIZE, BOXSIZE))
    for node in explored:
        pygame.draw.rect(DISPLAYSURF, GREEN, (node.x*(BOXSIZE+GAPSIZE), node.y*(BOXSIZE+GAPSIZE), BOXSIZE, BOXSIZE))

    #for node in path:
        #pygame.draw.rect(DISPLAYSURF, BLUE, (node.x*(BOXSIZE+GAPSIZE), node.y*(BOXSIZE+GAPSIZE), BOXSIZE, BOXSIZE))

#    while True:
#        for event in pygame.event.get():
#            if event.type == QUIT:
#                pygame.quit()
#                sys.exit()
    pygame.display.update()
