from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Начать')
kb.add(button1)
kb.add(button2)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет', reply_markup=kb)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Информация о боте!')


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start.')


executor.start_polling(dp, skip_updates=True)
