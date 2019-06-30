import pygame

from utils.classes import MyMeta
import locals


# class to make it easy to represent a mouse
class Mouse(metaclass=MyMeta):
    def __init__(self):
        self.pos = (0, 0)
        self.down = False  # short for mouse_button_down


class _EventHandler(metaclass=MyMeta):
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
                # put it back so it can be reused


class Game(metaclass=MyMeta):
    def __init__(self):
        super().__init__()
        self.win = pygame.display.set_mode(locals.SIZE)
        self.handler = _EventHandler()
        self.players = [Player()]

    def rewind(self):
        self.__init__()
        # easy implementation of rewind: re-init self

    def run(self):
        while True:
            self.update()

    def update(self):
        self.handler.update()  # get the newest keys
        keys = self.handler.keys[:]
        for i in self.players:
            i.update(keys)

    @staticmethod
    def stop():
        pygame.quit()


class Player(metaclass=MyMeta):
    PLAYER = slice(0)

    X = slice(1)
    Y = slice(2)
    # syntax sugar

    def __init__(self):
        self.mode = ""
        self.map = []  # Name x y ex1 ex2
        self.player = []  # Name x y ex1 ex2
        self.player.append(["Player", 18000, 12000, None, None])
        self.player.append(["Zombie", 17820, 11820, "Zombie", 120])
        self.walking = False
        self.walk = 1
        self.change = 0
        self.change2 = 7  # how much change has to be before the player moved
        self.move_speed = 6

    def update(self, keys):
        if self.change > self.change2:
            self.walking = False
            if pygame.K_w in keys:
                self.mode = "Up"
                self.player[self.PLAYER][self.Y] -= self.move_speed
                self.change = 0
                self.walking = True
            elif pygame.K_s in keys:
                self.mode = "Down"
                self.player[self.PLAYER][self.Y] += self.move_speed
                self.change = 0
                self.walking = True

            if pygame.K_a in keys:
                self.mode = "Left"
                self.player[self.PLAYER][self.X] -= self.move_speed
                self.change = 0
                self.walking = True
            elif pygame.K_d in keys:
                self.mode = "Right"
                self.player[self.PLAYER][self.X] += self.move_speed
                self.change = 0
                self.walking = True
        self.change += 1
