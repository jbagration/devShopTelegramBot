from aiogram import types, Dispatcher

from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Доброго времени суток! Чем могу помочь?', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\n@sushi_HouseBot')


# @dp.message_handler(commands=['Режим_работы'])
async def sushi_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-чт с 9:00 до 20:00, пт-сб с 10:00 до 23:00')


# @dp.message_handler(commands=['Расположение'])
async def sushi_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Нефтяного, 69')


@dp.message_handler(commands=['Меню'])
async def sushi_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(sushi_place_command, commands=['Расположение'])
    dp.register_message_handler(sushi_open_command, commands=['Режим_работы'])
    dp.register_message_handler(sushi_menu_command, commands=['Меню'])
