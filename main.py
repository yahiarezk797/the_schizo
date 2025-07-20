import constants
import pygame
import player

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
    player.player.containers = (drawable, updatable)
    player1 = player.player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
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
        dt = fps.tick(60) / 1000



if __name__ == "__main__":
    main()
