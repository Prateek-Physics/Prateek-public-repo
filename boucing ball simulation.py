import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)  # White
BALL_COLOR = (0, 0, 255)  # Blue
BALL_RADIUS = 20
GRAVITY = 0.5
BOUNCE_FACTOR = -0.7
MIN_SPEED = 1.8  # Minimum vertical velocity to consider the ball stopped

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Simulation")

# Ball properties
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 6, 0

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Apply gravity
    ball_speed_y += GRAVITY

    # Bounce off the edges
    if ball_x + BALL_RADIUS > WIDTH:
        ball_speed_x *= BOUNCE_FACTOR
        ball_x = WIDTH - BALL_RADIUS
    elif ball_x - BALL_RADIUS < 0:
        ball_speed_x *= BOUNCE_FACTOR
        ball_x = BALL_RADIUS

    if ball_y + BALL_RADIUS > HEIGHT:
        ball_speed_y *= BOUNCE_FACTOR
        ball_y = HEIGHT - BALL_RADIUS

        # Check if vertical velocity is very small and stop bouncing
        if abs(ball_speed_y) < MIN_SPEED:
            ball_speed_y = 0
            ball_speed_x=0

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(40)

