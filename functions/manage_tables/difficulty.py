import sqlite3

from ..randomic_id import generate_available_id

# difficulty

# def create_difficulty():
#     print("cria dificuldade")

# def delete_difficulty():
#     print("apaga dificuldade")


def show_diff():
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT position, diff FROM difficulty")
    difficulties = []
    for i in cursor.fetchall():
        difficulties.append(i)
    return difficulties


def set_difficulty(word):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()

    cursor.execute("SELECT max_letter, position FROM difficulty")
    diff_compiled = cursor.fetchall()
    # append max len 0, for compare max and min letter in iterator

    max_letters = [0]
    for i in diff_compiled:
        max_letters.append(i[0])
    positions = []
    for i in diff_compiled:
        positions.append(i[1])

    c = 0
    while c < len(max_letters):
        # create a second iterator for compare the max letter
        if c != len(max_letters):
            c2 = c + 1
        if len(word) > max_letters[c] and len(word) <= max_letters[c2]:
            return positions[c]
        c += 1


def get_diff_id(word):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()

    diff_pos = set_difficulty(word)

    cursor.execute(
        "SELECT diff_id from difficulty WHERE position = '" + str(diff_pos) + "'"
    )
    diff_id = cursor.fetchone()[0]

    return diff_id


def get_diff_id_by_pos(position):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()

    cursor.execute(
        "SELECT diff_id from difficulty WHERE position = '" + str(position) + "'"
    )
    diff_id = cursor.fetchone()[0]
    return diff_id
