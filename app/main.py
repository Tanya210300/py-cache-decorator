from typing import Callable


def cache(func) -> Callable:
    trash = {}
    def inner(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in trash:
            print("Getting from cache")
            return trash[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            trash[key] = res
            return res
    return inner