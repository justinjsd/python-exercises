import pygame
import math
import time

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 180
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(time.strftime("%H:%M:%S"))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Function to calculate hand positions
def get_hand_position(angle, length):
    rad = math.radians(angle)
    x = CENTER[0] + length * math.cos(rad)
    y = CENTER[1] - length * math.sin(rad)
    return int(x), int(y)

running = True
while running:
    screen.fill(BLACK)
    
    # Draw clock border
    pygame.draw.circle(screen, RED, CENTER, RADIUS, 3)
    
    # Get current time
    current_time = time.strftime("%H:%M:%S")
    pygame.display.set_caption(current_time)

    hours = int(time.strftime("%I"))  # 12-hour format
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # Calculate angles (adjusted for clock rotation)
    sec_angle = 90 - (seconds * 6)
    min_angle = 90 - (minutes * 6)
    hour_angle = 90 - ((hours % 12) * 30 + minutes * 0.5)

    # Draw hands
    pygame.draw.line(screen, BLUE, CENTER, get_hand_position(hour_angle, RADIUS * 0.5), 5)
    pygame.draw.line(screen, BLUE, CENTER, get_hand_position(min_angle, RADIUS * 0.7), 3)
    pygame.draw.line(screen, BLUE, CENTER, get_hand_position(sec_angle, RADIUS * 0.9), 1)

    pygame.draw.circle(screen, RED, CENTER, 8)  # Center point

    # Refresh display
    pygame.display.flip()
    
    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limit frame rate
    pygame.time.delay(1000)

pygame.quit()