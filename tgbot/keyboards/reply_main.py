# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup

from tgbot.data.config import get_admins


# Кнопки главного меню
def menu_frep(user_id):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row("💳 Карты", "Юридические фирмы") # "🧮 Наличие товаров", "👤 Профиль"
    keyboard.row("📮 Служба поддержки", "ℹ О нас") # "☎ Поддержка", "ℹ FAQ"

    if user_id in get_admins():
        keyboard.row("🎁 Управление товарами", "📊 Статистика")
        keyboard.row("⚙ Настройки", "🔆 Общие функции") # "🔑 Платежные системы"

    return keyboard


# Кнопки платежных систем
def payments_frep():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row('В разработке') # "🥝 Изменить QIWI 🖍", "🥝 Проверить QIWI ♻", "🥝 Баланс QIWI 👁"
    keyboard.row("🔙 Главное меню") # "🖲 Способы пополнений"

    return keyboard


# Кнопки общих функций
def functions_frep(user_id):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row("🏦 Реквезиты", "📢 Рассылка", "🧾 Поиск чеков 🔍") #"🧾 Поиск чеков 🔍"
    keyboard.row("🔙 Главное меню")

    return keyboard


# Кнопки настроек
def settings_frep():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row("🖍 Изменить данные", "🕹 Выключатели")
    keyboard.row("🔙 Главное меню")

    return keyboard


# Кнопки изменения товаров
def items_frep():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row("🎁 Добавить товары ➕", "🎁 Удалить все товары ❌")
    keyboard.row("📁 Создать позицию ➕", "📁 Изменить позицию 🖍", "📁 Удалить все позиции ❌")
    keyboard.row("🗃 Создать категорию ➕", "🗃 Изменить категорию 🖍", "🗃 Удалить все категории ❌")
    keyboard.row("🔙 Главное меню")

    return keyboard

# Кнопки изменения реквезитов
def req_frep():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row("🏦 Редактировать   реквезиты")
    keyboard.row("🔙 Главное меню")

    return keyboard


# Завершение загрузки товаров
finish_load_rep = ReplyKeyboardMarkup(resize_keyboard=True)
finish_load_rep.row("📥 Закончить загрузку товаров")
