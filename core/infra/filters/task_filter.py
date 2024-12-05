from dataclasses import dataclass


@dataclass(frozen=True)
class TaskFilter:
    category: str | None