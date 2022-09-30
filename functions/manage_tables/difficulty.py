import sqlite3

from ..create_id import generate_available_id

# difficulty

# def create_difficulty():
#     print("cria dificuldade")

# def update_difficulty():
#     print("apaga dificuldade")


def show_diff():
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT diff_id, diff FROM difficulty")
    difficulties = []
    for i in cursor.fetchall():
        difficulties.append(i)
    return difficulties


def get_diff_id(word):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()

    cursor.execute("SELECT max_letter, diff_id FROM difficulty")
    diff_compiled = cursor.fetchall()
    # append max len 0, for compare max and min letter in iterator

    max_letters = [0]
    for i in diff_compiled:
        max_letters.append(i[0])
    diff_id = []
    for i in diff_compiled:
        diff_id.append(i[1])

    c = 0
    while c < len(max_letters):
        # create a second iterator for compare the max letter
        if c != len(max_letters):
            c2 = c + 1
        if len(word) > max_letters[c] and len(word) <= max_letters[c2]:
            return diff_id[c]
        c += 1
