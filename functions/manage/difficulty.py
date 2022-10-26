import sqlite3
from functions.connect_db import Connect


class Diff:
    def __init__(self):
        self.db = Connect()

    def start(self):
        try:
            with open("functions/manage/sql/difficulty_schema.sql", "rt") as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            return False

    def get_max_letters(self):
        select = self.db.cursor.execute("SELECT max_letter FROM difficulty")
        max_letters = [i[0] for i in select.fetchall()]
        max_letters.sort()
        return max_letters

    def order_max_letters(self):
        """ORDENA TODOS A SEQUENCIA PELOS MAXIMOS DE LETRA"""
        db_list = self.get_max_letters()
        id = [i + 1 for i in range(0, len(db_list))]
        for i in zip(id, db_list):
            self.db.cursor.execute(
                "UPDATE difficulty SET sequence = {} WHERE max_letter = {}".format(
                    i[0], i[1]
                )
            )

    def create_difficulty(self, max_letter, input_diff):
        diff = input_diff.capitalize()
        try:
            self.db.cursor.execute(
                "INSERT INTO difficulty (max_letter, diff, sequence) VALUES (?,?,?)",
                (max_letter, diff, 1),
            )
            self.order_max_letters()
            self.db.commit_db()
        except sqlite3.Error as error:
            print("Erro: Máximo de letras já existe")

    def update_difficulty(self, sequence, new_name):
        diff = new_name.capitalize()
        try:
            self.db.cursor.execute(
                "UPDATE difficulty SET diff = ? WHERE sequence = ?", (diff, sequence)
            )
            self.db.commit_db()
        except sqlite3.Error as error:
            print("Error: ", error)

    def show_diff(self):
        select = self.db.cursor.execute(
            "SELECT sequence, id, diff, max_letter FROM difficulty"
        )
        difficulties = [i for i in select.fetchall()]
        difficulties.sort()
        return difficulties

    def get_diff_id(self, word):
        diff_compiled = self.show_diff()
        # i[1]; id
        # i[2]; max_letter
        return [i[1] for i in diff_compiled if len(word) <= i[-1]][0]

    def delete_diff(self, id):
        try:
            cursor = self.db.cursor
            cursor.execute("DELETE FROM difficulty WHERE id = {}".format(id))
            cursor.execute("DELETE FROM words WHERE diff_id = {}".format(id))
            self.db.commit_db()
        except sqlite3.Error as error:
            print("Error: ", error)

    def close_db(self):
        self.db.close_db()
