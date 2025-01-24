# WRITE YOUR SOLUTION HERE:
 
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
xvelocity = 1  # Start moving right
yvelocity = 0  # No vertical movement initially
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))  # Clear the screen with black
    window.blit(robot, (x, y))  # Draw the robot
    pygame.display.flip()  # Update the display

    # Move the robot
    x += xvelocity
    y += yvelocity

    # Change direction when reaching the boundaries
    if x + robot.get_width() >= 640 and yvelocity == 0:  # Right wall
        xvelocity = 0
        yvelocity = 1
    elif y + robot.get_height() >= 480 and xvelocity == 0:  # Bottom wall
        xvelocity = -1
        yvelocity = 0
    elif x <= 0 and yvelocity == 0:  # Left wall
        xvelocity = 0
        yvelocity = -1
    elif y <= 0 and xvelocity == 0:  # Top wall
        xvelocity = 1
        yvelocity = 0

    clock.tick(60)  # Limit the frame rate to 60 FPS