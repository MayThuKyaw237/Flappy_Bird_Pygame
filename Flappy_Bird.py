import pygame
import random

pygame.init()

# SCREEN SETUP
WIDTH, HEIGHT = 650, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# COLORS
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# FONT
font = pygame.font.SysFont(None, 48)
START = 0
PLAYING = 1
GAME_OVER = 2
game_state = START

bird_y = 300
speed = 0
pipe_x = WIDTH
pipe_top_height = 200

score = 0
# RESET GAME FUNCTION
def reset_game():
    global bird_y, speed, pipe_x, pipe_top_height, score, game_state
    bird_y = 300
    speed = 0
    pipe_x = WIDTH
    pipe_top_height = random.randint(100, 300)
    score = 0
    game_state = PLAYING

# BIRD SETTINGS
bird_x = 100
bird_size = 30
gravity = 1

# PIPE SETTINGS
pipe_width = 60
gap = 150

# START GAME
# reset_game()
running = True

# GAME LOOP
while running:

    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN and game_state == START:
                reset_game()

            if event.key == pygame.K_SPACE and game_state == PLAYING:
                speed = -10

            if event.key == pygame.K_r and game_state == GAME_OVER:
                reset_game()
            
            if event.key == pygame.K_ESCAPE:
                running = False

    #GAME LOGIC
    if game_state == PLAYING:
        speed += gravity
        bird_y += speed

        pipe_x -= 3
        if pipe_x < -pipe_width:
            pipe_x = WIDTH
            pipe_top_height = random.randint(100, 300)
            score += 1

        bird_rect = pygame.Rect(bird_x, bird_y, bird_size, bird_size)
        top_pipe = pygame.Rect(pipe_x, 0, pipe_width, pipe_top_height)
        bottom_pipe = pygame.Rect(
            pipe_x,
            pipe_top_height + gap,
            pipe_width,
            HEIGHT
        )

        if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
            game_state = GAME_OVER

        if bird_y < 0 or bird_y + bird_size > HEIGHT:
            game_state = GAME_OVER

    #DRAW
    screen.fill(BLUE)

    if game_state != START:
        pygame.draw.rect(screen, RED, bird_rect)
        pygame.draw.rect(screen, GREEN, top_pipe)
        pygame.draw.rect(screen, GREEN, bottom_pipe)

    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    if game_state == START:
        text = font.render("Press ENTER to Start", True, BLACK)
        screen.blit(text, (140, 350))

    if game_state == GAME_OVER:
        text = font.render("GAME OVER", True, BLACK)
        screen.blit(text, (190, 330))

        hint = pygame.font.SysFont(None, 30).render(
            "Press R to Restart", True, BLACK
        )
        screen.blit(hint, (210, 380))

    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
