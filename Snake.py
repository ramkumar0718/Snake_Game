#infiniti-code
# Snake Game
import pygame
import time
import sys
import random

restart = 1

check_errors = pygame.init()
if check_errors[1] > 0:
    print('(Warning!)Found {0} Errors!'.format(check_errors[1]))
    sys.exit(-1)
else:
    print('(+)PyGame successfully initialized!')

# Play Surface

PlaySurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game ')

# Colors
red = pygame.Color(255, 0, 0)  # gameover
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
blue = pygame.Color(236, 28, 36)  # food

# FPS controller
fpsController = pygame.time.Clock()

# Important varibles
SnakePos = [100, 50]
SnakeBody = [[100, 50], [90, 50], [80, 50]]

FoodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
FoodSpawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# Display my name:
PlaySurface.fill(white)
pfont = pygame.font.SysFont('monaco', 35)
pSurf = pfont.render('Welcome to Snake Game', True, blue) # add your name here
pRect = pSurf.get_rect()
pRect.midtop = (360, 200)
PlaySurface.blit(pSurf, pRect)
pygame.display.flip()
time.sleep(3)

# Game over function
def gameOver():
    gFont = pygame.font.SysFont('Arial Black', 72)
    GOsurf = gFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    PlaySurface.blit(GOsurf, GOrect)
    showScore(0)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()  # pygame exit
    sys.exit()  # console exit


def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    sfFont = pygame.font.SysFont('monaco', 42)
    Ssurf = sFont.render('Score : {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (40, 10)
    else:
        Ssurf = sfFont.render('Score : {0}'.format(score), True, black)
        Srect.midtop = (340, 120)
    PlaySurface.blit(Ssurf, Srect)

# Main Logic of the game

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.type == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.type == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_UP or event.type == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.type == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validation of Directions
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # More on Directions OR Snake Position
    if direction == 'RIGHT':
        SnakePos[0] += 10
    if direction == 'LEFT':

        SnakePos[0] -= 10
    if direction == 'UP':
        SnakePos[1] -= 10
    if direction == 'DOWN':
        SnakePos[1] += 10

    # Snake Body Mechanism
    SnakeBody.insert(0, list(SnakePos))
    if SnakePos[0] == FoodPos[0] and SnakePos[1] == FoodPos[1]:
        score += 1
        FoodSpawn = False
    else:
        SnakeBody.pop()

    if FoodSpawn == False:
        FoodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    FoodSpawn = True

    # Drawings
    PlaySurface.fill(white)

    for pos in SnakeBody:
        pygame.draw.rect(PlaySurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(PlaySurface, blue, pygame.Rect(FoodPos[0], FoodPos[1], 10, 10))

    if SnakePos[0] > 710 or SnakePos[0] < 0:
        gameOver()
    if SnakePos[1] > 450 or SnakePos[1] < 0:
        gameOver()

    for block in SnakeBody[1:]:
        if SnakePos[0] == block[0] and SnakePos[1] == block[1]:
            gameOver()

    # common stuff
    showScore()
    pygame.display.flip()
    fpsController.tick(20)