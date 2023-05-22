import pygame
import sprite 
class Tile(sprite.Sprite):
    def __init__(self, image_file, positions, collision_bool):
        #sprite.Sprite.__init__(self, image_file, positions)
        sprite.Sprite.__init__(self, image_file , positions)
        self.collide = collision_bool
        
    
    def collision(obj):
        if self.collide == True:
            if obj.rect[0] < (self.rect[0] + self.size[0]) and obj.rect[1] < (self.rect[1] + self.size[1]):
                if obj.rect[0] > self.rect[0] and obj.rect[0] < (self.rect[0] + self.size[0]) or (obj.rect[0] + self.size[0]) > self.rect[0] and (obj.rect[0] + self.size[0]) < (self.rect[0] + self.size[0]):
                       pass

            if obj.rect[0] > self.rect[0] and obj.rect[0] < (self.rect[0] + self.size[0])  or (obj.rect[0] + self.size[0]) > self.rect[0] and (obj.rect[0] + self.size[0]) < (self.rect[0] + self.size[0]):
                    pass


