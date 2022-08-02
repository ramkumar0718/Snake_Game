import pygame
import random
from os import path
pygame.init()
pygame.font.init()

# Display Window
WIDTH, HEIGHT = 750, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255,255,255)
BLACK = (0, 0, 0)
BLUE = (71, 118, 236)
GREEN = (0, 255, 0)           
RED = (236, 28, 36)
SKY_BLUE = (59, 242, 252)
ORANGE = (252, 149, 59)

# Game Control
FPS = 15
VEL = 10
RECT_WIDTH = RECT_HEIGHT = 10

# Variables
score = 0
snakePosition = [200, 200]
snakeBody = [[200, 200], [190, 200], [180, 200]]
foodPosition = [random.randrange(1, WIDTH//10 - 10) * 10, random.randrange(1, HEIGHT//10 - 10) * 10]
Food = True

# Font
font = lambda font_size : pygame.font.Font('Assets/Poppins.ttf', font_size)


clicked = False
class Button():
	Button_Width = 130
	Button_Height = 50

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):
		global clicked
		action = False

		pos = pygame.mouse.get_pos()
		Button_Rect = pygame.Rect(self.x, self.y, self.Button_Width, self.Button_Height)
		
		if Button_Rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(WIN, ORANGE, Button_Rect, border_radius=7) # Clicked Color
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(WIN, ORANGE, Button_Rect, border_radius=7) # Hover Color
		else:
			pygame.draw.rect(WIN, SKY_BLUE, Button_Rect, border_radius=7)	# Button Color

		#add text to button
		pygame.font.init()
		TEXT = font(20).render(self.text, 1, BLACK)
		TEXT_WIDTH = TEXT.get_width()
		WIN.blit(TEXT, (self.x + self.Button_Width//2 - 32, self.y + 12))
		return action


# Displaying Highscore on top of the window
def display_highscore():
	if not path.exists("Assets/highscore.txt"):
		with open("Assets/highscore.txt", "a") as file:
			file.write("0")
	with open("Assets/highscore.txt", "r") as file:
		f = file.read()
		pygame.display.set_caption(f"{'Snake Game'}{'   |   '}{'Highest score: '}{str(f)}")


# Update score in file
def update_high_score():
	global score
	file_r = open("Assets/highscore.txt", "r")
	f = file_r.read()
	with open("Assets/highscore.txt", "w") as file_w:
		if score > int(f):
			file_w.write(str(score))
		else:
			file_w.write(f)	
	file_r.close()
	

# Display game stage and score
def display_game_stage_and_score(main):
	color = GREEN if main == "Paused" else RED 
	MAIN_TEXT = font(68).render("Game " + main + "!", 1, color)
	MAIN_TEXT_RECT = MAIN_TEXT.get_rect()
	MAIN_TEXT_RECT.midtop = (WIDTH//2, HEIGHT//10)
	WIN.blit(MAIN_TEXT, MAIN_TEXT_RECT)

	SCORE_TEXT = font(45).render("Score: " + str(score), 1, BLACK)
	SCORE_TEXT_RECT = SCORE_TEXT.get_rect()
	SCORE_TEXT_RECT.midtop = (WIDTH//2, HEIGHT//3)
	WIN.blit(SCORE_TEXT, SCORE_TEXT_RECT)


# Dark Mode of the game
def dark_mode():
	global WHITE, BLUE, BLACK, RED, FPS
	if (score >= 25 and score <= 50) or (score >= 75 and score <= 100) or (score >= 125 and score <= 150) or (score >= 175 and score <= 200) or (score >= 225 and score <= 250) or (score >= 275 and score <= 300) or (score >= 325 and score <= 350) or (score >= 375 and score <= 400) or (score >= 425 and score <= 450) or (score >= 475 and score <= 500) or (score >= 525 and score <= 550) or (score >= 575 and score <= 600) or (score >= 625 and score <= 650) or (score >= 675 and score <= 700) or (score >= 725 and score <= 750) or (score >= 775 and score <= 800) or (score >= 825 and score <= 850) or (score >= 875 and score <= 900) or (score >= 925 and score <= 950) or (score >= 975 and score <= 999):
		WHITE = (0, 0, 0)			# BLACK
		BLACK = (255, 255, 255)		# WHITE
		BLUE = (0, 255, 0)			# GREEN
		RED = (255, 20, 147)		# PINK
		FPS = 18					# Increase speed
	else:
		WHITE = (255, 255, 255)
		BLUE = (71, 118, 236)
		BLACK = (0, 0, 0)
		RED = (236, 28, 36)
		FPS = 15


# Game Pause
def pause():
	pause = True

	while pause:
		WIN.fill(WHITE)
		resume = Button(x = WIDTH//8 + 10, y = HEIGHT - HEIGHT//2.5, text = 'Resume')
		quit = Button(x = WIDTH//1.5, y = HEIGHT - HEIGHT//2.5, text = '  Quit')
		if resume.draw_button():
			pause = False
		if quit.draw_button():
			pygame.quit()
		display_game_stage_and_score("Paused")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				update_high_score()
				pygame.quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pause = False
		pygame.display.update()


# Gameover Function
def game_over():
	global score
	update_high_score()
	exit = True

	while exit:
		WIN.fill(WHITE)
		replay = Button(x = WIDTH//8 + 10, y = HEIGHT - HEIGHT//2.5, text = 'Replay')
		quit = Button(x = WIDTH//1.5, y = HEIGHT - HEIGHT//2.5, text = '  Quit')
		if replay.draw_button():
			score = 0
			main()
		if quit.draw_button():
			exit = False
			pygame.quit()
		display_game_stage_and_score("Over")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				update_high_score()
				pygame.quit()				
		pygame.display.update()


# Main Function
def main():	
	global FPS, Food, score

	snakePosition = [200, 200]
	snakeBody = [[200, 200], [190, 200], [180, 200]]
	foodPosition = [random.randrange(1, WIDTH//10 - 10) * 10, random.randrange(1, HEIGHT//10 - 10) * 10]
	direction = "RIGHT"
	direction_go_to = direction

	clock = pygame.time.Clock()
	run = True
	
	# Main Loop
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				update_high_score()
				run = False
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					direction_go_to = "RIGHT"
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					direction_go_to = "LEFT"
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					direction_go_to = "UP"
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					direction_go_to = "DOWN"
				if event.key == pygame.K_SPACE:
					pause()

		if direction_go_to == "RIGHT" and not direction == "LEFT":
			direction = "RIGHT"
		if direction_go_to == "LEFT" and not direction == "RIGHT":
			direction = "LEFT"
		if direction_go_to == "UP" and not direction == "DOWN":
			direction = "UP"
		if direction_go_to == "DOWN" and not direction == "UP":
			direction = "DOWN"

		if direction == "RIGHT":
			snakePosition[0] += VEL
		if direction == "LEFT":
			snakePosition[0] -= VEL
		if direction == "UP":
			snakePosition[1] -= VEL
		if direction == "DOWN":
			snakePosition[1] += VEL

		WIN.fill(WHITE)
		snakeBody.insert(0, list(snakePosition))
		if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
			score += 1
			Food = False
		else:
			snakeBody.pop()

		if Food == False:
			foodPosition = [random.randrange(1, WIDTH//10 - 10) * 10, random.randrange(1, HEIGHT//10 - 10) * 10]
		Food = True

		for Position in snakeBody:
			pygame.draw.rect(WIN, BLUE, 
				pygame.Rect(Position[0], Position[1], RECT_WIDTH, RECT_HEIGHT))
		pygame.draw.rect(WIN, RED,
			pygame.Rect(foodPosition[0], foodPosition[1], RECT_WIDTH, RECT_HEIGHT))
		dark_mode()

		# Wall Hit
		if snakePosition[0] > WIDTH - 10 or snakePosition[0] < 0:
			game_over()
		if snakePosition[1] > HEIGHT - 10 or snakePosition[1] < 0:
			game_over()

		# Snake Hit
		for x in snakeBody[1:]:
			if snakePosition[0] == x[0] and snakePosition[1] == x[1]:
				game_over()

		SCORE_TEXT = font(23).render("Score: " + str(score), 1, BLACK)
		SCORE_TEXT_RECT = (10, 10)
		WIN.blit(SCORE_TEXT, SCORE_TEXT_RECT)

		display_highscore()
		pygame.display.update()
		
if __name__ == "__main__":
	main()