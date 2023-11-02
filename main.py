import pygame
import math

WIDTH, HEIGHT = 800, 600
PLANET_MASS = 100; SHIP_MASS = 5
G = 5
PLANET_SIZE = 50; SHIP_SIZE = 5
FPS = 60
VEL_SCALE = 100
COLORS = {'WHITE':(255,255,255), 'RED':(255,0,0), 'BLUE':(0,0,255)}

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity simulator")

bg = pygame.transform.scale(
                pygame.image.load("images/space.png"), (WIDTH, HEIGHT))
planet = pygame.transform.scale(
                pygame.image.load("images/planet.png"), (PLANET_SIZE*2,PLANET_SIZE*2))

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__':
    main()
