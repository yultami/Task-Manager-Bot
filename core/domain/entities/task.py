from dataclasses import dataclass

from core.domain.entities.base import BaseEntity


@dataclass
class Task(BaseEntity):
    title: str
    description: str
    category: str
    due_date: str
    priority: str
    status: str
    user_id: int

    def convert_task_to_message_view(self):
        return f'\n\nID:{self.id}\nЗаголовок:{self.title}\nОписание:{self.description}\nКатегория:{self.category}\nСрок выполнения:{self.due_date}\nПриоритет:{self.priority}\nСтатус:{self.status}'
