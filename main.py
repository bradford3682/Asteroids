import pygame
from constants import *
from player import *
from asteroidfield import *
def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock =pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawable  = pygame.sprite.Group()
	dt=0
	
	asteroid=pygame.sprite.Group()
	Player.containers=(updatable,drawable)
	Asteroid.containers = (asteroid, updatable, drawable)
	AsteroidField.containers =updatable
	ready_player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
	asteroid_field=AsteroidField()
	while True:# start of game loop
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				return
	
		pygame.Surface.fill(screen,color=(0,0,0))#draw screen
		for object in updatable:
			object.update(dt)
		for object in asteroid:
			if object.collisions(ready_player1):
				return "Game over!"
				break
		for object in drawable:
			object.draw(screen)
		
		pygame.display.flip()
		dt=clock.tick(60)/1000
if __name__ == "__main__":
	main()
