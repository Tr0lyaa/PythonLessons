from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Информация', callback_data='info')
kb.add(button1)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='info')],
        [KeyboardButton(text='shop'),
         KeyboardButton(text='Рассчитать')]

    ], resize_keyboard=True
)


class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=start_menu)


@dp.callback_query_handler(text='info')
async def info(call):
    await call.message.answer("Информация о боте")
    await call.answer


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserStates.age.set()


@dp.message_handler(state=UserStates.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост')
    await UserStates.growth.set()


@dp.message_handler(state=UserStates.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес')
    await UserStates.weight.set()


@dp.message_handler(state=UserStates.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    await message.answer(f'Результат: {10*data["weight"]+6.25*data["growth"]-5*data["age"]+5}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите слово /start для расчета калорий '
                         'для оптимального похудения или сохранения нормального веса.')


executor.start_polling(dp, skip_updates=True)
