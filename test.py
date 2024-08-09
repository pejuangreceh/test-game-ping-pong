from pygame import *
# import os
import random

img_back = "background2.png"
img_player1 = "racket.png"
FPS = 60

win_width = 700
win_height = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# main player class
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed


display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))


player1 = Player(img_player1, 30, 200, 20, 100, 10)
player2 = Player(img_player1, 650, 200, 20, 100, 10)

finish = False
run = True # the flag is cleared with the close window button
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    if not finish:
        window.blit(background,(0,0))
        player1.update()
        player2.update2()

        player1.reset()
        player2.reset()
        display.update()
    time.delay(FPS)
