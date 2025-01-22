# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()

window.fill((0, 0, 0))
for i in range(0,10):
    window.blit(robot,(75+width*i,100))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()