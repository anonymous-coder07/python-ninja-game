import pygame
import os

BASIC_IMG_PATH = 'D:/Python/pygame-platformer/Proj/assets/data/images/'

def load_image(path):
    img = pygame.image.load(BASIC_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASIC_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))
    return images