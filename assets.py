import pygame as pg

from loader import loadAssets

pixelResolution = 32

assets: dict[str, pg.Surface] = {}
assets.update(loadAssets("Assets", size=(pixelResolution, pixelResolution)))

fontLocation = "Assets/Fonts/"

