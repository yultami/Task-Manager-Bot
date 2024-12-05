from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from punq import Container

from core.app.states.states import Option
from core.logic.commands.task_manager_commands import GetTasksCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


async def watch_task_option_1(msg: Message, state: FSMContext):
    await msg.answer('<b>Введите разделяя ";" :\n • цифру 1,\n • категорию задачи или слово "весь список" для просмотра всех задач</b>', parse_mode="HTML")
    await state.set_state(Option.number_option)


async def watch_task_option_1_state(msg: Message, state: FSMContext):
    await state.update_data(number_option=msg.text)
    await state.clear()
    text = msg.text
    msg_list = text.split(';')
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    tasks = mediator.handle_command(GetTasksCommand(int(msg.from_user.id), msg_list[1] if msg_list[1] != "весь список" else None))
    await msg.answer(f"Список ваших задач:\n{''.join(tasks)}") if tasks != [[]] else await msg.answer("У вас ещё нет добавленных задач!")