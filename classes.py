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
