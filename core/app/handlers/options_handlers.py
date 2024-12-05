from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from core.app.options.add_task_option_2 import add_task_option_2, add_task_option_2_state
from core.app.options.edit_task_option_3 import edit_task_option_3, edit_task_option_3_state
from core.app.options.remove_task_option_4 import remove_task_option_4, remove_task_option_4_state
from core.app.options.watch_task_option_1 import watch_task_option_1, watch_task_option_1_state
from core.app.states.states import Option

option_router = Router()
value_list = ['1','2','3','4','5']


@option_router.message(lambda message: message.text in value_list)
async def option_h(msg: Message, state: FSMContext):
    await [watch_task_option_1, add_task_option_2, edit_task_option_3, remove_task_option_4][int(msg.text) - 1](msg, state)


@option_router.message(Option.number_option)
async def use_option_h(msg: Message, state: FSMContext):
    index = msg.text
    await [watch_task_option_1_state, add_task_option_2_state, edit_task_option_3_state, remove_task_option_4_state][int(index.split(';')[0]) - 1](msg, state)
