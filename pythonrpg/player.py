import pygame

from sprite import Sprite
from input import is_key_pressed
from camera import camera

class Player(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.movement_speed = 5

    def update(self):
        if is_key_pressed(pygame.K_w):
            self.y -= self.movement_speed
        if is_key_pressed(pygame.K_a):
            self.x -= self.movement_speed
        if is_key_pressed(pygame.K_s):
            self.y += self.movement_speed
        if is_key_pressed(pygame.K_d):
            self.x += self.movement_speed

        #make the camera screen divided by 2 to make player in the center of the camera
        camera.x = self.x - camera.width / 2 + self.image.get_width() / 2
        camera.y = self.y - camera.height / 2 + self.image.get_height()/2
