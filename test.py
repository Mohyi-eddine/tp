from typing import Any
import pygame as p


class chiken(p.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.x = 50
        self.y = HEIGHT / 2
        self.vel = 4
        self.width = 100
        self.height = 50

        #image

        self.chiken333 = p.image.load('chiken333.jpg')
        self.chiken4 = p.image.load('chiken 4.jpg')
        self.chiken333 = p.transform.scale(self.chiken333, (self.width, self.height))
        self.chiken4 = p.transform.scale(self.chiken4, (self.width, self.height))
        self.image = self.chiken333
        self.rect = self.image.get_rect()

    def update(self):
        self.movement()
        self.correction()
        self.rect.center = (self.x, self.y)

    def movement (self):
        keys = p.key.get_pressed()
        if keys[p.K_q]:
            self.x -=self.vel
            self.image = self.chiken4

        elif keys[p.K_d]:
            self.x +=self.vel
            self.image = self.chiken333

        if keys[p.K_z]:
            self.y -=self.vel

        elif keys[p.K_s]:
            self.y +=self.vel

    def correction(self):
        if self.x - self.width / 2 < 0:
          self.x = self.width / 2

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2

        if self.y - self.height / 2 < 0:
          self.y = self.height / 2

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2



class car (p.sprite.Sprite):
    def _init_(self,number):
        super()._init_()
        if number == 1:
            self.x = 190
            self.image = p.image.load('slow car.jpg')
            self.vel = -4
        else:
            self.x = 460
            self.image = p.image.load('fast car.jpg')
            self.vel = 5

        self.y = HEIGHT / 2
        self.width = 100
        self.height = 150
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update (self):
        self.movement()
        self.rect.center = (self.x, self.y)

    def movement (self):
        self.y += self.vel
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.vel *= -1

        elif self.y + self.height / 2 > HEIGHT :
              self.y = HEIGHT - self.height / 2
              self.vel *= -1


class screen (p.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.img1 = p.image.load('scene.jpg')
        self.img2 = p.image.load('you win.jpg')
        self.img3 = p.image.load('you lose.jpg')

        self.img1 = p.transform.scale(self.img1, (WIDTH, HEIGHT))
        self.img2 = p.transform.scale(self.img2, (WIDTH, HEIGHT))
        self.img3 = p.transform.scale(self.img3, (WIDTH, HEIGHT))

        self.image = self.img1
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)


class car (p.sprite.Sprite):
    def _init_(self,number):
        super()._init_()
        self.number = number

        if self.number == 1:
            self.image = p.image.load('you win.jpg')
            self.visible = False
            self.x = 50

        else:
            self.image = p.image.load('you lose.jpg')
            self.visible = True
            self.x = 580

        self.y = HEIGHT / 2
        self.image = p.transform.scale2x(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        if self.visible:
            self.rect.center = (self.x, self.y)

def scoredisplay():
    score_text = score_font.render(str(SCORE) + ' / 5', True, (0, 0, 0))
    win.blit(score_text, (255, 10))

WIDTH = 640
HEIGHT = 480

p.init()

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('the chicken that cross the road')
clock = p.time.Clock()

SCORE = 0
score_font = p.font.SysFont('comicsans', 80, True)

bg = screen()
screen_group = p.sprite.Group()
screen_group.add(bg)

chiken = chiken()
chiken_group = p.sprite.Group()
chiken_group.add(chiken)

slow_car = car (1)
fast_car = car (2)
car_group = p.sprite.Group()
car_group.add(slow_car, fast_car)

run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.quit:
            run = False

    screen_group.draw(win)

    chiken_group.draw(win)
    car_group.draw(win)

    chiken_group.update()
    car_group.update()

    screen_group.update()
    scoredisplay()

    p.display.update()

p.quit()