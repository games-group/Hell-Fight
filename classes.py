import pygame

import utils

import locals


class Mouse:
    def __init__(self):
        self.pos = (0, 0)
        self.down = False


class _EventHandler:
    def __init__(self):
        self.keys = {}
        self.mouse = Mouse()

    def rewind(self):
        self.keys.clear()

    def update(self):
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                self.keys[i.key] = True
            elif i.type == pygame.KEYUP and i.type in self.keys:
                del self.keys[i.key]
            elif i.type == pygame.MOUSEBUTTONDOWN:
                self.mouse.pos = i.pos
                self.mouse.down = True
            elif i.type == pygame.MOUSEBUTTONUP:
                self.mouse.pos = i.pos
                self.mouse.down = False
            elif i.type == pygame.MOUSEMOTION:
                self.mouse.pos = i.pos
            else:
                pygame.event.post(i)


class Game(utils.classes.Root):
    def __init__(self):
        super().__init__()
        self.win = pygame.display.set_mode(locals.SIZE)
        self.handler = _EventHandler()
        self.players = [Player()]

    def rewind(self):
        self.__init__()

    def run(self):
        while True:
            self.update()

    def update(self):
        self.handler.update()
        keys = self.handler.keys[:]
        for i in self.players:
            i.update(keys)

    @staticmethod
    def stop():
        pygame.quit()


class Player(utils,classes.Root):
    X = slice(1)
    Y = slice(2)

    def __init__(self):
        self.mode = ""
        self.map = []  # Empty Empty Empty Empty Empty
        self.player = []  # Empty Empty Empty Empty Empty
        self.player.append(["Player", 18000, 12000, None, None])
        self.player.append(["Zombie", 17820, 11820, "Zombie", 120])
        self.walking = False
        self.walk = 1
        self.change = 0
        self.change2 = 7
        self.move_speed = 6

    def update(self,key):
        if self.change > self.change2:
            self.walking = False
            if pygame.K_w in keys:
                self.mode = "Up"
                self.player[0][self.Y] -= self.move_speed
                self.change = 0
                self.walking = True
            elif pygame.K_s in keys:
                self.mode = "Down"
                self.player[0][self.Y] += self.move_speed
                self.change = 0
                self.walking = True

            if pygame.K_a in keys:
                self.mode = "Left"
                self.player[0][self.X] -= self.move_speed
                self.change = 0
                self.walking = True
            elif pygame.K_d in keys:
                self.mode = "Right"
                self.player[0][self.X] += self.move_speed
                self.change = 0
                self.walking = True
        self.change += 1
