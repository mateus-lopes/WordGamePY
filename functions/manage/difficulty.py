import sqlite3

from ..create_id import last_id


def create_difficulty(max_letter, input_diff):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    diff = input_diff.capitalize()
    try:
        select_diff = "SELECT diff FROM difficulty"
        id = last_id(select_diff) + 1

        cursor.execute(
            "INSERT INTO difficulty VALUES('"
            + str(id)
            + "', '"
            + str(max_letter)
            + "','"
            + diff
            + "')"
        )
        db.commit()
        db.close()
    except sqlite3.Error as error:
        print("Error: ", error)


def update_difficulty(diff_id, max_letter, new_name):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    diff = new_name.capitalize()
    try:
        cursor.execute(
            "UPDATE difficulty SET diff = '"
            + diff
            + "' WHERE diff_id = '"
            + str(diff_id)
            + "'"
        )
        cursor.execute(
            "UPDATE difficulty SET max_letter = '"
            + str(max_letter)
            + "' WHERE diff_id = '"
            + str(diff_id)
            + "'"
        )
        db.commit()
        db.close()
    except sqlite3.Error as error:
        print("Error: ", error)


def show_diff():
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT diff_id, diff, max_letter FROM difficulty")
    difficulties = [i for i in cursor.fetchall()]
    db.close()
    return difficulties


def get_diff_id(word):
    diff_compiled = show_diff()
    # i[0]; diff_id
    # i[2]; max_letter
    return [i[0] for i in diff_compiled if len(word) <= i[2]][0]


def delete_diff(diff_id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM difficulty WHERE diff_id = '" + str(diff_id) + "'")
        cursor.execute("DELETE FROM words WHERE diff_id = '" + str(diff_id) + "'")
        db.commit()
        db.close()
    except sqlite3.Error as error:
        print("Error: ", error)
