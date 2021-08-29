import math
import os
import random

import pygame
from pygame import mixer

pygame.init()

display = pygame.display.set_mode((800, 500))

score_value = 0
front = pygame.font.Font("profile\Early GameBoy.ttf", 16)
textX = 20
textY = 20

over_fornt = pygame.font.Font("profile\Early GameBoy.ttf", 64)
re = pygame.font.Font("profile\Early GameBoy.ttf", 16)
quit_text = pygame.font.Font("profile\Early GameBoy.ttf", 16)
q_text = pygame.font.Font("profile\Early GameBoy.ttf", 16)

pygame.display.set_caption("The Space Game")
icon = pygame.image.load('profile\icon.png')
pygame.display.set_icon(icon)

back = pygame.image.load(('profile\ground.png'))

player = pygame.image.load(('profile\player.png'))
playerX = 350
playerY = 350
playerX_change = 0
playerY_change = 0

enimy = []
enimyX = []
enimyY = []
enimyX_change = []
enimyY_change = []

number_of_enimys = 6
for i in range(number_of_enimys):
    enimy.append(pygame.image.load(('profile\enimy.png')))
    enimyX.append(random.randint(0, 734))
    enimyY.append(random.randint(55, 150))
    enimyX_change.append(0.3)
    enimyY_change.append(40)

bulet = pygame.image.load(('profile\cullet.png'))
buletX = 0
buletY = 345
buletX_change = 0
buletY_change = 1
bulet_state = "ready"


def score_show(x, y):
    score = front.render("Score : " + str(score_value), True, (255, 255, 255))
    display.blit(score, (x, y))


def quit_show():
    quit_ll = quit_text.render("Press 'Esc' To MainMenu", True, (255, 255, 255))
    display.blit(quit_ll, (250, 270))


def q_show():
    q_ll = q_text.render("Press 'Q' To Quit", True, (255, 255, 255))
    display.blit(q_ll, (290, 290))


def game_over_text():
    gameover = over_fornt.render("GAME OVER", True, (255, 0, 0))
    display.blit(gameover, (150, 150))


def rerun_show():
    replay = re.render("Press 'R' To Play Again", True, (0, 255, 0))
    display.blit(replay, (250, 250))


def player_add(x, y):
    display.blit(player, (x, y))


def enimy_add(x, y, i):
    display.blit(enimy[i], (x, y))


def fire_bulet(x, y):
    global bulet_state
    bulet_state = "fire"
    display.blit(bulet, (x + 16, y + 10))


def is_colliusion(enimyX, enimyY, buletX, buletY):
    distance = math.sqrt((math.pow(enimyX - buletX, 2)) + (math.pow(enimyY - buletY, 2)))
    if distance < 16:
        return True
    else:
        return False


running = True
while running:
    display.fill((0, 0, 0))
    display.blit(back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                os.system("python Game.pyw")
            if event.key == pygame.K_r:
                pygame.quit()
                os.system("python main.pyw")
            if event.key == pygame.K_a:
                playerX_change = -0.5
            if event.key == pygame.K_d:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bulet_state == "ready":
                    b_sound = mixer.Sound("profile\laser.wav")
                    b_sound.play()
                    buletX = playerX
                    fire_bulet(buletX, buletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735

    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 435:
        playerY = 435

    for i in range(number_of_enimys):
        if enimyY[i] > 300:
            for j in range(number_of_enimys):
                enimyY[j] = 2000
            game_over_text()
            rerun_show()
            quit_show()
            q_show()
            break

        enimyX[i] += enimyX_change[i]
        if enimyX[i] <= 0:
            enimyX_change[i] = 0.3
            enimyY[i] += enimyY_change[i]
        elif enimyX[i] >= 735:
            enimyX_change[i] = -0.3
            enimyY[i] += enimyY_change[i]

        colliusion = is_colliusion(enimyX[i], enimyY[i], buletX, buletY)
        if colliusion:
            e_sound = mixer.Sound("profile\e_sound.wav")
            e_sound.play()
            buletY = 345
            bulet_state = "ready"
            score_value += 1
            enimyX[i] = random.randint(0, 734)
            enimyY[i] = random.randint(55, 150)

        enimy_add(enimyX[i], enimyY[i], i)

    player_add(playerX, playerY)

    if buletY <= 0:
        buletY = 345
        bulet_state = "ready"

    if bulet_state is "fire":
        fire_bulet(buletX, buletY)
        buletY -= buletY_change
    score_show(textX, textY)

    pygame.display.update()
