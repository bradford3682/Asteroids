import pygame
from constants import *
from player import *
def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock =pygame.time.Clock()
	dt=0
	ready_player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
	while True:# start of game loop
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				return
		pygame.Surface.fill(screen,color=(0,0,0))#draw screen
		ready_player1.update(dt)
		ready_player1.draw(screen)#draw player
		pygame.display.flip()
		dt=clock.tick(60)/1000
if __name__ == "__main__":
	main()
