from dataclasses import dataclass

from core.domain.entities.task import Task
from core.infra.filters.task_filter import TaskFilter
from core.infra.repositories.task_manager_repository.base import BaseTaskManagerRepository
from core.logic.commands.base import BaseCommand, BaseCommandHandler


@dataclass(frozen=True)
class GetTasksCommand(BaseCommand):
    user_id: int
    category: str | None


@dataclass(frozen=True)
class AddTaskCommand(BaseCommand):
    title: str
    description: str
    category: str
    due_date: str
    priority: str
    status: str
    user_id: int


@dataclass(frozen=True)
class EditTaskCommand(BaseCommand):
    id: int
    kwargs: dict | None


@dataclass(frozen=True)
class DeleteTaskCommand(BaseCommand):
    id: int
    user_id: int


@dataclass(frozen=True)
class GetTasksCommandHandler(BaseCommandHandler[GetTasksCommand, str]):
    task_manager_repository: BaseTaskManagerRepository

    def handle(self, command: GetTasksCommand) -> str:
        task_filter = TaskFilter(
            category=command.category
        )
        return self.task_manager_repository.get_tasks(command.user_id, task_filter)


@dataclass(frozen=True)
class AddTaskCommandHandler(BaseCommandHandler[AddTaskCommand, None]):
    task_manager_repository: BaseTaskManagerRepository

    def handle(self, command: AddTaskCommand) -> None:
        task = Task(
            id=0,
            title=command.title,
            description=command.description,
            category=command.category,
            due_date=command.due_date,
            priority=command.priority,
            status=command.status,
            user_id=command.user_id
        )
        return self.task_manager_repository.add_task(task)


@dataclass(frozen=True)
class EditTaskCommandHandler(BaseCommandHandler[EditTaskCommand, None]):
    task_manager_repository: BaseTaskManagerRepository

    def handle(self, command: EditTaskCommand) -> None:
        print(command.id, command.kwargs)
        return self.task_manager_repository.edit_task(command.id, **command.kwargs)


@dataclass(frozen=True)
class DeleteTaskCommandHandler(BaseCommandHandler[DeleteTaskCommand, None]):
    task_manager_repository: BaseTaskManagerRepository

    def handle(self, command: DeleteTaskCommand) -> None:
        return self.task_manager_repository.del_task(command.id, command.user_id)

