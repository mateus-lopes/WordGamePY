import sqlite3
from functions import randomic_id as ri


def available_account(nickname):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        is_account_available = True
        cursor.execute("SELECT nickname FROM users")
        nicknames = cursor.fetchall()
        for i in nicknames:
            # i[0] for catching the str in tuple(i)
            if i[0] == nickname:
                is_account_available = False
                print("\nUsuário já existente")
        return is_account_available
    except sqlite3.Error as error:
        print("Error: ", error)


def create_account(nickname, password):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        id = ri.randomic_id()
        is_id_available = compare_id_account(id)
        while is_id_available == False:
            id = ri.randomic_id()
            is_id_available = compare_id_account(id)
        points = 0
        cursor.execute(
            "INSERT INTO users VALUES('"
            + id
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


def login(nickname, password):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        is_account = False
        cursor.execute("SELECT nickname FROM users WHERE password = '" + password + "'")
        nicknames = cursor.fetchall()
        for i in nicknames:
            # i[0] for catching the str in tuple(i)
            if i[0] == nickname:
                is_account = True
        return is_account
    except sqlite3.Error as error:
        print("Error: ", error)


def compare_id_account(id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    is_id_available = True
    cursor.execute("SELECT id FROM users")
    all_id = cursor.fetchall()
    for i in all_id:
        if i[0] == id:
            is_id_available = False
    return is_id_available


def get_id(nickname):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT id FROM users WHERE nickname = '" + nickname + "'")
    id = (cursor.fetchone())[0]
    return id


def show_nickname(id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT nickname FROM users WHERE id = '" + id + "'")
    nickname = (cursor.fetchone())[0]
    return nickname


def show_points(id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT points FROM users WHERE id = '" + id + "'")
    points = (cursor.fetchone())[0]
    return points


def sum_points(id, value):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    try:
        new_value = show_points(id)
        new_value += value
        cursor.execute(
            "UPDATE users SET points = '" + str(new_value) + "' WHERE id = '" + id + "'"
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
            "UPDATE users SET points = '" + str(0) + "' WHERE id = '" + id + "'"
        )
        db.commit()
        db.close()
    except sqlite3.Error as error:
        print("Error: ", error)


# def update_nickname():
#     print("mudando nickname")


def delete_account(id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("DELETE from users WHERE id == '" + id + "'")
    db.commit()


# cursor.execute("DELETE from users")
# db.commit()
