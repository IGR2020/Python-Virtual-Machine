import pygame as pg

from assets import pixelResolution, assets


class Pixel:
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, pixelResolution, pixelResolution)
        self.state = False

    def display(self, window: pg.Surface):
        if self.state:
            window.blit(assets["On"], self.rect)
        else:
            window.blit(assets["Off"], self.rect)