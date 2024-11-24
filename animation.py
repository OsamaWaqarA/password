import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Padlock")

# Colors
red = (255, 0, 0)
yellow = (255, 255, 0)

# Padlock parameters
side_length = 200
angle = 170
iterations = 0

# Starting position
x, y = width // 2, height // 2

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the pattern
    pygame.draw.line(screen, red, (x, y), (x + int(side_length * pygame.math.Vector2(1, 0).rotate(angle).x), y + int(side_length * pygame.math.Vector2(1, 0).rotate(angle).y)))

    # Calculate new position and angle
    x += int(side_length * pygame.math.Vector2(1, 0).rotate(angle).x)
    y += int(side_length * pygame.math.Vector2(1, 0).rotate(angle).y)

    # Update the angle
    angle = (angle + 170) % 360

    # Check for completion
    iterations += 1
    if iterations >= 3000:
        break

    # Update the display
    pygame.display.flip()

# Control the frame rate
pygame.time.delay(2000)  # Delay for 2 seconds before quitting
pygame.quit()
sys.exit()
