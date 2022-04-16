import pygame

class Star(pygame.sprite.Sprite):
    def __init__(self, name, color, radius, mass, vec_pos):
        super().__init__()
        self.name = name
        self.color = color
        self.radius = radius
        self.mass = mass
        self.vec_pos = pygame.Vector2(vec_pos)

        self.sprite_sheet = pygame.image.load('images/Sun.png')
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (50, 50))

        self.rect = self.sprite_sheet.get_rect()
        self.rect = self.getVec_pos() - pygame.Vector2(25, 25)
        self.image = pygame.Surface([100, 100])
        self.image.blit(self.sprite_sheet, (0, 0, 43, 43))
        self.image.set_colorkey([0, 0, 0])



    # Getters
    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getVec_pos(self):
        return self.vec_pos