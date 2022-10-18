import sqlite3

# from ..create_id import last_id

# def create_difficulty():
#     print("cria dificuldade")

# def update_difficulty():
#     print("atualiza nome da dificuldade")


def show_diff():
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT diff_id, diff, max_letter FROM difficulty")
    difficulties = [i for i in cursor.fetchall()]
    db.close()
    return difficulties


def get_diff_id(word):
    diff_compiled = show_diff()

    for i in diff_compiled:
        diff_id = i[0]
        max_letter = i[2]

        if len(word) <= max_letter:
            return diff_id

    # return [i[0] for i in diff_compiled if len(word) <= i[2]]
