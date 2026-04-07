import pygame
from read_words import read_words
from Word import Word

pygame.init()

screen = pygame.display.set_mode((800, 600))

# set title and icon of pygame window
pygame.display.set_caption("Typing Test")
pygame.display.set_icon(pygame.image.load("keyboard.png"))

# text font
base_font = pygame.font.Font(None, 32)

# read in words
words = read_words(20)
words_text = []

# TO DO: highlight current word
# TO DO: user text input
# TO DO: only show 4 lines at a time
# TO DO: move lines up (read in next line of words) when finished
width = 100
height = 150
for word in words:
    size = pygame.font.Font.size(base_font, word)
    # if width exceeds size of screen, put onto next line
    if width > 650:
        height += 30
        width = 100
    words_text.append(Word(word, base_font, width, height, size, screen))
    width += size[0] + 30

running = True
while running:
    screen.fill((255, 255, 255))

    for w in words_text:
        w.display()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
