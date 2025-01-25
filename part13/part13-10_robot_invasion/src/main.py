# WRITE YOUR SOLUTION HERE:

from random import randint
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()

x = randint(0, 640-width)
y = 0

xvelocity = 0
yvelocity = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    # Update position
    x += xvelocity
    y += yvelocity

    if yvelocity > 0 and y+robot.get_height() >= 480:
        yvelocity = 0  # Stop moving down
        if y < 240:
            xvelocity = 1  # Start moving to the right
        else:
            xvelocity = -1  # Start moving to the left

    clock.tick(60)
    