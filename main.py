import pygame
import math

WIDTH, HEIGHT = 800, 600
PLANET_MASS = 100; SHIP_MASS = 5
G = 10
PLANET_SIZE = 50; SHIP_SIZE = 5
FPS = 60
VEL_SCALE = 100
COLORS = {'WHITE':(255,255,255), 'RED':(255,0,0), 'BLUE':(0,0,255)}

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity simulator")

bg_img = pygame.transform.scale(
                pygame.image.load("images/space.png"), (WIDTH, HEIGHT))
planet_img = pygame.transform.scale(
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

    def move(self, planet=None):
        distance = get_distance((self.x, self.y), (planet.x, planet.y))
        a = (G*planet.mass) / distance**2
        angle = math.atan2(planet.y - self.y, planet.x - self.x)

        acceleration_x = a * math.cos(angle)
        acceleration_y = a * math.sin(angle)

        self.vel_x += acceleration_x
        self.vel_y += acceleration_y

        self.x += self.vel_x
        self.y += self.vel_y

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

    def draw(self):

        window.blit(planet_img, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))

def create_ship(location, mouse):
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    obj = Spacecraft(t_x, t_y, vel_x, vel_y, SHIP_MASS)
    return obj

def get_distance(cords1, cords2):
    x1, y1 = cords1
    x2, y2 = cords2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def main():
    running = True
    clock = pygame.time.Clock()
    objects = []
    temp_obj_pos = None
    planet = Planet(WIDTH//2, HEIGHT//2, PLANET_MASS)

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
                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None


        window.blit(bg_img, (0,0))
        if temp_obj_pos:
            pygame.draw.line(window, COLORS['WHITE'], temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(window, COLORS['RED'], temp_obj_pos, SHIP_SIZE)

        for obj in objects[:]:
            obj.draw()
            obj.move(planet=planet)
            off_screen = any([obj.x < 0, obj.x > WIDTH, obj.y < 0, obj.y > HEIGHT])
            if get_distance((obj.x, obj.y), (planet.x, planet.y)) < PLANET_SIZE-10:
                objects.remove(obj)
            if off_screen:
                objects.remove(obj)
        planet.draw()

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
