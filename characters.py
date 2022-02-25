import pygame
from random import randint

# Hero character class


class Hero(object):
    walk_right = [pygame.image.load('images/lama/lama_R1.png'), pygame.image.load('images/lama/lama_R2.png'),
                 pygame.image.load('images/lama/lama_R3.png'), pygame.image.load('images/lama/lama_R4.png')]
    walk_left = [pygame.image.load('images/lama/lama_L1.png'), pygame.image.load('images/lama/lama_L2.png'),
                 pygame.image.load('images/lama/lama_L3.png'), pygame.image.load('images/lama/lama_L4.png')]
    stand = pygame.image.load('images/lama/lama_F1.png')

    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.speed = 5
        self.right = True
        self.left = False
        self.standing = True
        self.walk_count = 0
        self.jumping = False
        self.jump_height = 10

    def walk(self, window):
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
            window.blit(self.stand, (self.x, self.y))

    def draw(self, window):
        self.walk(window)


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
        self.type = randint(0, len(self.food_images) - 1)
        self.life = 160

    def display(self, window):
        window.blit(self.food_images[self.type], (self.x, self.y))

    def draw(self, window):
        self.display(window)
