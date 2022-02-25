import pygame
from characters import Hero

# Initiate game
pygame.init()

# Set and open a game window
window_width = 905
window_height = 703
window = pygame.display.set_mode((window_width, window_height))
bg_pic = pygame.image.load('images/bg.png')
pygame.display.set_caption("Savage Lama Game")

# Set clock
clock = pygame.time.Clock()

# Instantiate characters and projectiles
lama = Hero(200, 580, 50)

# Redraw window function


def redraw_window():
    window.blit(bg_pic, (0, 0))
    lama.draw(window)
    pygame.display.update()


# Main game loop
run = True
while run:
    clock.tick(16)

    # Exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Move the character

    if keys[pygame.K_RIGHT] and lama.x + lama.width + lama.speed < window_width:
        lama.x += lama.speed
        lama.right = True
        lama.left = False
        lama.standing = False
    elif keys[pygame.K_LEFT] and lama.x - lama.speed > 0:
        lama.x -= lama.speed
        lama.right = False
        lama.left = True
        lama.standing = False
    else:
        lama.standing = True

    if keys[pygame.K_UP]:
        lama.jumping = True

    if lama.jumping:
        if lama.jump_height >= 0:
            lama.y -= (lama.jump_height ** 2) * 0.5
            lama.jump_height -= 1
        elif -10 <= lama.jump_height < 0:
            lama.y += (lama.jump_height ** 2) * 0.5
            lama.jump_height -= 1
        else:
            lama.jumping = False
            lama.jump_height = 10

    redraw_window()

# Quit game

pygame.quit()
