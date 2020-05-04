import pygame as pg
from settings import *
from os import path
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.mysprite
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE

    def get_keys(self):

        #game_folder = path.dirname(__file__)
        #img_folder = path.join(game_folder, "assets")

        #PLAYER_IMG = 'main_character_sprite_alone_front.png'
        #PLAYER_IMG_UP = 'main_character_sprite_alone_up.png'
        #PLAYER_IMG_RIGHT = 'main_character_sprite_alone_right.png'
        #PLAYER_IMG_LEFT = 'main_character_sprite_alone_left.png'

        #PLAYER_IMG_UP = path.join(img_folder, 'main_character_sprite_alone_up.png')
        #PLAYER_IMG = path.join(img_folder, 'main_character_sprite_alone_front.png')
        #PLAYER_IMG_RIGHT = path.join(img_folder, 'main_character_sprite_alone_right.png')
        #PLAYER_IMG_LEFT = path.join(img_folder, 'main_character_sprite_alone_left.png')



        #player_images = {
            #'Up': pg.image.load(img_folder, 'main_character_sprite_alone_up.png').convert_alpha(),
            #'Right': pg.image.load(img_folder, 'main_character_sprite_alone_right.png').convert_alpha(),
            #'Down': pg.image.load(img_folder, 'main_character_sprite_alone_front.png').convert_alpha(),
            #'Left': pg.image.load(img_folder, 'main_character_sprite_alone_left.png').convert_alpha()
        #}

        #direction = pg.Vector2()

        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            #direction.x -= 1
            #self.image = PLAYER_IMG_LEFT #players_image['Left']
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            #direction.x += 1
            #self.image = PLAYER_IMG_RIGHT #players_image['Right']
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_z]:
            #direction.y -= 1
            #self.image = PLAYER_IMG_UP #players_image['Up']
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_q]:
            #direction.y += 1
            #self.image = PLAYER_IMG #players_image['Down']
            self.vel.y = PLAYER_SPEED

            if self.vel.x != 0 and self.vel.y != 0:
                self.vel *= 0.7071 #0.7071 = 1 / racine carrée de 2

        #if direction != pg.Vector2():
            #self.center = direction * self.vel
            #self.center += direction * self.vel
            #self.rect.center = self.center




    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y



    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.mysprite, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

