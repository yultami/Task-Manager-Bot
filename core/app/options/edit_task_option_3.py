from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from punq import Container

from core.app.states.states import Option
from core.logic.commands.task_manager_commands import EditTaskCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


async def edit_task_option_3(msg: Message, state: FSMContext):
    await msg.answer('<b>Введите разделяя на ";" :\n • цифру 3,\n • ID задачи,\n • новое название /"п" - пропустить,\n • новое описание /"п" - пропустить,\n • новая категория /"п" - пропустить,\n • новый срок выполнения (YYYY-MM-DD) /"п" - пропустить,\n • новый приоритет /"п" - пропустить,\n • новый статус /"п" - пропустить</b>', parse_mode="HTML")
    await state.set_state(Option.number_option)


async def edit_task_option_3_state(msg: Message, state: FSMContext):
    await state.update_data(number_option=msg.text)
    await state.clear()
    text = msg.text
    msg_list = text.split(';')
    kwargs = {}

    kwargs.update({'title': msg_list[2]}) if msg_list[2] != 'п' else kwargs
    kwargs.update({'description': msg_list[3]}) if msg_list[3] != 'п' else kwargs
    kwargs.update({'category': msg_list[4]}) if msg_list[4] != 'п' else kwargs
    kwargs.update({'due_date': msg_list[5]}) if msg_list[5] != 'п' else kwargs
    kwargs.update({'priority': msg_list[6]}) if msg_list[6] != 'п' else kwargs
    kwargs.update({'status': msg_list[7]}) if msg_list[7] != 'п' else kwargs

    container: Container= init_container()
    mediator: Mediator = container.resolve(Mediator)
    mediator.handle_command(EditTaskCommand(id=int(msg_list[1]), kwargs=kwargs))
    await msg.reply("Задача отредактирована!")
