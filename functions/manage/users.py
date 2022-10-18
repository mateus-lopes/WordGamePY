import sqlite3

from ..create_id import generate_available_id


def available_account(nickname):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    is_account_available = True
    cursor.execute("SELECT nickname FROM users")
    nicknames = cursor.fetchall()
    for i in nicknames:
        # i[0] get str in tuple(i)
        if i[0] == nickname:
            is_account_available = False
            print("\nUsuário já existente")
    db.close()
    return is_account_available


def create_account(nickname, password):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        command = "SELECT user_id FROM users"
        id = generate_available_id(command)
        points = 0
        cursor.execute(
            "INSERT INTO users VALUES('"
            + str(id)
            + "',"
            + str(points)
            + ",'"
            + nickname
            + "','"
            + password
            + "')"
        )
        db.commit()
        db.close()
    except sqlite3.Error as error:
        print("Error: ", error)


def is_account(nickname, password):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    is_account = False
    cursor.execute("SELECT nickname FROM users WHERE password = '" + password + "'")
    nicknames = cursor.fetchall()
    for i in nicknames:
        # i[0] get str in tuple(i)
        if i[0] == nickname:
            is_account = True
    db.close()
    return is_account


def get_id(nickname):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT user_id FROM users WHERE nickname = '" + nickname + "'")
    id = (cursor.fetchone())[0]
    db.close()
    return id


def show_nickname(id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT nickname FROM users WHERE user_id = '" + str(id) + "'")
    nickname = (cursor.fetchone())[0]
    db.close()
    return nickname


def show_points(id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT points FROM users WHERE user_id = '" + str(id) + "'")
    points = (cursor.fetchone())[0]
    db.close()
    return points


def sum_points(id, value):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        new_value = show_points(id)
        new_value += value
        cursor.execute(
            "UPDATE users SET points = '"
            + str(new_value)
            + "' WHERE user_id = '"
            + str(id)
            + "'"
        )
        db.commit()
        db.close()
    except sqlite3.Error as error:
        print("Error: ", error)


def delete_points(id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        cursor.execute(
            "UPDATE users SET points = '"
            + str(0)
            + "' WHERE user_id = '"
            + str(id)
            + "'"
        )
        db.commit()
        db.close()
    except sqlite3.Error as error:
        print("Error: ", error)


def update_nickname(user_id, nickname):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        cursor.execute(
            "UPDATE users SET nickname = '"
            + nickname
            + "' WHERE user_id = '"
            + str(user_id)
            + "'"
        )
        db.commit()
        db.close()
    except sqlite3.Error as error:
        print("Error: ", error)


def delete_account(id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE user_id == '" + str(id) + "'")
        db.commit()
        db.close
    except sqlite3.Error as error:
        print("Error: ", error)
