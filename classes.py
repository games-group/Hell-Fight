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
