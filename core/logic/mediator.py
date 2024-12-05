from collections import defaultdict
from dataclasses import dataclass, field
from typing import Type, Iterable

from core.logic.commands.base import CT, BaseCommandHandler, CR, BaseCommand


@dataclass(eq=False)
class Mediator:
    command_map: dict[Type[CT], list[BaseCommandHandler[CT, CR]]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    def register_command(self, command: Type[CT], command_handlers: Iterable[BaseCommandHandler[CT, CR]]) -> None:

        self.command_map[command].extend(command_handlers)

    def handle_command(self, command: BaseCommand) -> Iterable[CR]:

        command_type = command.__class__
        handlers = self.command_map.get(command_type)

        return [handler.handle(command) for handler in handlers]