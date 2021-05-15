import pygame
import time
import sys
import random
pygame.font.init()

WIDTH, HEIGHT = 720, 460
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
RED = pygame.Color(255, 0, 0)       
GREEN = pygame.Color(0, 255, 0)     
BLACK = pygame.Color(0, 0, 0)       
WHITE = pygame.Color(255, 255, 255) 
BLUE = pygame.Color(236, 28, 36)    
PINK = pygame.Color(255,20,147)     

# Important varibles
score = 0
snakepos = [100, 50]
snakebody = [[100, 50], [90, 50], [80, 50]]
foodpos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
FoodSpawn = True
direction = 'RIGHT'
change_to = direction

# Display my name:
WIN.fill(WHITE)
pFont = pygame.font.SysFont('Berlin Sans FB Demi', 50)
pSurf = pFont.render('Welcome to Snake Game', True, PINK)
pRect = pSurf.get_rect()
pRect.midtop = (360, 160)
WIN.blit(pSurf, pRect)
pygame.display.flip()
time.sleep(4)

def gameOver():
    gFont = pygame.font.SysFont('Berlin Sans FB Demi', 72)
    gSurf = gFont.render('Game over !', True, RED)
    gRect = gSurf.get_rect()
    gRect.midtop = (360, 15)
    WIN.blit(gSurf, gRect)
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()

def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    sfFont = pygame.font.SysFont('Source Code Pro Black', 42)
    sSurf = sFont.render('Score : {0}'.format(score), True, BLACK)
    sRect = sSurf.get_rect()
    if choice == 1:
        sRect.midtop = (40, 10)
    else:
        sSurf = sfFont.render('Score : {0}'.format(score), True, BLACK)
        sRect.midtop = (280, 120)
    WIN.blit(sSurf, sRect)

# Main Loop
while True:
    FPS = pygame.time.Clock()

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
        snakepos[0] += 10
    if direction == 'LEFT':
        snakepos[0] -= 10
    if direction == 'UP':
        snakepos[1] -= 10
    if direction == 'DOWN':
        snakepos[1] += 10

    # Snake Body Mechanism
    snakebody.insert(0, list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        score += 1
        FoodSpawn = False
    else:
        snakebody.pop()

    if FoodSpawn == False:
        foodpos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    FoodSpawn = True

    # Drawings
    WIN.fill(WHITE)
    for pos in snakebody:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(WIN, BLUE, pygame.Rect(foodpos[0], foodpos[1], 10, 10))

    if snakepos[0] > WIDTH - 10 or snakepos[0] < 0:
        gameOver()
    if snakepos[1] > HEIGHT - 10 or snakepos[1] < 0:
        gameOver()

    for block in snakebody[1:]:
        if snakepos[0] == block[0] and snakepos[1] == block[1]:
            gameOver()

    # Conclusion
    showScore()
    pygame.display.flip()
    FPS.tick(15)