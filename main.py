import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# set title and icon of pygame window
pygame.display.set_caption("Typing Test")
pygame.display.set_icon(pygame.image.load("keyboard.png"))

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
