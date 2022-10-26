import sqlite3

from functions.connect_db import Connect
from functions.hash_password import create_hash, compare_hash


class User:
    def __init__(self):
        self.db = Connect()

    def start(self):
        try:
            with open("functions/manage/sql/users_schema.sql", "rt") as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            return False

    def available_account(self, nickname):
        select = self.db.cursor.execute(
            "SELECT nickname FROM users WHERE nickname = (?)", ((nickname,))
        )
        db_list = select.fetchone()
        is_account_available = False if db_list else True
        None if is_account_available else print("Erro: Usuário já existe")
        return is_account_available

    def create_account(self, nickname, password):
        try:
            hashed_password = create_hash(password)
            points = 0
            self.db.cursor.execute(
                "INSERT INTO users (points, nickname, password) VALUES (?,?,?)",
                (points, nickname, hashed_password),
            )
            self.db.commit_db()
        except sqlite3.Error:
            print("Erro: Usuário já existe")

    def is_account(self, nickname, password):
        select = self.db.cursor.execute(
            "SELECT password FROM users WHERE nickname = (?)", ((nickname,))
        )
        password_account = select.fetchall()
        if password_account == []:
            print("Erro: Conta não encontrada")
            return False
        password_account = password_account[0][0]
        is_account = True if compare_hash(password, password_account) else False
        None if is_account else print("Erro: Senha incorreta")
        return is_account

    def get_id(self, nickname):
        select = self.db.cursor.execute(
            "SELECT id FROM users WHERE nickname = (?)", ((nickname,))
        )
        id = select.fetchone()
        return id[0] if id else "Erro: Usuário não encontrado"

    def show_nickname(self, id):
        select = self.db.cursor.execute(
            "SELECT nickname FROM users WHERE id = (?)", ((id,))
        )
        nickname = select.fetchone()
        return nickname[0] if nickname else "Erro: Usuário não encontrado"

    def update_nickname(self, id, nickname):
        try:
            self.db.cursor.execute(
                "UPDATE users SET nickname = ? WHERE id = ?", (nickname, id)
            )
            self.db.commit_db()
        except sqlite3.Error:
            print("Erro: nickname já está em uso")

    def show_points(self, id):
        select = self.db.cursor.execute(
            "SELECT points FROM users WHERE id = (?)", ((id,))
        )
        points = select.fetchone()
        return points[0] if points else "Erro: Usuário não encontrado"

    def sum_points(self, id, value):
        try:
            new_value = self.show_points(id)
            new_value += value
            self.db.cursor.execute(
                "UPDATE users SET points = ? WHERE id = ?", (new_value, id)
            )
            self.db.commit_db()
        except sqlite3.Error as error:
            print("Error: ", error)

    def delete_points(self, id):
        try:
            self.db.cursor.execute("UPDATE users SET points = ? WHERE id = ?", (0, id))
            self.db.commit_db()
        except sqlite3.Error as error:
            print("Error: ", error)

    def delete_account(self, id):
        try:
            self.db.cursor.execute("DELETE FROM users WHERE id == ?", ((id,)))
            self.db.commit_db()
        except sqlite3.Error as error:
            print("Error: ", error)

    def drop_table(self):
        self.db.cursor.execute("DROP TABLE users")

    def close_db(self):
        self.db.close_db()
