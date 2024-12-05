from abc import ABC, abstractmethod

from core.domain.entities.user import User


class BaseUserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User) -> None:
        ...

    @abstractmethod
    def get_user_by_id(self, id: int) -> User:
        ...