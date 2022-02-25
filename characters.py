import pygame

# Hero character class


class Hero(object):
    walk_right = [pygame.image.load('images/lama_R1.png'), pygame.image.load('images/lama_R2.png'),
                 pygame.image.load('images/lama_R3.png'), pygame.image.load('images/lama_R4.png')]
    walk_left = [pygame.image.load('images/lama_L1.png'), pygame.image.load('images/lama_L2.png'),
                 pygame.image.load('images/lama_L3.png'), pygame.image.load('images/lama_L4.png')]
    stand = pygame.image.load('images/lama_F1.png')

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


