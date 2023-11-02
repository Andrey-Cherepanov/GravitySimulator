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
    objects = []
    temp_obj_pos = None

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not temp_obj_pos:
                    temp_obj_pos = mouse_pos
                else:
                    t_x, t_y = temp_obj_pos
                    obj = Spacecraft(t_x, t_y, 0, 0, SHIP_MASS)
                    objects.append(obj)
                    temp_obj_pos = None


        window.blit(bg, (0,0))
        window.blit(planet, (WIDTH//2 - PLANET_SIZE, HEIGHT//2 - PLANET_SIZE))
        if temp_obj_pos:
            pygame.draw.line(window, COLORS['WHITE'], temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(window, COLORS['RED'], temp_obj_pos, SHIP_SIZE)

        for obj in objects:
            obj.draw()
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
