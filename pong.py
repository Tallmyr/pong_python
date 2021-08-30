# Pygame template - skeleton for a new pygame project
import pygame
from sprites import Actor, Ball

WIDTH = 640
HEIGHT = 480
FPS = 60

FINALSCORE = 9


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Import Sounds
blip_sound = pygame.mixer.Sound("assets/blip.wav")

# Import Sprites
actors = pygame.sprite.Group()
player = Actor(WIDTH, HEIGHT, True)
opponent = Actor(WIDTH, HEIGHT, False)
actors.add(player, opponent)

balls = pygame.sprite.Group()
ball = Ball(WIDTH, HEIGHT)


# Set text
score_font = pygame.font.SysFont("Arial", 32)
menu_font = pygame.font.SysFont("Arial", 64)

# Vars
gameover = True
winner = ""


# Functions
def start():
    text = score_font.render("Press SpaceBar to Start", True, ("white"))
    text_width = text.get_width()
    screen.blit(text, ((WIDTH / 2) - (text_width / 2), (HEIGHT / 2) - 32))


def win(winner):
    text = score_font.render(str(winner) + " wins the round!", True, ("white"))
    text_width = text.get_width()
    screen.blit(text, ((WIDTH / 2) - (text_width / 2), (HEIGHT / 2) - 128))


def newgame():
    balls.add(ball)
    player.reset()
    opponent.reset()


def score(x, score):
    text = score_font.render(str(score), True, ("white"))
    screen.blit(text, (x, 30))


def play_sound(sound):
    pygame.mixer.Sound.play(sound)


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
        if gameover and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            gameover = False
            winner = ""
            newgame()

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
        play_sound(blip_sound)

    # Check Collision with Paddles
    collision = pygame.sprite.spritecollideany(ball, actors)
    if collision:
        ball.vx *= -1
        ball.vy += collision.vy / 3
        play_sound(blip_sound)

    # Check Score
    if ball.rect.x < 0:
        opponent.score += 1
        ball.reset("opponent")
    if ball.rect.x > WIDTH - 10:
        player.score += 1
        ball.reset("player")
    if opponent.score == FINALSCORE:
        gameover = True
        winner = "Computer"
    if player.score == FINALSCORE:
        gameover = True
        winner = "Player"

    # Update

    opponent.ai(ball.rect.y)
    actors.update()
    balls.update()

    # Draw / render
    screen.fill("black")

    if gameover:
        ball.kill()
        start()
        if winner != "":
            win(winner)

    score(50, player.score)
    score(WIDTH - 50, opponent.score)
    actors.draw(screen)
    balls.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
