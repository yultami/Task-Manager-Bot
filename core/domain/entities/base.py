from abc import ABC
from dataclasses import dataclass


@dataclass(eq=False)
class BaseEntity(ABC):
    id: int