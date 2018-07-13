import os
import pygame as pg


def load_all_gfx(directory, colorkey=(255, 0, 255),
                 accept=('.png', '.jpg', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics


def load_all_music(directory,
                   accept=('.wav', '.mp3', '.ogg', '.mdi', '.flac')):
    songs = {}
    for song in os.listdir(directory):
        name, ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs


def load_all_fonts(directory,
                   accept=('.ttf')):
        fonts = {}
        for font in os.listdir(directory):
            name, ext = os.path.splitext(font)
            if ext.lower() in accept:
                fonts[name] = os.path.join(directory, font)
        return fonts


def load_all_sfx(directory,
                 accept=('.wav', '.mpe', '.ogg', '.mdi')):
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects
