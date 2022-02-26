import pygame
import time
from characters import Lama, Food, Life, Chicken

# Initiate game
pygame.init()

# Set and open a game window
window_width = 905
window_height = 703
window = pygame.display.set_mode((window_width, window_height))
bg_pic = pygame.image.load('images/bg.png')
pygame.display.set_caption("Savage Lama Game")

# Set clock and FPS
clock = pygame.time.Clock()
fps = 16

# Instantiate characters, enemies and projectiles
lama = Lama()
chicken = Chicken()

# Set variables to generate random food with fixed frequency
food_freq = 10
generate_food = [0 for i in range(0, fps * food_freq - 1)]
generate_food.append(1)
food_timer = 0
food_list = []

# Generate health hearts
life_no = 5
life_list = []
life_width = 27
life_space = 3
for i in range(0, life_no):
    life_list.append(Life((20 + i * (life_width + life_space)), 20))

# Redraw window function


def redraw_window():
    window.blit(bg_pic, (0, 0))
    for food in food_list:
        food.draw(window)
    lama.draw(window)
    for life in life_list:
        life.draw(window)
    chicken.draw(window)
    pygame.display.update()


# Main game loop
run = True
while run:
    clock.tick(fps)

    # Exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Generate random food

    if food_timer < fps * food_freq:
        if generate_food[food_timer] and len(food_list) < 6:
            food_list.append(Food())
            food_timer += 1
        else:
            food_timer += 1
    else:
        food_timer = 0

    # Get key commands

    keys = pygame.key.get_pressed()

    # CHARACTER
    # character moving
    if keys[pygame.K_RIGHT] and not lama.eating and lama.x + lama.width + lama.speed < window_width:
        lama.x += lama.speed
        lama.right = True
        lama.left = False
        lama.standing = False
    elif keys[pygame.K_LEFT] and not lama.eating and lama.x - lama.speed > 0:
        lama.x -= lama.speed
        lama.right = False
        lama.left = True
        lama.standing = False
    else:
        lama.standing = True

    # character jumping
    if keys[pygame.K_UP] and not lama.eating:
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

    # character eating
    if keys[pygame.K_DOWN] and lama.standing and not lama.jumping:
        lama.eating = True

    # FOOD
    for food in food_list:
        # delete food after 15 s
        if food.life >= 0:
            food.life -= 1
        else:
            food_list.pop(food_list.index(food))

        # delete food if eaten
        if lama.right and lama.eating and food.x < lama.x + lama.width_eating < food.x + food.width:
            food_list.pop(food_list.index(food))
            lama.health_points += 1
        elif lama.left and lama.eating and food.x < lama.x < food.x + food.width:
            food_list.pop(food_list.index(food))
            lama.health_points += 1

    # ENEMY - CHICKEN
    # chicken moving
    if chicken.steps >= chicken.path:
        chicken.steps = 0
        if chicken.left:
            chicken.left = False
            chicken.right = True
        elif chicken.right:
            chicken.left = True
            chicken.right = False
    if chicken.left:
        chicken.x -= chicken.vel
        chicken.steps += 1
    elif chicken.right:
        chicken.x += chicken.vel
        chicken.steps += 1

    # Redraw game window
    redraw_window()

# Quit game

pygame.quit()
