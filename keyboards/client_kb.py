from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_роботи')
b2 = KeyboardButton('/Розташування')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('Поділитись номерои', request_contact=True)
b5 = KeyboardButton('Відправити де я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3).row(b4, b5)