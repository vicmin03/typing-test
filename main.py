import pygame
from read_words import read_words
from Word import Word

pygame.init()


# define dimensions of window and playable area
WIDTH, HEIGHT = 800, 600
START_X, END_X = 50, 550

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# set title and icon of pygame window
pygame.display.set_caption("Typing Test")
pygame.display.set_icon(pygame.image.load("keyboard.png"))

# text font
base_font = pygame.font.Font(None, 32)

# read in words
# TO DO - increase to 200? and display 3 lines at a time
words = read_words(20)
words_text = []

# display words to be typed
#   TO DO: only show 4 lines at a time
#   TO DO: move lines up (read in next line of words) when finished
x = START_X
y = 150
for word in words:
    size = pygame.font.Font.size(base_font, word)
    # if width exceeds size of screen, put onto next line
    if x + size[0] > 750:
        y += 50
        x = START_X
    words_text.append(Word(word, base_font, x, y, size, screen))
    x += size[0] + 30

# text box for user input
text_box = pygame.Rect(START_X, 500, 700, 60)
user_text = ""

current_word = 0        # index of current word user is to type

# GAME LOOP
running = True
while running:
    target = words[current_word]

    screen.fill((255, 255, 255))

    for i in range(len(words_text)):
        w = words_text[i]
        if i == current_word:
            w.highlight()
        w.display()

    # display text box
    pygame.draw.rect(screen, (210, 210, 210), text_box)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:         # when user presses space, move onto next word
                w = words_text[current_word]
                w.finished(user_text == target)     # check if spelt correctly
                user_text = ""
                w.unhighlight()
                current_word += 1

            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            else:
                if event.unicode.isalpha():
                    user_text += event.unicode

            # compare current text with word (up til length)
            # if incorrect, highlight with red
            if user_text != target[0:len(user_text)]:
                words_text[current_word].incorrect()
            else:
                words_text[current_word].correct()

    text_surface = base_font.render(user_text, True, (0, 0, 0))
    screen.blit(text_surface, (START_X + 20, 520))

    pygame.display.update()
