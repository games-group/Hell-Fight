import pkgutil
import io

import pygame


def get_cont(name):
    data = pkgutil.get_data(__package__, name)
    if data is None:
        raise PermissionError(name)
    return data


def load(name):
    """portable way of getting a image"""
    file = io.BytesIO(get_cont(name))
    return pygame.image.load(file)
