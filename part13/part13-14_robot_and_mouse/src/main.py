# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()

window_width, window_height = 640, 480

window = pygame.display.set_mode((window_width, window_height))
robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

robot_x = random.randint(0, window_width - width)
robot_y = random.randint(0, window_height - height)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left-click (button 1)
            mouse_x, mouse_y = event.pos  # Get mouse click position
            
            # Check if the click is inside the robot's area
            if robot_x <= mouse_x <= robot_x + width and robot_y <= mouse_y <= robot_y + height:
                robot_x = random.randint(0, window_width)
                robot_y = random.randint(0, window_height)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)