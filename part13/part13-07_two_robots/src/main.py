import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")

x1 = 0
x2 = 0

velocity1 = 1
velocity2 = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot1, (x1, 50))
    window.blit(robot2, (x2, 150))
    pygame.display.flip()
    
    x1 += velocity1
    x2 += velocity2
    if velocity1 > 0 and x1+robot1.get_width() >= 640:
        velocity1 = -velocity1
    if velocity1 < 0 and x1 <= 0:
        velocity1 = -velocity1
    if velocity2 > 0 and x2+robot1.get_width() >= 640:
        velocity2 = -velocity2
    if velocity2 < 0 and x2 <= 0:
        velocity2 = -velocity2

    clock.tick(60)