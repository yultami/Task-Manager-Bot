from dataclasses import dataclass

from core.domain.entities.user import User
from core.infra.repositories.user_repository.base import BaseUserRepository
from core.logic.commands.base import BaseCommand, BaseCommandHandler


@dataclass(frozen=True)
class AddUserCommand(BaseCommand):
    id: int
    username: str
    phone_numb: str


@dataclass(frozen=True)
class GetUserByIdCommand(BaseCommand):
    id: int


@dataclass(frozen=True)
class AddUserCommandHandler(BaseCommandHandler[AddUserCommand, None]):
    user_repository: BaseUserRepository

    def handle(self, command: AddUserCommand) -> None:
        user = User(
            id=command.id,
            username=command.username,
            phone_numb=command.phone_numb
        )
        return self.user_repository.add_user(user)


@dataclass(frozen=True)
class GetUserByIdCommandHandler(BaseCommandHandler[GetUserByIdCommand, User]):
    user_repository: BaseUserRepository

    def handle(self, command: GetUserByIdCommand) -> User:
        return self.user_repository.get_user_by_id(command.id)