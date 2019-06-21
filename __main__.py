# __main__.py
# caller of all mods
import classes


def main():
    game = classes.Game()
    while game.run():
        game.rewind()
    game.stop()
    return game


if __name__ == "__main__":
    main()
