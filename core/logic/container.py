from functools import lru_cache

from aiogram import Bot, Dispatcher
from punq import Container, Scope

from core.infra.repositories.task_manager_repository.base import BaseTaskManagerRepository
from core.infra.repositories.task_manager_repository.task_manager_repository import TaskManagerRepository
from core.infra.repositories.user_repository.base import BaseUserRepository
from core.infra.repositories.user_repository.user_repository import UserRepository
from core.logic.commands.task_manager_commands import GetTasksCommandHandler, AddTaskCommandHandler, \
    EditTaskCommandHandler, DeleteTaskCommandHandler, GetTasksCommand, AddTaskCommand, EditTaskCommand, \
    DeleteTaskCommand
from core.logic.commands.user_commands import AddUserCommandHandler, GetUserByIdCommandHandler, AddUserCommand, \
    GetUserByIdCommand
from core.logic.mediator import Mediator
from core.settings.config import Settings


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(AddUserCommandHandler)
    container.register(GetUserByIdCommandHandler)
    container.register(GetTasksCommandHandler)
    container.register(AddTaskCommandHandler)
    container.register(EditTaskCommandHandler)
    container.register(DeleteTaskCommandHandler)
    container.register(Settings, scope=Scope.singleton)

    def init_bot() -> Bot:
        settings = container.resolve(Settings)
        bot = Bot(token=settings.TOKEN)
        return bot

    def init_dispatcher() -> Dispatcher:
        dp = Dispatcher()
        return dp

    def init_user_repository() -> BaseUserRepository:
        return UserRepository()

    def init_task_manager_repository() -> BaseTaskManagerRepository:
        return TaskManagerRepository()

    def init_mediator() -> Mediator:
        mediator = Mediator()

        mediator.register_command(AddUserCommand, [container.resolve(AddUserCommandHandler)])
        mediator.register_command(GetUserByIdCommand, [container.resolve(GetUserByIdCommandHandler)])
        mediator.register_command(GetTasksCommand, [container.resolve(GetTasksCommandHandler)])
        mediator.register_command(AddTaskCommand, [container.resolve(AddTaskCommandHandler)])
        mediator.register_command(EditTaskCommand, [container.resolve(EditTaskCommandHandler)])
        mediator.register_command(DeleteTaskCommand, [container.resolve(DeleteTaskCommandHandler)])

        return mediator

    container.register(Bot, factory=init_bot, scope=Scope.singleton)
    container.register(Dispatcher, factory=init_dispatcher, scope=Scope.singleton)

    container.register(BaseUserRepository, factory=init_user_repository, scope=Scope.singleton)
    container.register(BaseTaskManagerRepository, factory=init_task_manager_repository, scope=Scope.singleton)

    container.register(Mediator, factory=init_mediator, scope=Scope.singleton)

    return container
