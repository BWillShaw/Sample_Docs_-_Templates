import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_RADIUS = 15

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Not Pong due to copyright reasons')
clock = pygame.time.Clock()

# Initialize paddle and ball
paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
ball_dx, ball_dy = random.choice([-5, 5]), -5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 10
    if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - PADDLE_WIDTH:
        paddle_x += 10

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball-wall collision
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy

    # Ball-paddle collision
    if paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH and paddle_y <= ball_y <= paddle_y + PADDLE_HEIGHT:
        ball_dy = -ball_dy

    # Ball misses paddle
    if ball_y >= SCREEN_HEIGHT:
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ball_dy = -ball_dy

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

