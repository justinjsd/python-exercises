# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_width, window_height = 640, 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png") 

width = robot.get_width()
height = robot.get_height()

#FIRST ROBOT
x1 = window_width-width
y1 = 0

velocity = 3

#FIRST ROBOT
to_right1 = False
to_left1 = False
to_up1 = False
to_down1 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #FIRST ROBOT
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_UP:
                to_up1 = True
            if event.key == pygame.K_DOWN:
                to_down1 = True

        if event.type == pygame.KEYUP:
            #FIRST ROBOT
            if event.key == pygame.K_RIGHT:
                to_right1 = False
            if event.key == pygame.K_LEFT:
                to_left1 = False
            if event.key == pygame.K_UP:
                to_up1 = False
            if event.key == pygame.K_DOWN:
                to_down1 = False

        if event.type == pygame.QUIT:
            exit()

    #FIRST ROBOT
    if to_right1:
        if x1 < window_width - width:
            x1 += velocity
    if to_left1:
        if x1 > 0:
            x1 -= velocity
    if to_up1:
        if y1 > 0:
            y1 -= velocity
    if to_down1:
        if y1 < window_height - height:
            y1 += velocity

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    pygame.display.flip()

    clock.tick(60)