# __main__.py
# caller of module classes
# main script
import classes


def main():
    game = classes.Game()
    while game.run():  # game.run returns True if user has ended a game,or False if a user closed the window
        game.rewind()
        # game.rewind rewinds the game so it can be run again (without it,the game will have bizarre bugs)
    game.stop()
    return game  # for debugging


if __name__ == "__main__":
    main()
