from star import Star
from planet import Planet
from comet import Comet
import colors
import pygame
import math


class Simulation:
    def __init__(self, screen):

        self.screen = screen
        self.t = 0
        self.dt = 1

        self.G = 1  # Change to 6.67e-11 to use real-world values.
        self.running = True
        self.clock = pygame.time.Clock()

        # Star : Name, color, radius, mass, position, velocity
        self.sun = Star("Sun", colors.YELLOW, 20, 1.989e30 / scale_mass, (screen_width_half, screen_height_half))

        # Planet : Name, color, radius, mass, position, velocity, has_ring
        self.mercury = Planet("Mercury", colors.GRAY, 2, 3.285e23 / scale_mass,
                              (screen_width_half - 58, screen_height_half), (0, 0))

        self.venus = Planet("Venus", colors.YELLOW_ORANGE, 5, 4.867e24 / scale_mass,
                            (screen_width_half - 108, screen_height_half), (0, 0))
        self.earth = Planet("Earth", colors.BLUE, 5, 5.972e24 / scale_mass, (screen_width_half - 149.6, screen_height_half),
                            (0, 0))
        self.mars = Planet("Mars", colors.RED, 4, 6.89e23 / scale_mass, (screen_width_half - 228, screen_height_half),
                           (0, 0))

        self.jupiter = Planet("Jupiter", colors.CAMEO, 10, 1.898e27 / scale_mass,
                              (screen_width_half - 778, screen_height_half), (0, 0))

        self.saturn = Planet("Saturn", colors.SATURN, 9, 5.683e26 / scale_mass,
                             (screen_width_half - 900, screen_height_half), (0, 0))

        # self.moon = Planet("Moon", colors.WHITE, 1, 7.6e22 / scale_mass,
        # (screen_width_half - 151, screen_height_half), (0, 0))

        # self.phobos = Planet("Phobos", colors.WHITE, 1, 1.072e16 / scale_mass,
                            # (screen_width_half - 228 - 6, screen_height_half), (0, 0))


        """
        - Essayer de créer l'objet lorsque l'on clic, ainsi l'objet n'est plus initialisé dès le début et le bug disparait
        - Il faut donc aussi pouvoir détruire l'objet, et le reconstruire.
        """
        # Comet : color, radius, mass, position, velocity
        self.comet = Comet("Halley", colors.WHITE, 1, 2.2e14 / scale_mass, (0, 0), (0, 0))

        # Comet isn't a planet but this is easier to code if we include in it
        self.planets = [self.mercury, self.venus, self.earth, self.mars, self.jupiter, self.saturn]

        # We initialize their trail and their initial velocity
        for p in self.planets:
            self.initialVelocity(p)
            p.trail = []
        self.comet.trail = []

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP:

                # We catch the vector position of the mouse click
                # comet_pos = event.pos
                self.comet.setVec_pos(event.pos)
                # We create the object comet
                # Comet : color, radius, mass, position, velocity
                # self.comet = Comet("Halley", colors.WHITE, 1, 1000, comet_pos, (0, 0))

                # Reset the velocity
                self.initialVelocity(self.comet)

                # We need to remove the objet if he is instanced

                # If this is the first click, the object doesn't exist
                # We need to catch this error
                try:
                    self.planets.remove(self.comet)
                except ValueError:
                    self.planets.append(self.comet)

                # On the first click we don't want to instance two comets object in the list
                # So we need to check it
                if self.comet not in self.planets:
                    self.planets.append(self.comet)

                # We create the object comet
                # Comet : color, radius, mass, position, velocity
                #self.comet = Comet("Halley", colors.WHITE, 1, 1000, (screenWidthHalf - 500, screenHeightHalf), (0, 0))

                # We need to remove the objet if he is instanced

                # If this is the first click, the object doesn't exist
                # We need to catch this error
                try:
                    self.planets.remove(self.comet)
                except ValueError:
                    self.planets.append(self.comet)

                # On the first click we don't want to instance two comets object in the list
                # So we need to check it
                if self.comet not in self.planets:
                    self.planets.append(self.comet)

                # Reset the velocity
                self.initialVelocity(self.comet)

                # We catch the vector position of the mouse click
                self.comet.setVec_pos(event.pos)


    def update(self):

        # Calculate forces
        '''self.sun.force = self.gforce(self.sun, self.comet)
        for p in self.planets:
            self.sun.force += self.gforce(self.sun, p)
            p.force = self.gforce(p, self.sun)

            # Si commenter la comète fonctionne
            for next_p in self.planets:
                try:
                    p.force += self.gforce(p, next_p)
                except ValueError:
                    pass'''


        self.sun.force = self.gforce(self.sun, self.earth) \
                         + self.gforce(self.sun, self.mercury) \
                         + self.gforce(self.sun, self.venus) \
                         + self.gforce(self.sun, self.mars) \
                         + self.gforce(self.sun, self.jupiter) \
                         + self.gforce(self.sun, self.saturn) \
                         + self.gforce(self.sun, self.comet)
            # + self.gforce(self.sun, self.phobos)
        # + self.gforce(self.sun, self.moon) \

        self.mercury.force = self.gforce(self.mercury, self.sun) \
                             + self.gforce(self.mercury, self.earth) \
                             + self.gforce(self.mercury, self.venus) \
                             + self.gforce(self.mercury, self.mars) \
                             + self.gforce(self.mercury, self.jupiter) \
                             + self.gforce(self.mercury, self.saturn) \
                             + self.gforce(self.mercury, self.comet)

        self.venus.force = self.gforce(self.venus, self.sun) \
                           + self.gforce(self.venus, self.mercury) \
                           + self.gforce(self.venus, self.earth) \
                           + self.gforce(self.venus, self.mars) \
                           + self.gforce(self.venus, self.jupiter) \
                           + self.gforce(self.venus, self.saturn) \
                           + self.gforce(self.venus, self.comet)

        self.earth.force = self.gforce(self.earth, self.sun) \
                           + self.gforce(self.earth, self.mercury) \
                           + self.gforce(self.earth, self.venus) \
                           + self.gforce(self.earth, self.jupiter) \
                           + self.gforce(self.earth, self.saturn) \
                           + self.gforce(self.earth, self.mars) \
                           + self.gforce(self.earth, self.comet) \
            # + self.gforce(self.earth, self.moon)

        # self.moon.force = self.gforce(self.moon, self.sun) + \
        # + self.gforce(self.moon, self.earth)

        self.mars.force = self.gforce(self.mars, self.sun) \
                          + self.gforce(self.mars, self.earth) \
                          + self.gforce(self.mars, self.venus) \
                          + self.gforce(self.mars, self.mercury) \
                          + self.gforce(self.mars, self.jupiter) \
                          + self.gforce(self.mars, self.saturn) \
                          + self.gforce(self.mars, self.comet) \
            # + self.gforce(self.mars, self.phobos)

        # self.phobos.force = self.gforce(self.phobos, self.sun) \
                          # + self.gforce(self.phobos, self.mars)

        self.jupiter.force = self.gforce(self.jupiter, self.sun) \
                             + self.gforce(self.jupiter, self.mars) \
                             + self.gforce(self.jupiter, self.earth) \
                             + self.gforce(self.jupiter, self.venus) \
                             + self.gforce(self.jupiter, self.mercury) \
                             + self.gforce(self.jupiter, self.saturn) \
                             + self.gforce(self.jupiter, self.comet)

        self.saturn.force = self.gforce(self.saturn, self.sun) \
                            + self.gforce(self.saturn, self.earth) \
                            + self.gforce(self.saturn, self.venus) \
                            + self.gforce(self.saturn, self.mercury) \
                            + self.gforce(self.saturn, self.mars) \
                            + self.gforce(self.saturn, self.jupiter) \
                            + self.gforce(self.saturn, self.comet) \

        self.comet.force = self.gforce(self.comet, self.sun) \
                           + self.gforce(self.comet, self.earth) \
                           + self.gforce(self.comet, self.venus) \
                           + self.gforce(self.comet, self.mercury) \
                           + self.gforce(self.comet, self.mars) \
                           + self.gforce(self.comet, self.jupiter) \
                           + self.gforce(self.comet, self.saturn) \



        # Calculate velocity
        for p in self.planets:
            # Calculate velocity
            self.velocity(p)
            # Update position
            # Before update the position, we add the current position for each planet
            p.trail.append(p.getVec_pos())
            self.updatePosition(p)

        self.t = self.t + self.dt

    def display(self):
        screen.fill(colors.BLACK)
        screen.blit(background, (0, 0))
        # draw the sun
        # self.draw(screen, self.sun)
        screen.blit(self.sun.image, self.sun.rect)

        # Draw all planets
        for p in self.planets:
            self.draw(screen, p)

            # We catch the error of the comet because I don't want to have an image
            try:
                screen.blit(p.image, p.rect)
            except AttributeError:
                pygame.draw.circle(screen,p.getColor(),p.getVec_pos(), p.getRadius())
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)

    def draw(self, screen, planetOrStar):

        # pygame.draw.circle(screen, planetOrStar.getColor(), planetOrStar.getVec_pos(), planetOrStar.getRadius())
        # We have an error because the Sun and the comet is included, but he doesn't need a trail, so we catch it
        try:
            for pos in planetOrStar.trail:
                pygame.draw.line(screen, planetOrStar.getColor(), pos, pos, 1)

                # We need to clear the list to avoid a lot of data position
                if len(planetOrStar.trail) >= 100:
                    planetOrStar.trail.pop(0)

        except AttributeError:
            planetOrStar.trail = []  # I create his trail to avoid the error, there are maybe a better solution

    def gforce(self, p1, p2):

        # Calculate the gravitational force exerted on p1 by p2.

        # Calculate the distance between two points
        vec_dist = (pygame.Vector2.magnitude(p1.getVec_pos() - p2.getVec_pos())) ** 2

        # Calculate the directional vector
        vec_dir = pygame.Vector2(p1.getVec_pos() - p2.getVec_pos()).normalize()

        # Calculate the force vector
        vec_force = pygame.Vector2(- vec_dir * self.G * p1.getMass() * p2.getMass() / vec_dist)

        return vec_force

    def velocity(self, planet):
        # acc = F / M
        # the velocity update is v = v + acc * dt
        acceleration = planet.force / planet.getMass()
        planet.setVec_vit(planet.getVec_vit() + acceleration * self.dt)

    def updatePosition(self, planet):
        planet.setVec_pos(planet.getVec_pos() + planet.getVec_vit() * self.dt)

        # For images
        if planet.getName() == "Mercury":
            planet.rect = planet.getVec_pos() - pygame.Vector2(8, 8)
        elif planet.getName() == "Jupiter":
            planet.rect = planet.getVec_pos() - pygame.Vector2(16.5, 17)
        elif planet.getName() == "Saturn":
            planet.rect = planet.getVec_pos() - pygame.Vector2(41.5, 20.5)
        else:
            planet.rect = planet.getVec_pos() - pygame.Vector2(16, 16)


    def initialVelocity(self, planet):
        # Calculate the distance between the sun and planets

        vec_dist = (pygame.Vector2.magnitude(planet.getVec_pos() - self.sun.getVec_pos()))
        planet.setVec_vit(pygame.Vector2(0, math.sqrt((self.G * (self.sun.getMass())) / vec_dist)))

        # Calculate initial velocity
        # This one is for a circular orbital
        # planet.setVec_vit(pygame.Vector2(0, math.sqrt((self.G * (self.sun.getMass())) / vec_dist)))


# VARIABLES #
#############

pygame.init()

scale_mass = 10e27
scale = 149_600_000 / 250

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
# we divide by 2 to have the center of the screen and then place the sun on it
screen_width_half = screen_width // 2
screen_height_half = screen_height // 2

background = pygame.image.load("images/background.jpg")
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Solar System Simulation")

simulation = Simulation(screen)

simulation.run()
pygame.quit()