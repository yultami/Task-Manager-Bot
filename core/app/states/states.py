from aiogram.fsm.state import StatesGroup, State


class Authorization(StatesGroup):
    authorization_user_data = State()


class Option(StatesGroup):
    number_option = State()