from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from BD import db_start, create_prof, edit_prof
from keyButton import one_start_kb
async def on_startup(_):
    await db_start()

bot = Bot(token="6482847859:AAGPRNrL_m1tnXhHq-M4oIw8qNXMkEGhshs")
dp = Dispatcher(bot)

Family = 'Нету'
Status = 'Игрок'
Levle = 1
Balans = 0
Exp = 0
SIM = 'нету'
Phone = 'нету'

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Добро пожаловать на проект",
                         reply_markup=one_start_kb)
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://sun9-25.userapi.com/impg/rztqa5JudhELhD0CQ7uhwm9jYkLf5cYRuCm3sw/UXPcCkldjjA.jpg?size=1600x740&quality=96&sign=f040797e44f6465104cf118c43bea1eb&type=album',)
    await create_prof(user_id=message.from_user.id)

@dp.message_handler(commands=['Профиль'])
async def greet(message: types.Message):
    await message.answer(text=f'Вас зовут: \n'
                              f'Ваш id: \n'
                              f'Семья: \n'
                              f'Статус: \n'
                              f'Уровень: \n'
                              f'Опыт: \n'
                              f'Баланы: \n'
                              f'SIM: \n'
                              f'Телевон: \n')

if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)