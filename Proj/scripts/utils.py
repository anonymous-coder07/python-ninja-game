import pygame
import os

BASIC_IMG_PATH = 'D:/Coding/Python/pygame-platformer/Proj/assets/data/images/'

def load_image(path):
    img = pygame.image.load(BASIC_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASIC_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))
    return images

class Animations:
    def __init__(self, images, img_dur = 5, loop = True) -> None:
        self.images = images
        self.loop = loop
        self.img_dur = img_dur
        self.done = False 
        self.frame = 0
    
    def copy(self):
        return Animations(self.images, self.loop, self.img_dur)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_dur * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_dur * len(self.images) - 1)
            if self.frame >= self.img_dur * len(self.images) - 1:
                self.done = True
            
    def img(self):
        return self.images[int(self.frame / self.img_dur)]