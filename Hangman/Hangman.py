import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Hangman")
font = pygame.font.Font('arial.ttf', 30)
text = font.render('Enter a letter:', True, 'Black')
textRect = text.get_rect()
textRect.midleft = (330, 190)
chances = 6  # There are 6 chances to get it wrong
usedw = []
usedrec = []
correct_text = []
correct_rec = []
used_letter = []
num = 0
a = random.randint(0, 5)
f = open("words.txt", 'r')
r = f.readlines()
stripped = list(map(str.strip, r))
original_word = stripped[a]
f.close()


loser = pygame.mixer.Sound('Lose.wav')
winner = pygame.mixer.Sound('congrats.wav')


def end():
    pygame.quit()
    exit()


def draw(chance, word, letter, num):
    a = "abcdefghijklmnopqrstuvwxyz"
    screen.fill((255, 255, 255))  # Fill screen white
    pygame.draw.line(screen, 'Black', (200, 50), (200, 250), 5)
    pygame.draw.line(screen, 'Black', (150, 250), (250, 250), 5)
    pygame.draw.line(screen, 'Black', (198, 50), (260, 50), 5)
    pygame.draw.line(screen, 'Black', (260, 50), (260, 70), 5)

    # Body parts
    if chance < 6:
        pygame.draw.circle(screen, 'Black', (260, 100), 30, 5)
    if chance < 5:
        pygame.draw.line(screen, 'Black', (260, 130), (260, 200), 5)
    if chance < 4:
        pygame.draw.line(screen, 'Black', (260, 140), (300, 130), 5)
    if chance < 3:
        pygame.draw.line(screen, 'Black', (260, 140), (220, 130), 5)
    if chance < 2:
        pygame.draw.line(screen, 'Black', (260, 200), (220, 230), 5)
    if chance < 1:
        pygame.draw.line(screen, 'Black', (260, 200), (300, 230), 5)

    # Display lines of hidden word
    for i in range(len(word)):
        p1 = (330 + i * 60, 140)
        p2 = (370 + i * 60, 140)
        pygame.draw.line(screen, 'Black', p1, p2, 5)  # Starting point for first row

    screen.blit(text, textRect)
    t = font.render(letter, True, 'Black')

    if letter in word and letter not in used_letter:
        l = check_word(letter, word)
        for i in l:
            trec = t.get_rect()
            trec.midleft = (340 + i * 60, 110)
            correct_text.append(font.render(original_word[i], True, 'Black'))
            correct_rec.append(trec)

    if letter in a and letter not in used_letter:
        trec = t.get_rect()
        trec.midleft = (50 + num * 50, 300)
        usedw.append(font.render(letter, True, 'Black'))
        usedrec.append(trec)

    for i in range(len(correct_text)):
        screen.blit(correct_text[i], correct_rec[i])

    #  Draw out the used words
    for i in range(len(usedw)):
        screen.blit(usedw[i], usedrec[i])

    used_letter.append(letter)
    pygame.display.update()


# Return list of num of index that matches the letter to word
def check_word(letter, word):
    lw = list(word)
    l = []
    index = 0
    for i in lw:
        if i.lower() == letter:
            l.append(index)
        index += 1
    return l


while True:
    word = original_word.lower()
    letter = chr(32)
    for event in pygame.event.get():  # Get a list of all different events
        if event.type == pygame.QUIT:  # Quit the game
            end()
        if event.type == pygame.KEYDOWN:  # If a key is pressed
            letter = chr(event.key)
            if letter not in used_letter:
                num += 1
            if letter not in word:
                chances -= 1
    screen.fill((135, 206, 235))

    if len(correct_rec) == len(original_word):
        winner.play()
        pygame.time.wait(5000)
        end()

    else:
        draw(chances, word, letter, num)
        if chances == 0:
            loser.play()
            pygame.time.wait(5000)
            end()
