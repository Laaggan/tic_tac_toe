import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tic Tac Toe")

player_img = pygame.image.load('gfx/character.png')
player_x = 0
player_y = 0
player_delta_x = 0
player_delta_y = 0
delta = 5

def player(x, y):
    screen.blit(player_img, (x, y))

def attack_animation(j, k):
    i = j % 4
    if k == 'DOWN':
        animation_args = (32*i, 32*4, 32, 32)
    elif k == 'UP':
        animation_args = (32*i, 32*5, 32, 32)
    elif k == 'RIGHT':
        animation_args = (32*i, 32*6, 32, 32)
    elif k == 'LEFT':
        animation_args = (32*i, 32*7, 32, 32)
    player_sprite = player_img.subsurface(*animation_args)
    scale = 3
    player_sprite = pygame.transform.scale(player_sprite, (scale * 32, scale * 32))
    screen.blit(player_sprite, (400, 400))

def animate(j, orientation, x, y, state):
    i = j % 4
    if state == "WALK":
        #FIXME: Is setting a variable cleaner to choose row from the orientation of player?
        if orientation == 'DOWN':
            animation_args = (i * 16, 0, 16, 32)
        elif orientation == 'RIGHT':
            animation_args = (i * 16, 32, 16, 32)
        elif orientation == 'UP':
            animation_args = (i * 16, 64, 16, 32)
        elif orientation == 'LEFT':
            animation_args = (i * 16, 96, 16, 32)
    elif state == 'STOP':
        if orientation == 'DOWN':
            animation_args = (0, 0, 16, 32)
        elif orientation == 'RIGHT':
            animation_args = (0, 32, 16, 32)
        elif orientation == 'UP':
            animation_args = (0, 64, 16, 32)
        elif orientation == 'LEFT':
            animation_args = (0, 96, 16, 32)
    elif state == 'ATTACK':
        if orientation == 'DOWN':
            animation_args = (32 * i, 32 * 4, 32, 32)
        elif orientation == 'UP':
            animation_args = (32 * i, 32 * 5, 32, 32)
        elif orientation == 'RIGHT':
            animation_args = (32 * i, 32 * 6, 32, 32)
        elif orientation == 'LEFT':
            animation_args = (32 * i, 32 * 7, 32, 32)

    player_sprite = player_img.subsurface(*animation_args)
    scale = 3
    if state == 'ATTACK':
        player_sprite = pygame.transform.scale(player_sprite, (scale * 32, scale * 32))
        screen.blit(player_sprite, (x-16, y))
    else: #state == 'WALK':
        player_sprite = pygame.transform.scale(player_sprite, (scale * 16, scale * 32))
        screen.blit(player_sprite, (x, y))
    #FIXME: for the character to be centered during attack anim (x, y) must be transformed


def update_position(x, delta):
    return x + delta

# Game loop
running = True
frame = 0
t0 = pygame.time.get_ticks()
state = 'STOP'
orientation = 'DOWN'
force_attack_anim = 0
anim_counter = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_delta_x = -delta
                state = 'WALK'
                orientation = 'LEFT'
            if event.key == pygame.K_RIGHT:
                player_delta_x = delta
                state = 'WALK'
                orientation = 'RIGHT'
            if event.key == pygame.K_UP:
                player_delta_y = -delta
                state = 'WALK'
                orientation = 'UP'
            if event.key == pygame.K_DOWN:
                player_delta_y = delta
                state = 'WALK'
                orientation = 'DOWN'
            if event.key == pygame.K_SPACE:
                state = 'ATTACK'

        if event.type == pygame.KEYUP:
            if state != 'ATTACK':
                state = 'STOP'
                anim_counter = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_delta_y = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_delta_x = 0

    t1 = pygame.time.get_ticks()
    delta_time = t1 - t0
    screen.fill((100, 100, 100))
    player_x, player_y = update_position(player_x, player_delta_x), update_position(player_y, player_delta_y)

    animate(anim_counter, orientation, player_x, player_y, state)
    #attack_animation(frame, orientation)

    if delta_time > 100:
        frame += 1
        t0 = pygame.time.get_ticks()
        # Code to force full animation
        if state == 'ATTACK':
            anim_counter += 1
            if anim_counter == 4:
                state = 'STOP'
                anim_counter = 0
        elif state == 'WALK':
            anim_counter += 1

    pygame.display.update()
