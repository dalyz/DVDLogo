import pygame
import sys

pygame.init()

speed = [8, 7]
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
logo = pygame.image.load("./DVD/dvdgreen.png")
rect = logo.get_rect()
fps = 60

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
    
        if rect.left < 0:
            speed[0] = -speed[0]
            logo = pygame.image.load("./DVD/dvdblue.png")

        if rect.right > width:
            speed[0] = -speed[0]
            logo = pygame.image.load("./DVD/dvdred.png")

        if rect.top < 0:
            speed[1] = -speed[1]
            logo = pygame.image.load("./DVD/dvdgreen.png")

        if rect.bottom > height:
            speed[1] = -speed[1]
            logo = pygame.image.load("./DVD/dvdyellow.png")

        rect.left += speed[0]
        rect.top += speed[1]
        screen.fill((0, 0, 0))
        screen.blit(logo, rect)
        pygame.display.update()
        clock.tick(fps)
