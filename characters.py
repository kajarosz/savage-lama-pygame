import pygame
from random import randint

# Hero character class


class Lama(object):
    walk_right = [pygame.image.load('images/lama/lama_R1.png'), pygame.image.load('images/lama/lama_R2.png'),
                  pygame.image.load('images/lama/lama_R3.png'), pygame.image.load('images/lama/lama_R4.png')]
    walk_left = [pygame.image.load('images/lama/lama_L1.png'), pygame.image.load('images/lama/lama_L2.png'),
                 pygame.image.load('images/lama/lama_L3.png'), pygame.image.load('images/lama/lama_L4.png')]
    stand = [pygame.image.load('images/lama/lama_R0.png'), pygame.image.load('images/lama/lama_L0.png')]
    eat_right = [pygame.image.load('images/lama/lama_RE1.png'), pygame.image.load('images/lama/lama_RE2.png'),
                 pygame.image.load('images/lama/lama_RE3.png'), pygame.image.load('images/lama/lama_RE4.png')]
    eat_left = [pygame.image.load('images/lama/lama_LE1.png'), pygame.image.load('images/lama/lama_LE2.png'),
                pygame.image.load('images/lama/lama_LE3.png'), pygame.image.load('images/lama/lama_LE4.png')]

    def __init__(self):
        self.x = 200
        self.y = 582
        self.width = 50
        self.width_eating = 66
        self.height = 63
        self.speed = 6
        self.right = True
        self.left = False
        self.standing = True
        self.walk_count = 0
        self.jumping = False
        self.jump_height = 10
        self.eating = False
        self.eat_count = 0
        self.health_points = 0
        self.protected = False
        self.protection_count = 0
        self.score = 0

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

    def hit(self, window, s):
        if self.protected:
            if self.protection_count >= 32:
                self.protected = False
                self.protection_count = 0
            else:
                window.blit(s, (0, 0))
                self.protection_count += 1

    def draw(self, window, s):
        self.move(window)
        self.eat(window)
        self.hit(window, s)


# Hero lifes class

class Life(object):
    life_100 = pygame.image.load('images/life/life_100.png')
    life_75 = pygame.image.load('images/life/life_75.png')
    life_50 = pygame.image.load('images/life/life_50.png')
    life_25 = pygame.image.load('images/life/life_25.png')
    life_0 = pygame.image.load('images/life/life_0.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 27
        self.height = 30
        self.status = 100

    def draw(self, window):
        if self.status == 100:
            window.blit(self.life_100, (self.x, self.y))
        elif self.status == 75:
            window.blit(self.life_75, (self.x, self.y))
        elif self.status == 50:
            window.blit(self.life_50, (self.x, self.y))
        elif self.status == 25:
            window.blit(self.life_25, (self.x, self.y))
        else:
            window.blit(self.life_0, (self.x, self.y))


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

    def __init__(self, x):
        self.width = 32
        self.height = 32
        self.x = x
        self.y = 614
        self.eatbox = [self.x, self.y, self.x + self.width, self.y + self.height]
        self.type = randint(0, len(self.food_images) - 1)
        self.life = randint(80, 1440)

    def display(self, window):
        window.blit(self.food_images[self.type], (self.x, self.y))

    def draw(self, window):
        self.display(window)


# Chicken enemy class

class Chicken(object):
    walk_right = [pygame.image.load('images/chicken/chicken_R1.png'),
                  pygame.image.load('images/chicken/chicken_R2.png'),
                  pygame.image.load('images/chicken/chicken_R3.png'),
                  pygame.image.load('images/chicken/chicken_R4.png')]
    walk_left = [pygame.image.load('images/chicken/chicken_L1.png'),
                 pygame.image.load('images/chicken/chicken_L2.png'),
                 pygame.image.load('images/chicken/chicken_L3.png'),
                 pygame.image.load('images/chicken/chicken_L4.png')]

    def __init__(self, x):
        self.x = x
        self.y = 618
        self.width = 33
        self.height = 27
        self.right = True
        self.left = False
        self.speed = 3
        self.walk_count = 0
        self.steps = 0
        self.path = 50

    def move(self, window):
        if self.walk_count + 1 >= 16:
            self.walk_count = 0
        if self.left:
            window.blit(self.walk_left[self.walk_count // 4], (self.x, self.y))
            self.walk_count += 1
        else:
            window.blit(self.walk_right[self.walk_count // 4], (self.x, self.y))
            self.walk_count += 1

    def draw(self, window):
        self.move(window)

