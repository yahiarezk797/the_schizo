import constants
import pygame
import player
import asteroid
from asteroidfield import *
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    player.Shot.containers = (shot, updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    player.Player.containers = (drawable, updatable)
    AsteroidField.containers = (updatable)
    astroidfield1 = AsteroidField()
    player1 = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        for thing in updatable:
            thing.update(dt)
        for thing in asteroids:
            for small in shot:
                if thing.is_colliding(small):
                    thing.split()
                    small.kill()
            if thing.is_colliding(player1):
                sys.exit("Game over!")
        dt = fps.tick(60) / 1000



if __name__ == "__main__":
    main()
