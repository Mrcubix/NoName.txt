import pygame as pg
import random
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

# assets folders
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "assets")

class Game:
    def __init__(self): #init game windows
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(300, 100)
        self.running = True
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        #self.map = Map(path.join(game_folder, 'temp_map.txt'))
        img_folder = path.join(game_folder, "assets")
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'forest_map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.player_img_up = pg.image.load(path.join(img_folder, PLAYER_IMG_UP)).convert_alpha()
        self.player_img_right = pg.image.load(path.join(img_folder, PLAYER_IMG_RIGHT)).convert_alpha()
        self.player_img_left = pg.image.load(path.join(img_folder, PLAYER_IMG_LEFT)).convert_alpha()


    def new(self):
        self.mysprite = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        #for row, tiles in enumerate(self.map.data):
        #    for col, tile in enumerate(tiles):
        #        if tile == '1':
        #            Wall(self, col, row)
        #        if tile == 'P':
        #            self.player = Player(self, col, row)
        self.player = player(self, 5, 5)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self): #Thread
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.mysprite.update()
        self.camera.update(self.player)

    def quit(self):
        pg.quit()
        sys.exit()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False


    def draw_grid(self):
        for x in range (0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LG, (x, 0), (x, HEIGHT))
        for y in range (0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LG, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        #self.screen.fill(BG)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        #self.draw_grid()
        for sprite in self.mysprite:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# initialise pg et setup de la fenêtre

g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()