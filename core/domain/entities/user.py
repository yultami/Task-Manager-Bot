from dataclasses import dataclass

from core.domain.entities.base import BaseEntity


@dataclass
class User(BaseEntity):
    username: str
    phone_numb: str