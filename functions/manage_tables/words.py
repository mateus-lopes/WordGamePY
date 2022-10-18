import sqlite3

from functions.manage_tables import topics as tp
from functions.manage_tables import difficulty as df

from ..create_id import last_id


def add_word(input_word, input_topic):
    word = input_word.capitalize()
    topic = input_topic.capitalize()
    max_letter = df.show_diff()[-1][-1]
    if len(word) <= max_letter:
        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()
        try:
            select_word = "SELECT word FROM words"
            id = last_id(select_word) + 1

            topic_id = (
                tp.create_topic(topic)
                if tp.is_new_topic(topic)
                else tp.get_topic_id(topic)
            )
            diff_id = df.get_diff_id(word)

            cursor.execute(
                "INSERT INTO words VALUES('"
                + str(id)
                + "',"
                + str(topic_id)
                + ",'"
                + str(diff_id)
                + "','"
                + word
                + "')"
            )

            db.commit()
            db.close()
        except sqlite3.Error as error:
            print("Error: ", error)
    else:
        print("palavra inválida")


def get_word_filtered(topic_id, diff_id):
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute(
        "SELECT diff_id, word FROM words WHERE topic_id = '" + str(topic_id) + "'"
    )
    words = [i[1] for i in cursor.fetchall() if i[0] == diff_id]
    db.close()
    return words


def get_all_words():
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM words")
    words = [i for i in cursor.fetchall()]
    db.close()
    return words
