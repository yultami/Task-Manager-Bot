from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from punq import Container

from core.app.states.states import Option
from core.logic.commands.task_manager_commands import DeleteTaskCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


async def remove_task_option_4(msg: Message, state: FSMContext):
    await msg.answer('<b>Введите Введите разделяя на ";" :\n • цифру 4,\n • ID задачи, которую хотите удалить</b>', parse_mode="HTML")
    await state.set_state(Option.number_option)


async def remove_task_option_4_state(msg: Message, state: FSMContext):
    await state.update_data(number_option=msg.text)
    await state.clear()
    text = msg.text
    msg_list = text.split(';')
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    mediator.handle_command(DeleteTaskCommand(int(msg_list[1]), int(msg.from_user.id)))
    await msg.reply("Задача была успешно удалена!")