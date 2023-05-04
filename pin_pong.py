from pygame import *
import pygame

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width=70, height=70):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.speed = speed

    def reset(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 435:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

#создай окно игры
wind = display.set_mode((700, 500))
display.set_caption('pin pong')
wind.fill((130, 100, 200))

clock = time.Clock()
FPS = 60
clock.tick(FPS)

racket1 = Player('platform_v.png', 25, 150, 1, 25, 70)
racket2 = Player('platform_v.png', 650, 150, 1, 25, 70)

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        wind.fill((130, 100, 200))
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()


    display.update()