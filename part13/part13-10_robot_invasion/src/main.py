from random import randint
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

# List to store robots' positions and velocities
robots = []

clock = pygame.time.Clock()

# Timer for spawning robots
SPAWN_INTERVAL = 1000  # Spawn a robot every 1000ms (1 second)
last_spawn_time = pygame.time.get_ticks()


# Function to spawn a new robot at the top
def spawn_robot():
    width = robot.get_width()
    x = randint(0, 640 - width)  # Random x position
    y = 0  # Start at the top
    xvelocity = 0
    yvelocity = 1
    return {"x": x, "y": y, "xvelocity": xvelocity, "yvelocity": yvelocity}


while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Check if it's time to spawn a new robot
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > SPAWN_INTERVAL:
        robots.append(spawn_robot())  # Add a new robot
        last_spawn_time = current_time

    # Update and draw
    window.fill((0, 0, 0))  # Clear the screen
    for robot_data in robots:
        # Update positions
        robot_data["x"] += robot_data["xvelocity"]
        robot_data["y"] += robot_data["yvelocity"]

        # Draw the robot
        window.blit(robot, (robot_data["x"], robot_data["y"]))

        # Check if the robot has reached the bottom
        if robot_data["yvelocity"] > 0 and robot_data["y"] + robot.get_height() >= 480:
            robot_data["yvelocity"] = 0  # Stop moving down
            if robot_data["x"] > 320:
                robot_data["xvelocity"] = 1  # Move right if in the upper half
            else:
                robot_data["xvelocity"] = -1  # Move left if in the lower half

    pygame.display.flip()
    clock.tick(60)