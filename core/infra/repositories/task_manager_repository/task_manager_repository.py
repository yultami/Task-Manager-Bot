import sqlite3

from core.domain.entities.task import Task
from core.infra.filters.task_filter import TaskFilter
from core.infra.repositories.task_manager_repository.base import BaseTaskManagerRepository


class TaskManagerRepository(BaseTaskManagerRepository):
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

    def get_tasks(self, user_id: int, task_filter: TaskFilter) -> str:
        self.cursor.execute(
            """
            SELECT * FROM tasks WHERE user_id=?
            """,
            [user_id]
        )
        tasks = self.cursor.fetchall()
        if task_filter.category is not None:
            return ''.join([
                f'\n\nID:{field[0]}\nЗаголовок:{field[1]}\nОписание:{field[2]}\nКатегория:{field[3]}\nСрок выполнения:{field[4]}\nПриоритет:{field[5]}\nСтатус:{field[6]}'
                for field in tasks if task_filter.category == field[3]])
        return ''.join([
            f'\n\nID:{field[0]}\nЗаголовок:{field[1]}\nОписание:{field[2]}\nКатегория:{field[3]}\nСрок выполнения:{field[4]}\nПриоритет:{field[5]}\nСтатус:{field[6]}'
            for field in tasks])

    def add_task(self, task: Task) -> None:
        task_data = (task.title, task.description, task.category,
                     task.due_date, task.priority, task.status, task.user_id)
        self.cursor.execute(
            """
            INSERT INTO tasks (title, description, category, due_date, priority, status, user_id) 
            VALUES (?,?,?,?,?,?,?)
            """,
            task_data
        )
        self.connection.commit()

    def edit_task(self, id: int, **kwargs) -> None:
        self.cursor.execute(
            """
            SELECT * FROM tasks WHERE id=?
            """,
            [id]
        )
        id, title, description, category, due_date, priority, status, user_id = self.cursor.fetchone()
        task_data = (
            kwargs.get('title') if kwargs.get('title') is not None else title,
            kwargs.get('description') if kwargs.get('description') is not None else description,
            kwargs.get('category') if kwargs.get('category') is not None else category,
            kwargs.get('due_date') if kwargs.get('due_date') is not None else due_date,
            kwargs.get('priority') if kwargs.get('priority') is not None else priority,
            kwargs.get('status') if kwargs.get('status') is not None else status,
            id
        )
        self.cursor.execute(
            """
            UPDATE tasks
            SET title = ?, description = ?, category = ?, due_date = ?, priority = ?, status = ?
            WHERE id=?
            """,
            task_data
        )
        self.connection.commit()

    def del_task(self, id: int, user_id: int) -> None:
        self.cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ? AND user_id = ?
            """,
            (id, user_id)
        )
        self.connection.commit()