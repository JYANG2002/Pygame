import random
import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Initalize the sprite class
        player_walk_1 = pygame.image.load('Runner_graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('Runner_graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('Runner_graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]  # Image and rect are required in this sprite
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('Runner_audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
                self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()  # Required for pygame

        if type == 'fly':
            fly_1 = pygame.image.load('Runner_graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('Runner_graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('Runner_graphics/snail/snail1.png').convert_alpha()  # remove alpha values
            snail_2 = pygame.image.load('Runner_graphics/snail/snail2.png').convert_alpha()  # remove alpha values
            self.frames = [snail_1, snail_2]
            y_pos = 300
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()  # Kill destroy this obstacle sprite


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time  # Give our time in milliseconds
    score_surf = test_font.render(f'Score:{current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        # Copy existing item of list if x is greater than -100
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:  # Jump
        player_surf = player_jump
    else:  # Walk
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


pygame.init()  # Starts pygame
screen = pygame.display.set_mode((800, 400))  # Width 800 pixels height 400 pixels size screen
pygame.display.set_caption("Runner")  # Set title
clock = pygame.time.Clock()  # Create a clock object
test_font = pygame.font.Font('Runner_font/Pixeltype.ttf', 50)  # Create a text
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('Runner_audio/music.wav')
bg_music.play(loops=-1)  # Play this song forever

player = pygame.sprite.GroupSingle()
player.add(Player())  # Have a group contain the sprite to access it

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('Runner_graphics/Sky.png').convert()  # the .convert() helps pygame run easier
ground_surface = pygame.image.load('Runner_graphics/ground.png').convert()

# Obstacles
snail_frame_1 = pygame.image.load('Runner_graphics/snail/snail1.png').convert_alpha()  # remove alpha values
snail_frame_2 = pygame.image.load('Runner_graphics/snail/snail2.png').convert_alpha()  # remove alpha values
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

fly_frame1 = pygame.image.load('Runner_graphics/Fly/Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('Runner_graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('Runner_graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('Runner_graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('Runner_graphics/Player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))  # Takes the surface and draws a rectangle around it
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('Runner_graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 330))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:  # since the screen displays once for a second, a while true will keep the screen up
    for event in pygame.event.get():  # Get a list of event and loop through them
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # Use sys to exit without an error message
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:  # if mouse is pressed
                if player_rect.collidepoint(
                        event.pos) and player_rect.bottom >= 300:  # clicking on player makes them jump
                    player_gravity = -20
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:  # If a key is pressed
                if event.key == pygame.K_SPACE:  # If the key pressed is space
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active:
        screen.blit(sky_surface, (0, 0))  # Blit is block image transfer to have one surface to another
        screen.blit(ground_surface, (0, 300))  # Blit draws in order so it sometimes overwrite
        score = display_score()

        # Player
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()
        game_active = collision_sprite()

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        if score == 0:  # If you just started the game
            screen.blit(game_name, game_name_rect)
            screen.blit(game_message, game_message_rect)
        else:  # If you already played the game
            screen.blit(score_message, score_message_rect)

    pygame.display.update()  # update anything we have drawn and display to the player
    clock.tick(60)  # Saying that this while true loop cannot go faster than 60 frames per second
