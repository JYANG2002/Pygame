import pygame
import time
pygame.init()
screen = pygame.display.set_mode((400, 400))
board = [  # 0 is empty, 1 is X, 2 is O
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
lx = []
lo = []
turn = False  # True is x False is y
state = 0  # 0 is intro screen, 1 is game screen, 2 is game end
s1 = pygame.Rect(95, 95, 95, 95)
s1.topleft = (51, 51)
s2 = pygame.Rect(95, 95, 95, 95)
s2.topleft = (154, 51)
s3 = pygame.Rect(95, 95, 95, 95)
s3.topleft = (255, 51)
s4 = pygame.Rect(95, 95, 95, 95)
s4.topleft = (51, 154)
s5 = pygame.Rect(95, 95, 95, 95)
s5.topleft = (154, 154)
s6 = pygame.Rect(95, 95, 95, 95)
s6.topleft = (255, 154)
s7 = pygame.Rect(95, 95, 95, 95)
s7.topleft = (51, 255)
s8 = pygame.Rect(95, 95, 95, 95)
s8.topleft = (154, 255)
s9 = pygame.Rect(95, 95, 95, 95)
s9.topleft = (255, 255)

x = pygame.transform.scale(pygame.image.load("Assets/x.png"), (95, 95)).convert_alpha()
o = pygame.transform.scale(pygame.image.load("Assets/o.png"), (85, 85)).convert_alpha()
x_rec = x.get_rect(center=(100, 100))

font = pygame.font.Font('Assets/arial.ttf', 30)
winner_text = "Hello"

def draw():
    screen.fill((3, 252, 240))
    pygame.draw.line(screen, "black", (50, 150), (350, 150), 10)
    pygame.draw.line(screen, "black", (50, 250), (350, 250), 10)
    pygame.draw.line(screen, "black", (150, 50), (150, 350), 10)
    pygame.draw.line(screen, "black", (250, 50), (250, 350), 10)


def solution(board):
    global winner_text
    choice = board[0][0]  # Check diagonally
    if board[1][1] == choice and board[2][2] == choice and choice != 0:
        if choice == 1:
            winner_text = "The winner is Player X!"
        else:
            winner_text = "The winner is Player O!"
        return True
    choice = board[0][2]
    if board[1][1] == choice and board[2][0] == choice and choice != 0:
        if choice == 1:
            winner_text = "The winner is Player X!"
        else:
            winner_text = "The winner is Player O!"
        return True
    for i in board:  # check horizontally
        if i[0] == i[1] == i[2] and i[0] != 0:
            if i[0] == 1:
                winner_text = "The winner is Player X!"
            else:
                winner_text = "The winner is Player O!"
            return True
    for i in range(3):  # check vertically
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            if board[0][i] == 1:
                winner_text = "The winner is Player X!"
            else:
                winner_text = "The winner is Player O!"
            return True
    return False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and state == 0:
            if text_rec2.collidepoint(event.pos):
                state = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == 2 and text_rec2.collidepoint(event.pos):
                lo.clear()
                lx.clear()
                board = [  # 0 is empty, 1 is X, 2 is O
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
                state = 1
            if state == 2 and text_rec3.collidepoint(event.pos):
                pygame.quit()
                exit()
            if s1.collidepoint(event.pos) and board[0][0] == 0:
                if turn:
                    lx.append(x.get_rect(center=(100, 100)))
                    turn = False
                    board[0][0] = 1
                else:
                    lo.append(o.get_rect(center=(100, 100)))
                    turn = True
                    board[0][0] = 2
            if s2.collidepoint(event.pos) and board[0][1] == 0:
                if turn:
                    lx.append(x.get_rect(center=(205, 100)))
                    turn = False
                    board[0][1] = 1
                else:
                    lo.append(o.get_rect(center=(197, 100)))
                    turn = True
                    board[0][1] = 2
            if s3.collidepoint(event.pos) and board[0][2] == 0:
                if turn:
                    lx.append(x.get_rect(center=(305, 100)))
                    turn = False
                    board[0][2] = 1
                else:
                    lo.append(o.get_rect(center=(300, 100)))
                    turn = True
                    board[0][2] = 2
            if s4.collidepoint(event.pos) and board[1][0] == 0:
                if turn:
                    lx.append(x.get_rect(center=(100, 200)))
                    turn = False
                    board[1][0] = 1
                else:
                    lo.append(o.get_rect(center=(100, 200)))
                    turn = True
                    board[1][0] = 2
            if s5.collidepoint(event.pos) and board[1][1] == 0:
                if turn:
                    lx.append(x.get_rect(center=(205, 200)))
                    turn = False
                    board[1][1] = 1
                else:
                    lo.append(o.get_rect(center=(197, 200)))
                    turn = True
                    board[1][1] = 2
            if s6.collidepoint(event.pos) and board[1][2] == 0:
                if turn:
                    lx.append(x.get_rect(center=(305, 200)))
                    turn = False
                    board[1][2] = 1
                else:
                    lo.append(o.get_rect(center=(300, 200)))
                    turn = True
                    board[1][2] = 2
            if s7.collidepoint(event.pos) and board[2][0] == 0:
                if turn:
                    lx.append(x.get_rect(center=(100, 300)))
                    turn = False
                    board[2][0] = 1
                else:
                    lo.append(o.get_rect(center=(100, 300)))
                    turn = True
                    board[2][0] = 2
            if s8.collidepoint(event.pos) and board[2][1] == 0:
                if turn:
                    lx.append(x.get_rect(center=(205, 300)))
                    turn = False
                    board[2][1] = 1
                else:
                    lo.append(o.get_rect(center=(197, 300)))
                    turn = True
                    board[2][1] = 2
            if s9.collidepoint(event.pos) and board[2][2] == 0:
                if turn:
                    lx.append(x.get_rect(center=(305, 300)))
                    turn = False
                    board[2][2] = 1
                else:
                    lo.append(o.get_rect(center=(300, 300)))
                    turn = True
                    board[2][2] = 2
    if state == 0:
        screen.fill((3, 252, 240))
        text = font.render("Tic Tac Toe", True, 'blue')
        text_rec = text.get_rect(center=(200, 100))
        screen.blit(text, text_rec)
        text2 = font.render("Start", True, 'blue')
        text_rec2 = text2.get_rect(center=(200, 370))
        screen.blit(text2, text_rec2)

    if state == 1:
        if turn:
            text = font.render("Turn: X", True, 'Red')
            text_rec = text.get_rect(center=(200, 30))
        else:
            text = font.render("Turn: O", True, 'skyblue')
            text_rec = text.get_rect(center=(200, 30))
        draw()
        screen.blit(text, text_rec)
        for i in lx:
            screen.blit(x, i)
        for i in lo:
            screen.blit(o, i)
        if solution(board):
            state = 2
        elif len(lx) + len(lo) == 9:
            state = 2
    if state == 2:
        text = font.render(winner_text, True, 'blue')
        text_rec = text.get_rect(center=(200, 200))
        text2 = font.render("Restart", True, 'blue')
        text_rec2 = text2.get_rect(center=(200, 380))
        text3 = font.render("Quit", True, 'blue')
        text_rec3 = text3.get_rect(center=(50, 380))
        screen.blit(text, text_rec)
        screen.blit(text2, text_rec2)
        screen.blit(text3, text_rec3)
    pygame.display.update()
