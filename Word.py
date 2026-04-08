import pygame


class Word:
    def __init__(self, word, font, x, y, size, screen, eol):
        self.word = word
        self.screen = screen
        self.color = (0, 0, 0)
        self.x = x
        self.y = y
        self.size = size
        self.font = font
        self.text = font.render(self.word, True, self.color)
        self.highlight_color = (190, 190, 190)
        self.start_of_line = eol

        self.textRect = pygame.Rect(
            self.x-10, self.y-5, self.size[0] + 20, self.size[1] + 10)

        self.highlighted = False

    def display(self):
        if self.highlighted:
            pygame.draw.rect(self.screen, (self.highlight_color),
                             self.textRect, border_radius=8)
        self.screen.blit(self.text, (self.x, self.y))

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_y(self, y):
        self.y = y
        self.set_rect()

    def set_rect(self):
        self.textRect = pygame.Rect(
            self.x-10, self.y-5, self.size[0] + 20, self.size[1] + 10)

    # return true if word is first on its line
    def get_sol(self):
        return self.start_of_line

    def highlight(self):
        self.highlighted = True

    def unhighlight(self):
        self.highlighted = False

    def incorrect(self):
        self.highlight_color = (255, 0, 0)

    def correct(self):
        self.highlight_color = (190, 190, 190)

    def finished(self, correct):
        # check if correct or not to determine color
        if correct:
            self.color = (59, 156, 50)
        if not correct:
            self.color = (255, 0, 0)
        self.text = self.font.render(self.word, True, self.color)
