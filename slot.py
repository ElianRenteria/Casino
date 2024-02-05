import pygame
import random

class Slot:
    def __init__(self, x, y):
        sprites = ["assets/lemon.png", "assets/pineapple.png", "assets/watermelon.png", "assets/apple.png", "assets/grape.png"]
        types = ["lemon", "pineapple", "watermelon", "apple", "grape"]
        colors = [(220, 20, 60), (255, 215, 0), (51, 204, 51), (255, 127, 127), (135, 31, 120)]
        self.option = -1
        weights = [30, 15, 15, 25, 15]
        self.option = random.choices([0,1,2,3,4], weights, k=1)[0]
        # o = random.randint(0, 19)
        # if o < 7:
        #     self.option = 0
        # elif o < 10:
        #     self.option = 1
        # elif o < 12:
        #     self.option = 2
        # elif o < 16:
        #     self.option = 4
        # else:
        #     self.option = 3
        self.x = x
        self.y = y
        self.sprite = pygame.transform.scale(pygame.image.load(sprites[self.option]), (150, 150))
        self.container = pygame.Rect(self.x, self.y, 200,200)
        self.color = colors[self.option]
        self.multiplier = None
        self.type = types[self.option]

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.container, 20)
        pygame.draw.rect(window, (0,0,0), self.container, 2)
        window.blit(self.sprite, (self.container.x+25, self.container.y+25))

    def reload(self, newOption):
        sprites = ["assets/lemon.png", "assets/pineapple.png", "assets/watermelon.png", "assets/apple.png",
                   "assets/grape.png"]
        types = ["lemon", "pineapple", "watermelon", "apple", "grape"]
        colors = [(220, 20, 60), (255, 215, 0), (51, 204, 51), (255, 127, 127), (135, 31, 120)]
        self.option = newOption
        self.sprite = pygame.transform.scale(pygame.image.load(sprites[self.option]), (150, 150))
        self.color = colors[self.option]
        self.type = types[self.option]





