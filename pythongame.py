import pygame
#initialize
pygame.init()
screen = pygame.display.set_mode((800,600))
white =(255,255,255)
#caption
pygame.display.set_caption("space invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
#create loop
running = True
while running:
    # red,green,bule
    screen.fill(white)
    screen.fill((0,0,1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()