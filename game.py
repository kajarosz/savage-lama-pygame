import pygame
from random import randint, choice
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

# Instantiate lama
lama = Lama()

# Set variables to generate chickens
chicken_freq = 10
chicken_max = 2
generate_chicken = [0 for i in range(0, fps * chicken_freq - 1)]
generate_chicken.append(1)
chicken_timer = 0
chicken_list = []

# Set variables to generate random food with fixed frequency
food_freq = 10
generate_food = [0 for i in range(0, fps * food_freq - 1)]
generate_food.append(1)
food_timer = 0
food_list = [Food(randint(5, 870))]

# Generate health hearts
life_no = 5
life_list = []
life_width = 27
life_space = 3
for i in range(0, life_no):
    life_list.append(Life((20 + i * (life_width + life_space)), 20))

# Generate red transparent background fill
s = pygame.Surface((window_width, window_height))
s.set_alpha(128)
s.fill((255, 0, 0))

# Set font for score
font_score = pygame.font.SysFont('comicsans', 30, True)

# Set font for health points
font_health = pygame.font.SysFont('comicsans', 14, True)

# Redraw window function


def redraw_window():
    window.blit(bg_pic, (0, 0))
    for food in food_list:
        food.draw(window)
    lama.draw(window, s)
    for life in life_list:
        life.draw(window)
    for chicken in chicken_list:
        chicken.draw(window)
    text_score = font_score.render('SCORE: ' + str(lama.score), 1, (0, 0, 0))
    window.blit(text_score, (720, 10))
    text_health = font_health.render('REGAIN LIFE: ' + str(lama.health_points) + ' / 5', 1, (0, 0, 0))
    window.blit(text_health, (20, 50))
    pygame.display.update()


def life_reduce():
    for life in reversed(life_list):
        if life.status == 0:
            continue
        else:
            life.status -= 25
            break
    if life_list[0].status == 0:
        run = False
    else:
        run = True
    return run


# Main game loop
run = True
while run:
    clock.tick(fps)

    # Exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



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
    # Generate random food
    if food_timer < fps * food_freq:
        if generate_food[food_timer] and len(food_list) < 6:
            food_list.append(Food(randint(5, 870)))
            food_timer += 1
        else:
            food_timer += 1
    else:
        food_timer = 0

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

        # regain life if lama collects 5 health points
        if lama.health_points == 5:
            lama.health_points = 0
            for life in life_list:
                if life.status != 100:
                    life.status = 100
                    break
                else:
                    continue

    # ENEMY - CHICKEN
    # Generate chickens
    if chicken_timer < fps * chicken_freq:
        if generate_chicken[chicken_timer] and len(chicken_list) <= chicken_max:
            chicken_available_x_list = [i for i in range(5, window_width - 33 - 210 - 5)]
            chicken_unavailable_x_list = [i for i in range(lama.x - 50, lama.x + lama.width + 50)]
            for x in chicken_unavailable_x_list:
                try:
                    chicken_available_x_list.pop(chicken_available_x_list.index(x))
                except ValueError:
                    continue
            random_chicken_x = choice(chicken_available_x_list)
            chicken_list.append(Chicken(random_chicken_x))
            chicken_timer += 1
        else:
            chicken_timer += 1
    else:
        chicken_timer = 0

    for chicken in chicken_list:
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
            chicken.x -= chicken.speed
            chicken.steps += 1
        elif chicken.right:
            chicken.x += chicken.speed
            chicken.steps += 1

        if chicken.x < lama.x + lama.width < chicken.x + chicken.width:
            if lama.jumping and chicken.y < lama.y + lama.height:
                lama.score += 1
                chicken_list.pop(chicken_list.index(chicken))
            elif not lama.jumping and not lama.protected:
                lama.protected = True
                life_reduce()
        elif chicken.x < lama.x < chicken.x + chicken.width:
            if lama.jumping and chicken.y < lama.y + lama.height:
                lama.score += 1
                chicken_list.pop(chicken_list.index(chicken))
            elif not lama.jumping and not lama.protected:
                lama.protected = True
                life_reduce()

    # Redraw game window
    redraw_window()

# Quit game

pygame.quit()
