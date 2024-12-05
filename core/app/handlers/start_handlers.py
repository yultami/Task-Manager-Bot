from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from punq import Container

from core.app.states.states import Authorization
from core.logic.commands.user_commands import AddUserCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator

start_router = Router()


@start_router.message(Command("start"))
async def start_h(msg: Message, state: FSMContext):
    await msg.answer('\nДобро пожаловать в Менеджер задач!\n\nТы сможешь:\n • просматривать задачи,\n • добавлять задачи,\
                     \n • менять задачи,\n • удалять задачи из списка\
                     \n\nВведите свой номер и имя для регистрации через пробел (Для входа в свою учетную запись введите "вход")')
    await state.set_state(Authorization.authorization_user_data)


@start_router.message(Authorization.authorization_user_data)
async def authorization_h(msg: Message, state: FSMContext):
    await state.update_data(authorization_user_data=msg.text)
    await state.clear()

    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    if msg.text != 'вход':
        mediator.handle_command(AddUserCommand(
            id=int(msg.from_user.id), username=msg.text.split()[1], phone_numb=msg.text.split()[0]
        ))
        await msg.reply("Регистрация прошла успешно! Теперь вы можете использовать Менеджер задач!\
                    \nВыберите нужную опцию по цифре:\n\n<b>1</b> - Просмотр задач\n<b>2</b> - Добавление задачи\
                    \n<b>3</b> - Изменение задачи\n<b>4</b> - Удаление задачи\n<b>5</b> - Поиск задачи\n", parse_mode="HTML")
    else:
        await msg.reply("Вы вошли в систему! \nВыберите нужную опцию по цифре:\n\n<b>1</b> - Просмотр задач\n<b>2</b> - Добавление задачи\
                    \n<b>3</b> - Изменение задачи\n<b>4</b> - Удаление задачи\n<b>5</b> - Поиск задачи\n", parse_mode="HTML")


