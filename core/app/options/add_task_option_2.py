from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from punq import Container

from core.app.states.states import Option
from core.logic.commands.task_manager_commands import AddTaskCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


async def add_task_option_2(msg: Message, state: FSMContext):
    await msg.answer('<b>Введите разделяя на ";" :\n • цифру 2,\n • название задачи,\n • описание задачи,\n • категорию задачи,\n • срок выполнения (YYYY-MM-DD),\n • приоритет (низкий, средний, высокий)</b>', parse_mode="HTML")
    await state.set_state(Option.number_option)


async def add_task_option_2_state(msg: Message, state: FSMContext):
    await state.update_data(number_option=msg.text)
    await state.clear()
    text = msg.text
    msg_list = text.split(';')
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    mediator.handle_command(AddTaskCommand(
        title=msg_list[1],
        description=msg_list[2],
        category=msg_list[3],
        due_date=msg_list[4],
        priority=msg_list[5],
        status='Не выполнена',
        user_id=msg.from_user.id
    ))
    await msg.reply("Задача добавлена в список!")