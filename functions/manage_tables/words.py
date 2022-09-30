import sqlite3

from functions.manage_tables import topics as tp
from functions.manage_tables import difficulty as df

from ..create_id import last_id


# words


def add_word(input_word, input_topic):
    input_word = input_word.capitalize()
    input_topic = input_topic.capitalize()
    if len(input_word) > 15:
        print("palavra inválida")
    else:
        if tp.is_new_topic(input_topic):
            topic_id = tp.create_topic(input_topic)
        else:
            topic_id = tp.use_topic(input_topic)

        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()

        select_word = "SELECT word FROM words"
        id = last_id(select_word)

        diff_id = df.get_diff_id(input_word)

        cursor.execute(
            "INSERT INTO words VALUES('"
            + str(id + 1)
            + "',"
            + str(topic_id)
            + ",'"
            + str(diff_id)
            + "','"
            + input_word
            + "')"
        )

        db.commit()
        db.close()


def get_word_filtered(topic_id, diff_id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute(
        "SELECT diff_id, word FROM words WHERE topic_id = '" + str(topic_id) + "'"
    )
    words = []
    for i in cursor.fetchall():
        if i[0] == diff_id:
            words.append(i[1])
    return words


def get_all_words():
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM words")
    words = []
    for i in cursor.fetchall():
        words.append(i)
    return words
