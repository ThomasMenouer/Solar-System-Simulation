import pygame


class Planet(pygame.sprite.Sprite):
    def __init__(self, name, color, radius, mass, vec_pos, vec_vit):
        super().__init__()
        self.name = name
        self.color = color
        self.radius = radius
        self.mass = mass
        self.vec_pos = pygame.Vector2(vec_pos)
        self.vec_vit = pygame.Vector2(vec_vit)

        if self.getName() == "Mercury":

            self.sprite_sheet = pygame.image.load("images/Mercury.png")
            self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (16, 16))
            self.image = pygame.Surface([16, 16])
            self.image.blit(self.sprite_sheet, (0, 0, 32, 32))
            self.image.set_colorkey([0, 0, 0])

        elif self.getName() == "Venus":

            self.sprite_sheet = pygame.image.load("images/Venus.png")
            self.image = pygame.Surface([32, 32])
            self.image.blit(self.sprite_sheet, (0, 0, 32, 32))
            self.image.set_colorkey([0, 0, 0])

        elif self.getName() == "Earth":

            self.sprite_sheet = pygame.image.load("images/Earth.png")
            self.image = pygame.Surface([32, 32])
            self.image.blit(self.sprite_sheet, (0, 0, 32, 32))
            self.image.set_colorkey([0, 0, 0])

        elif self.getName() == "Mars":

            self.sprite_sheet = pygame.image.load("images/Mars.png")
            self.image = pygame.Surface([32, 32])
            self.image.blit(self.sprite_sheet, (0, 0, 32, 32))
            self.image.set_colorkey([0, 0, 0])

        elif self.getName() == "Jupiter":
            self.sprite_sheet = pygame.image.load("images/Jupiter.png")
            self.image = pygame.Surface([33, 34])
            self.image.blit(self.sprite_sheet, (0, 0, 33, 34))
            self.image.set_colorkey([0, 0, 0])

        elif self.getName() == "Saturn":
            self.sprite_sheet = pygame.image.load("images/Saturn.png")
            self.image = pygame.Surface([83, 41])
            self.image.blit(self.sprite_sheet, (0, 0, 83, 41))
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

    def getVec_vit(self):
        return self.vec_vit

    # Setters
    def setVec_pos(self, newVec_pos):
        self.vec_pos = newVec_pos

    def setVec_vit(self, newVec_vit):
        self.vec_vit = newVec_vit
