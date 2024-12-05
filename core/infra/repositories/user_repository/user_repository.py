import sqlite3

from core.domain.entities.user import User
from core.infra.repositories.user_repository.base import BaseUserRepository


class UserRepository(BaseUserRepository):
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

    def add_user(self, user: User) -> None:
        user_data = (user.id, user.username, user.phone_numb)

        self.cursor.execute(
            """
            INSERT INTO users (id, username, phone_numb) VALUES (?, ?, ?)
            """,
            user_data
        )
        self.connection.commit()

    def get_user_by_id(self, id: int) -> User:
        self.cursor.execute(
            """
            SELECT * FROM users WHERE id=?
            """,
            [id]
        )
        id, username, phone_numb = self.cursor.fetchone()
        user = User(id=id, username=username, phone_numb=phone_numb)
        return user