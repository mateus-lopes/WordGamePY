import sqlite3
from functions.connect_db import Connect


class Topic:
    def __init__(self):
        self.db = Connect()

    def start(self):
        try:
            with open("functions/manage/sql/topics_schema.sql", "rt") as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            return False

    def show_topics(self):
        select = self.db.cursor.execute("SELECT id, topic FROM topics")
        topics = [i for i in select.fetchall()]
        return topics

    def is_new_topic(self, topic):
        is_new_topic = True
        all_topics = self.show_topics()
        topics = [(topic[1]) for topic in all_topics]
        for i in topics:
            if topic == i:
                is_new_topic = False
        return is_new_topic

    def topic_exists(self, topic_id):
        print(topic_id)
        select = self.db.cursor.execute(
            "SELECT topic FROM topics WHERE id = ?", ((topic_id,))
        )
        selected = select.fetchone()
        return True if selected else False

    def topic_is_alpha(self, input_topic):
        topic_is_alpha = True
        for i in input_topic:
            if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                topic_is_alpha = False
                break
        return topic_is_alpha

    def create_topic(self, topic):
        try:
            is_alpha = self.topic_is_alpha(topic)
            if is_alpha:
                self.db.cursor.execute(
                    "INSERT INTO topics (topic) VALUES (?)", ((topic,))
                )
                self.db.commit_db()
                topic_id = self.get_id(topic)
                return topic_id
            else:
                print("Erro: Números não são aceitos")
                return False
        except sqlite3.Error:
            print("Erro: Tópico já existe")

    def get_id(self, topic):
        select = self.db.cursor.execute(
            "SELECT id FROM topics WHERE topic = ?", ((topic,))
        )
        selected = select.fetchone()
        topic_id = selected[0] if selected else selected
        return topic_id

    def use_topic(self, id):
        select = self.db.cursor.execute(
            "SELECT topic FROM topics WHERE id = {}".format(id)
        )
        topic = select.fetchone()
        return topic[0] if topic else topic

    def delete_topic(self, id):
        try:
            cursor = self.db.cursor
            cursor.execute("DELETE FROM topics WHERE id = {}".format(id))
            cursor.execute("DELETE FROM words WHERE topic_id = {}".format(id))
            self.db.commit_db()
        except sqlite3.Error as error:
            print("Error: ", error)

    def drop_table(self):
        self.db.cursor.execute("DROP TABLE topics")

    def close_db(self):
        self.db.close_db()
