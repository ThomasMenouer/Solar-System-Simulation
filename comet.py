import pygame


class Comet():
    def __init__(self, name, color, radius, mass, vec_pos, vec_vit):
        super().__init__()
        self.name = name
        self.color = color
        self.radius = radius
        self.mass = mass
        self.vec_pos = pygame.Vector2(vec_pos)
        self.vec_vit = pygame.Vector2(vec_vit)

        '''
        self.sprite_sheet = pygame.image.load("images/Mercury.png")
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (16, 16))
        self.image = pygame.Surface([16, 16])
        self.image.blit(self.sprite_sheet, (0, 0, 32, 32))
        self.image.set_colorkey([0, 0, 0])
        '''

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

    def getVec_vit(self):
        return self.vec_vit

    # Setters
    def setVec_pos(self, newVec_pos):
        self.vec_pos = newVec_pos

    def setVec_vit(self, newVec_vit):
        self.vec_vit = newVec_vit
