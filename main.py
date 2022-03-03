import pygame

from constants import WINDOW_WIDTH, WINDOW_HEIGHT


def main():
    pygame.init()
    pygame.display.set_caption('Future teller')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


main()
