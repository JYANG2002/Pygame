import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption("Flappybird")
FPS = 60
clock = pygame.time.Clock()
gravity = 0
font = pygame.font.Font('Assets/04B_19.TTF', 50)
font2 = pygame.font.Font('Assets/04B_19.TTF', 30)
game_over = False
score = 0

# Images
background = pygame.transform.scale(pygame.image.load("Assets/city_background.png"), (500, 600)).convert_alpha()
background_rec = background.get_rect(topleft=(0, 0))
ground = pygame.transform.scale(pygame.image.load("Assets/ground_background.png"), (600, 110)).convert()
ground_rec = ground.get_rect()
ground_rec.left = 0
ground_rec.bottom = 700
pause = True

# bird
bird = pygame.image.load("Assets/bluebird.png").convert_alpha()
bird_up = pygame.image.load("Assets/up.png").convert_alpha()
bird_down = pygame.image.load("Assets/down.png").convert_alpha()
bird_rec = bird.get_rect(center=(50, 300))
image = bird

# pipe: have at least 150 pixels between two pipes
pipe = pygame.image.load("Assets/pipe-green.png").convert_alpha()
pipe = pygame.transform.scale(pipe, (52, 250))
pipe_rec = pipe.get_rect(bottom=590)
pipe_rec.left = 350

pipe2 = pygame.transform.flip(pygame.image.load("Assets/pipe-green.png").convert_alpha(), False, True)
pipe2 = pygame.transform.scale(pipe2, (52, 200))
pipe2_rec = pipe2.get_rect(bottom=200)
pipe2_rec.left = 350

# Sound effects
point = pygame.mixer.Sound("Assets/audio_point.wav")
jump = pygame.mixer.Sound("Assets/audio_wing.wav")
die1 = pygame.mixer.Sound("Assets/audio_hit.wav")
die2 = pygame.mixer.Sound("Assets/audio_die.wav")


def draw(image):
    score_text = font.render("Score:" + str(score), False, (0, 0, 0))
    score_rec = score_text.get_rect(center=(200, 150))
    screen.blit(background, background_rec)
    screen.blit(ground, ground_rec)
    screen.blit(score_text, score_rec)
    screen.blit(image, bird_rec)
    screen.blit(pipe, pipe_rec)
    screen.blit(pipe2, pipe2_rec)


while True:
    clock.tick(FPS)
    for event in pygame.event.get():  # Get a list of all different events
        if event.type == pygame.QUIT:  # Quit the game
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pause:  # Start the game
                pause = False
            if event.key == pygame.K_SPACE:  # Make bird jump
                gravity = -9.5
                jump.play()
            if event.key == pygame.K_SPACE and game_over:  # If the game is over, restart by pressing space
                game_over = False
                gravity = 0
                bird_rec.bottom = 200
                pipe_rec.bottom = 590
                pipe_rec.left = 350
                pipe2_rec.left = 350
                pipe2_rec.top = 0
                score = 0
    if pause:  # First time
        draw(image)
        start_msg = font2.render("Press Space To Play", False, (0, 0, 0))
        start_msg_rec = start_msg.get_rect(center=(200, 350))
        screen.blit(start_msg, start_msg_rec)
    elif game_over:  # When dead
        end_message = font.render("Game Over", False, (0, 0, 0))
        end_message_rect = end_message.get_rect(center=(200, 350))
        end_message2 = font2.render("Press Space To Restart", False, (0, 0, 0))
        end_message2_rect = end_message2.get_rect(center=(200, 400))
        screen.blit(end_message, end_message_rect)
        screen.blit(end_message2, end_message2_rect)
    else:  # Game active
        #  Make it seem like the ground is moving
        ground_rec.left -= 5
        if ground_rec.left == -210:
            ground_rec.left = 0
        # Make pipe move
        pipe_rec.left -= 5
        pipe2_rec.left -= 5
        if pipe_rec.right == -3:
            num = random.randint(1, 6) * 50
            pipe = pygame.transform.scale(pipe, (52, 100 + num))
            pipe_rec = pipe.get_rect(bottom=590)
            pipe2 = pygame.transform.scale(pipe2, (52, 350 - num))
            pipe2_rec = pipe2.get_rect(top=0)
            pipe_rec.left = 400
            pipe2_rec.left = 400
        # Keep track of score
        if pipe_rec.right == 67:
            score += 1
            point.play()
        # Somewhat animation
        if gravity < 0:
            image = bird_up
        else:
            image = bird_down
        # If bird touches ground it show end screen
        if bird_rec.bottom < 590 and not pipe_rec.colliderect(bird_rec) and not pipe2_rec.colliderect(bird_rec):
            gravity += 0.6
            bird_rec.bottom += gravity
        else:
            game_over = True
            die1.play()
            die2.play()
        draw(image)
    pygame.display.update()