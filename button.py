import pygame


pygame.init()
class Button:
    def __init__(self, color, window, x):
        self.x = ((16+100)*x)+216
        self.y = 675
        self.color = color
        self.bet = 0
        self.sprite = pygame.Rect(self.x, self.y, 100, 100)
        self.window = window
        self.pressed = False
        self.active = True
        self.multiplier = -1
    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        multiplier_text = font.render(str(self.multiplier)+"x", True, (40, 40, 40))
        bet_text = font.render(str(self.bet), True, (20, 20, 20))
        if self.sprite.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.active:
                pygame.draw.rect(self.window, pygame.Color(self.color).correct_gamma(.2), self.sprite,0,10)
                pygame.draw.rect(self.window, pygame.Color(self.color).correct_gamma(.5), self.sprite, 6,10)
                self.pressed = True

            else:
                pygame.draw.rect(self.window, pygame.Color(self.color).correct_gamma(2), self.sprite,0,10)
                pygame.draw.rect(self.window, pygame.Color(self.color).correct_gamma(1), self.sprite,5,10)
        else:
            pygame.draw.rect(self.window, pygame.Color(self.color).correct_gamma(1), self.sprite,0,10)
            pygame.draw.rect(self.window, pygame.Color(self.color).correct_gamma(.7), self.sprite,5,10)
        if self.multiplier >= 9:
            self.window.blit(multiplier_text, (self.x+20, self.y+40))
        elif self.multiplier >= 0:
            self.window.blit(multiplier_text, (self.x + 30, self.y + 40))
        if self.bet >= 0:
            self.window.blit(bet_text, (self.x+40, self.y-40))
        else:
            self.window.blit(font.render("Start", True, (255, 255, 255)), (self.x+57, self.y+36))
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y

    def set_rect(self,width,height):
        self.sprite = pygame.Rect(self.x, self.y, width, height)