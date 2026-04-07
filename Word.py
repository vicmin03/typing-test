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

        self.textRect = pygame.Rect(
            self.x-10, self.y-5, size[0] + 20, size[1] + 10)
        # self.textRect.center = (self.x + size[0]//2, self.y + size[1]//2)

        self.highlighted = False

    def display(self):
        if self.highlighted:
            pygame.draw.rect(self.screen, (190, 190, 190),
                             self.textRect, border_radius=8)
        self.screen.blit(self.text, (self.x, self.y))

    def highlight(self):
        self.highlighted = True

    def unhighlight(self):
        self.highlighted = False
