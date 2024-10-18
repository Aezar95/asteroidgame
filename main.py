import sys
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
    # Loop over each bullet
            for shot in shots:
            # Check for collision
                if asteroid.collides_with(shot):
                # If they collide, call the kill method on both
                    asteroid.split()  # Remove the asteroid
                    shot.kill()    # Remove the bullet
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()