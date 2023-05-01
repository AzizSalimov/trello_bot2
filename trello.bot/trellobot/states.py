from telebot.handler_backends import StatesGroup, State
from telebot.storage.memory_storage import StateMemoryStorage

class CreateNewTask(StateMemoryStorage):
    board = State()
    list = State()
    name = State()
    description = State()
    members = State()
    labers = State()
    date = State()