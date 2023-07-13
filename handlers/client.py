from aiogram import types, Dispatcher
from create_bot import *
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Смачного!!!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Спілкування з ботом через ЛП, напишить йому:\nhttps://t.me/Pizza_chiefgofBot')

#@dp.message_handler(commands=['Режим_роботи'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт з 9:00 до 20:00, Сб-Нд з 11:00 до 19:00')

#@dp.message_handler(commands=['Розташування'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'вул. Пекарська 32', reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_роботи'])
    dp.register_message_handler(pizza_place_command, commands=['Розташування'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])