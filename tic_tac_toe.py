import pygame
from math import floor

pygame.init()
size = height, width = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

circle_img = pygame.image.load('circle.png')
cross_img = pygame.image.load('cross.png')

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = my_font.render('Crosses turn', False, (0, 0, 0))

class game_obj:
    def __init__(self, x, y, obj_img):
        self.x = x
        self.y = y
        self.obj_img = obj_img

    def update(self):
        screen.blit(self.obj_img, (self.x, self.y))

def convert_position_to_state(pos):
    box_size = 200
    x = floor(pos[0]/box_size)
    y = floor(pos[1] / box_size)
    return x, y

def set_game_state(game_state, current_state, i, j):
    if game_state[i][j] < 1:
        game_state[i][j] = current_state
    return game_state

def win_conditions(game_state):
    cond1 = game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0] != 0
    cond2 = game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and game_state[2][0] != 0
    if cond1 or cond2:
        return True, game_state[2][0]

    for i in range(3):
        if game_state[i][0] == game_state[i][1] and game_state[i][1] == game_state[i][2] and game_state[i][0] != 0:
            return True, game_state[i][0]
        if game_state[0][i] == game_state[1][i] and game_state[1][i] == game_state[2][i] and game_state[0][i] != 0:
            return True, game_state[0][i]
    return False, 0

# Game loop
running = True
game_objects = []
original_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_state = original_state
count = 0
win = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            i, j = convert_position_to_state(event.pos)
            if game_state[i][j] < 1:
                count += 1
                if count % 2 == 0:
                    current_img = circle_img
                    current_state = 1
                else:
                    current_img = cross_img
                    current_state = 2

                game_state[i][j] = current_state
                game_objects.append(game_obj(event.pos[0], event.pos[1], current_img))
            if current_state == 1:
                textsurface = my_font.render('Crosses turn', False, (0, 0, 0))
            elif current_state == 2:
                textsurface = my_font.render('Circles turn', False, (0, 0, 0))

            print(game_state)
            win, winner = win_conditions(game_state)
            if win:
                if winner == 1:
                    textsurface = my_font.render('Circles won', False, (0, 0, 0))
                elif winner == 2:
                    textsurface = my_font.render('Crosses won', False, (0, 0, 0))
                #game_state = original_state
                #game_objects = []

    screen.fill((100, 100, 100))
    pygame.draw.line(screen, (255, 255, 255), (200, 0), (200, 600), 5)
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, 200), (600, 200), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, 400), (600, 400), 5)

    for obj in game_objects:
        obj.update()

    if win:
        screen.blit(textsurface, (250, 300))
    else:
        screen.blit(textsurface, (0, 0))

    pygame.display.update()