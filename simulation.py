import pygame
import colors

from star import Star
from planet import Planet
from comet import Comet


class Simulation:
    def __init__(self, screen):

        self.screen = screen
        self.t = 0
        self.dt = 1
        self.G = 1  # Change to 6.67e-11 to use real-world values.
        self.running = True
        self.clock = pygame.time.Clock()

        # Star : Name, color, radius, mass, position, velocity
        self.sun = Star("Sun", colors.YELLOW, 20, 1.989e30 / scale_mass, (screenWidthHalf, screenHeightHalf))

        # Planet : Name, color, radius, mass, position, velocity, has_ring
        self.mercury = Planet("Mercury", colors.GRAY, 2, 3.285e23 / scale_mass,
                              (screenWidthHalf - 58, screenHeightHalf), (0, 0), False)

        self.venus = Planet("Venus", colors.YELLOW_ORANGE, 5, 4.867e24 / scale_mass,
                            (screenWidthHalf - 108, screenHeightHalf), (0, 0),
                            False)
        self.earth = Planet("Earth", colors.BLUE, 5, 5.972e24 / scale_mass, (screenWidthHalf - 149.6, screenHeightHalf),
                            (0, 0), False)
        self.mars = Planet("Mars", colors.RED, 4, 6.89e23 / scale_mass, (screenWidthHalf - 228, screenHeightHalf),
                           (0, 0), False)

        self.jupiter = Planet("Jupiter", colors.CAMEO, 10, 1.898e27 / scale_mass,
                              (screenWidthHalf - 778, screenHeightHalf), (0, 0),
                              False)

        self.saturn = Planet("Saturn", colors.SATURN, 9, 5.683e26 / scale_mass,
                             (screenWidthHalf - 1_900, screenHeightHalf), (0, 0), True)

        # self.moon = Planet("Moon", colors.WHITE, 1, 7.6e22 / scale_mass,
        # (screenWidthHalf - 151, screenHeightHalf), (0, 0), False)

        #self.phobos = Planet("Phobos", colors.WHITE, 1, 1.072e16 / scale_mass,
                            # (screenWidthHalf - 228 - 6, screenHeightHalf), (0, 0), False)


        """
        - Essayer de créer l'objet lorsque l'on clic, ainsi l'objet n'est plus initialisé dès le début et le bug disparait
        - Il faut donc aussi pouvoir détruire l'objet, et le reconstruire.
        """
        # Comet : color, radius, mass, position, velocity
        self.comet = Comet("Halley", colors.WHITE, 1, 2.2e14 / scale_mass, (0, 0), (0, 0))

        # Comet isn't a planet but this is more easier to code if we include in it
        self.planets = [self.mercury, self.venus, self.earth, self.mars, self.jupiter, self.saturn]

        # We initialize their trail and their initial velocity
        for p in self.planets:
            self.initialVelocity(p)
            p.trail = []
        self.comet.trail = []
