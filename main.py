import pygame
from read_words import read_words
from Word import Word

pygame.init()

# define dimensions of window and playable area
WIDTH, HEIGHT = 900, 600
START_X, END_X = 50, 750
START_Y, END_Y = 150, 400
NUM_LINES = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# set title and icon of pygame window
pygame.display.set_caption("Typing Test")
pygame.display.set_icon(pygame.image.load("keyboard.png"))

# text fonts
base_font = pygame.font.SysFont("Arial", 32)
timer_font = pygame.font.SysFont("Arial", 60, bold=True)

# read in words
NUM_WORDS = 50
words = read_words(NUM_WORDS)
words_text = []

# display words to be typed
# keeps track of 3 lines of words to be displayed
lines = [[] for _ in range(NUM_LINES)]

x = START_X
y = START_Y
# create an object for each word in list (x position will be correct)
for i in range(len(words)):
    word = words[i]
    size = pygame.font.Font.size(base_font, word)
    # if width exceeds size of screen, put onto next line
    if i == 0 or x + size[0] > WIDTH - 50:
        y += 50
        x = START_X
        words_text.append(Word(word, base_font, x,
                          y, size, screen, True))
    else:
        words_text.append(Word(word, base_font, x,
                          y, size, screen, False))
    x += size[0] + 30


def fill_lines(start, lines):
    # fill line arrays with index of words to be displayed on each line
    lines = [[], [], []]
    line = 0
    current_y = START_Y
    i = start
    while line < NUM_LINES and i < NUM_WORDS:
        word = words_text[i]
        if i != start and word.get_sol():
            line += 1
            current_y += 50
        word.set_y(current_y)
        if line < NUM_LINES:
            lines[line].append(i)
        i += 1

    return lines


# text box for user input
text_box = pygame.Rect(START_X, 450, WIDTH - 100, 60)
user_text = ""

# keep track of current words + those to be displayed
current_word = 0        # index of current word user is to type
first_word = 0          # index of first word to display
lines = fill_lines(first_word, lines)

# control game flow + timer
started = False
TIMEREVENT = pygame.USEREVENT + 1
# triggers timerevent every 1000ms = 1s
pygame.time.set_timer(TIMEREVENT, 1000)
time_left = 10


# --- GAME LOOP ---
running = True
while running:
    target = words[current_word]        # target string for user to type

    screen.fill((255, 255, 255))

    for line in lines[0:NUM_LINES]:
        for index in line:
            w = words_text[index]
            if index == current_word:
                w.highlight()
            w.display()

    # display text box
    pygame.draw.rect(screen, (210, 210, 210), text_box)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == TIMEREVENT:
            if time_left > 0:
                time_left -= 1
            else:
                print("TIMER FINISHED")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:         # when user presses space, move onto next word
                # check if reached end of line, then move next line up
                if current_word == lines[0][-1]:
                    first_word = current_word + 1
                    lines = fill_lines(first_word, lines)

                w = words_text[current_word]
                w.finished(user_text == target)     # check if spelt correctly
                user_text = ""
                w.unhighlight()
                current_word += 1

            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            else:
                if event.unicode.isalpha() or event.unicode == "-":
                    user_text += event.unicode

            # compare current text with word (up til length)
            # if incorrect, highlight with red
            if user_text != target[0:len(user_text)]:
                words_text[current_word].incorrect()
            else:
                words_text[current_word].correct()

    # displays user input text
    text_surface = base_font.render(user_text, True, (0, 0, 0))
    screen.blit(text_surface, (START_X + 20, 460))

    # displays timer
    timer = timer_font.render(str(time_left), True, (0, 0, 0))
    screen.blit(timer, ((WIDTH // 2) - 20, 50))

    pygame.display.update()
