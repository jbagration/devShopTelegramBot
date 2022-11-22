from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# кнопки клавиатуры администратора

button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)