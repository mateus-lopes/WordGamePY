import numbers
import sqlite3

from functions.connect_db import Connect
from functions.manage.difficulty import Diff
from functions.manage.topics import Topic


class Word:
    def __init__(self):
        self.db = Connect()
        self.df = Diff()
        self.tp = Topic()

    def start(self):
        self.create_schema()

    def create_schema(self):
        try:
            with open("functions/manage/sql/words_schema.sql", "rt") as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            return False

    def format_input(self, input):
        numbers = []
        for i in input:
            if i.isalpha():
                continue
            else:
                numbers.append(i)
        numbers = "".join(numbers)
        return int(numbers)

    def create_word(self, input_topic, word):
        max_letter = self.df.show_diff()[-1][-1]
        if len(word) <= max_letter:
            try:
                is_alpha = self.tp.topic_is_alpha(input_topic)
                if is_alpha:
                    topic_id = (
                        self.tp.create_topic(input_topic, is_alpha)
                        if self.tp.is_new_topic(input_topic)
                        else self.tp.get_id(input_topic)
                    )
                else:
                    input_topic = self.format_input(input_topic)
                    topic_id = (
                        input_topic if self.tp.topic_exists(input_topic) else None
                    )

                if topic_id:
                    pass
                else:
                    print("Erro: Tópico não existe")
                    return False

                diff_id = self.df.get_diff_id(word)

                self.db.cursor.execute(
                    "INSERT INTO words (topic_id,diff_id,word) VALUES (?,?,?)",
                    (topic_id, diff_id, word),
                )
                self.db.commit_db()
            except sqlite3.Error as error:
                print("Error: ", error)
        else:
            print("Erro: Palavra ultrapassa o número de caracteres")

    def get_words(self):
        select = self.db.cursor.execute("SELECT * FROM words")
        words = [i for i in select.fetchall()]
        return words

    def select_topic_diff(self, topic_id, diff_id):
        select = self.db.cursor.execute(
            "SELECT topic_id, diff_id, word FROM words WHERE topic_id = {}".format(
                topic_id
            )
        )
        words = [i for i in select.fetchall() if i[1] == diff_id]
        return words

    def delete_word(self, id):
        try:
            self.db.cursor.execute("DELETE FROM words WHERE id = {}".format(id))
            self.db.commit_db()
        except sqlite3.Error as error:
            print("Error: ", error)

    def drop_table(self):
        self.db.cursor.execute("DROP TABLE words")

    def close_db(self):
        self.db.close_db()
