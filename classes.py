import pygame

import utils

import locals


class Game(utils.classes.Root):
    def __init__(self):
        super().__init__()
        self.win = pygame.display.set_mode(locals.SIZE)

    def rewind(self):
        self.__init__()

    def run(self):
        while True:
            self.update()

    def update(self):
        pass

    @staticmethod
    def stop():
        pygame.quit()
