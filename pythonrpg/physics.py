
from pygame import Rect

bodies = []


class Body:
    def __init__(self, x=0, y=0, width=32, height=32):
        self.hitbox = Rect(x, y, width, height)
        bodies.append(self)
    def is_colliding(self, other):
        x = self.hitbox.x + other.hitbox.x