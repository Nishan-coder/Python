import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# Set up colors
blue = (0, 0, 255)
red = (255, 0, 0)

# Set up the rectangle
rect_width, rect_height = 50, 50
rect_x, rect_y = (width - rect_width) // 2, (height - rect_height) // 2
rect_speed = 5
rect_color = blue

# Set up the circle
circle_radius = 20
circle_x, circle_y = width // 2, height // 2
circle_color = red

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Change circle color on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Move the rectangle based on arrow keys
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Update circle position to follow the mouse cursor
    circle_x, circle_y = pygame.mouse.get_pos()

    # Draw background
    screen.fill((255, 255, 255))

    # Draw rectangle with the selected color
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Draw circle with the selected color
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Update display
    pygame.display.flip()

    # Set frames per second
    pygame.time.Clock().tick(60)
