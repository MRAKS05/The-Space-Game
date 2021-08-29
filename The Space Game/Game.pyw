import os

import button
import pygame

# create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
back = pygame.image.load(('profile\ground.png'))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The Space Game')

# load button images
start_img = pygame.image.load('profile\start_btn.png').convert_alpha()
exit_img = pygame.image.load('profile\exit_btn.png').convert_alpha()
player = pygame.image.load('profile\player.png')
enemy = pygame.image.load('profile\enimy.png')
icon = pygame.image.load('profile\icon.png')
name = pygame.image.load("profile\same.png")

# icon 
pygame.display.set_icon(icon)

# create button instances
start_button = button.Button(100, 300, start_img, 0.8)
exit_button = button.Button(450, 300, exit_img, 0.8)

# game loop
run = True
while run:

    screen.fill((0, 0, 0))
    screen.blit(back, (0, 0))
    screen.blit(player, (700, 100))
    screen.blit(enemy, (50, 100))
    screen.blit(name, (200, 25))

    if start_button.draw(screen):
        pygame.quit()
        os.system('python main.pyw')
    if exit_button.draw(screen):
        quit()

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
