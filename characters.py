import pygame
from random import randint

# Hero character class


class Hero(object):
    walk_right = [pygame.image.load('images/lama/lama_R1.png'), pygame.image.load('images/lama/lama_R2.png'),
                  pygame.image.load('images/lama/lama_R3.png'), pygame.image.load('images/lama/lama_R4.png')]
    walk_left = [pygame.image.load('images/lama/lama_L1.png'), pygame.image.load('images/lama/lama_L2.png'),
                 pygame.image.load('images/lama/lama_L3.png'), pygame.image.load('images/lama/lama_L4.png')]
    stand = [pygame.image.load('images/lama/lama_R0.png'), pygame.image.load('images/lama/lama_L0.png')]
    eat_right = [pygame.image.load('images/lama/lama_RE1.png'), pygame.image.load('images/lama/lama_RE2.png'),
                 pygame.image.load('images/lama/lama_RE3.png'), pygame.image.load('images/lama/lama_RE4.png')]
    eat_left = [pygame.image.load('images/lama/lama_LE1.png'), pygame.image.load('images/lama/lama_LE2.png'),
                pygame.image.load('images/lama/lama_LE3.png'), pygame.image.load('images/lama/lama_LE4.png')]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.width_eating = 66
        self.height = 63
        self.speed = 5
        self.right = True
        self.left = False
        self.standing = True
        self.walk_count = 0
        self.jumping = False
        self.jump_height = 10
        self.eating = False
        self.eat_count = 0
        self.hitbox = [self.x, self.y, self.x + self.width, self.y + self.height]
        self.eatbox = [self.x, self.y, self.x + self.width_eating, self.y + self.height]

    def move(self, window):
        if not self.eating:
            if not self.standing:
                if self.walk_count + 1 >= 16:
                    self.walk_count = 0
                if self.right:
                    window.blit(self.walk_right[self.walk_count // 4], (self.x, self.y))
                    self.walk_count += 1
                elif self.left:
                    window.blit(self.walk_left[self.walk_count // 4], (self.x, self.y))
                    self.walk_count += 1
            else:
                if self.right:
                    window.blit(self.stand[0], (self.x, self.y))
                elif self.left:
                    window.blit(self.stand[1], (self.x, self.y))

    def eat(self, window):
        if self.eating and self.standing:
            if self.right:
                window.blit(self.eat_right[self.eat_count // 4], (self.x, self.y))
                self.eat_count += 1
            elif self.left:
                window.blit(self.eat_left[self.eat_count // 4], (self.x - 16, self.y))
                self.eat_count += 1
        if self.eat_count + 1 >= 16:
            self.eating = False
            self.eat_count = 0

    def draw(self, window):
        self.move(window)
        self.eat(window)


# Food class

class Food(object):
    food_images = [pygame.image.load('images/food/banana.png'), pygame.image.load('images/food/watermelon.png'),
                   pygame.image.load('images/food/carrot.png'), pygame.image.load('images/food/cheese.png'),
                   pygame.image.load('images/food/cherry.png'), pygame.image.load('images/food/grapes_green.png'),
                   pygame.image.load('images/food/grapes_purple.png'), pygame.image.load('images/food/lemon.png'),
                   pygame.image.load('images/food/mulberry.png'), pygame.image.load('images/food/mushroom.png'),
                   pygame.image.load('images/food/orange.png'), pygame.image.load('images/food/pear.png'),
                   pygame.image.load('images/food/pepper_green.png'), pygame.image.load('images/food/pepper_red.png'),
                   pygame.image.load('images/food/pepper_yellow.png'), pygame.image.load('images/food/pineapple.png'),
                   pygame.image.load('images/food/radish.png'), pygame.image.load('images/food/strawberry.png')]

    def __init__(self):
        self.width = 32
        self.height = 32
        self.x = randint(5, 870)
        self.y = 614
        self.eatbox = [self.x, self.y, self.x + self.width, self.y + self.height]
        self.type = randint(0, len(self.food_images) - 1)
        self.life = 160

    def display(self, window):
        window.blit(self.food_images[self.type], (self.x, self.y))

    def eaten(self):
        pass

    def draw(self, window):
        self.display(window)
