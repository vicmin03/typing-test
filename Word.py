import pygame


# make rect first then display text on top of rect
class Word:
    def __init__(self, word, font, x, y, size, screen):
        self.word = word
        self.screen = screen
        # self.user_input = ""
        self.color = (0, 0, 0)
        self.x = x
        self.y = y
        self.size = size
        self.text = font.render(self.word, True, self.color)

        self.textRect = self.text.get_rect()

        self.textRect.center = (self.x + size[0]//2, self.y + size[1]//2)

    def display(self):
        pygame.draw.rect(self.screen, (190, 190, 190), self.textRect)
        self.screen.blit(self.text, (self.x, self.y))
