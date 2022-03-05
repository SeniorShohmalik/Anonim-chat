from aiogram.dispatcher.filters.state import StatesGroup, State

class Translate(StatesGroup):
    tekst=State()
    id=State()
    NONE=State()

    