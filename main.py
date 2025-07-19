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
    player1 = player.player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2) 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player1.draw(screen)
        pygame.display.flip()
        dt = fps.tick(60) / 1000



if __name__ == "__main__":
    main()
