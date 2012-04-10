import pygame
from pygame.locals import *

class Button(object):

    def __init__(self, image_filename, position):
        self.position = position
        self.image = pygame.image.load(image_filename)

    def render(self, surface):
        # Render at the center
        x, y = self.position
        w, h = self.image.get_size()
        x -= w /2
        y -= h / 2
        surface.blit(self.image, (x, y))

    def is_over(self, point):
        # Return True if a point is over the button
        point_x, point_y = point
        x, y = self.position
        w, h = self.image.get_size()
        x -= w /2
        y -= h / 2
        in_x = point_x >= x and point_x < x + w
        in_y = point_y >= y and point_y < y + h

        return in_x and in_y