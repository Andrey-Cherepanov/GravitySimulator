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


class Spacecraft:

    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass

    def draw(self):
        pygame.draw.circle(window, COLORS['RED'], (int(self.x), int(self.y)), SHIP_SIZE)

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.blit(bg, (0,0))
        window.blit(planet, (WIDTH//2 - PLANET_SIZE, HEIGHT//2 - PLANET_SIZE))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
