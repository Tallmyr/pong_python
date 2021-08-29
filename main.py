# Pygame template - skeleton for a new pygame project
import pygame
from sprites import Actor, Ball

WIDTH = 640
HEIGHT = 480
FPS = 60


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Import Sprites
actors = pygame.sprite.Group()
player = Actor(WIDTH, HEIGHT, True)
opponent = Actor(WIDTH, HEIGHT, False)
actors.add(player, opponent)

balls = pygame.sprite.Group()
ball = Ball(WIDTH, HEIGHT)
balls.add(ball)


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Key Inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or not keys[pygame.K_DOWN] and player.vy > 0:
        player.vy += -0.5
    elif keys[pygame.K_DOWN] or player.vy < 0:
        player.vy += 0.5

    # Game Logic

    # Check Collision with Walls
    if ball.rect.y < 0 or ball.rect.y > HEIGHT - 10:
        ball.vy *= -1

    # Check Collision with Paddles
    if pygame.sprite.spritecollideany(ball, actors):
        ball.vx *= -1

    # Check Score
    if ball.rect.x < 0:
        opponent.score += 1
        ball.reset("opponent")
    if ball.rect.x > WIDTH - 10:
        player.score += 1
        ball.reset("player")

    # Update
    actors.update()
    balls.update()

    # Draw / render
    screen.fill("black")
    actors.draw(screen)
    balls.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
