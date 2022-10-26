import sqlite3


class Connect:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("db.sqlite3")
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print("Error:", error)

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
