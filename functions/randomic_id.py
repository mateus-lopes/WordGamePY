import random


def randomic_id():
    id = ["1", "a", "3", "b", "5", "c", "7", "d", "9"]
    random.shuffle(id)
    return "".join(id)
