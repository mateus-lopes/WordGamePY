import sqlite3

from random import shuffle


def randomic_id():
    id = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    shuffle(id)
    return int("".join(id))


def compare_id(id, command):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    is_id_available = True
    cursor.execute(command)
    all_id = cursor.fetchall()
    for i in all_id:
        if i[0] == id:
            is_id_available = False
    return is_id_available


def last_id(command):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute(command)
    n_properties = cursor.fetchall()
    my_last_id = len(n_properties)
    return my_last_id


def generate_available_id(command):
    while True:
        id = randomic_id()
        is_id_available = compare_id(id, command)
        if is_id_available:
            break
    return id
