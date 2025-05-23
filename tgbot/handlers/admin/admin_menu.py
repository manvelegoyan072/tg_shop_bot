# - *- coding: utf- 8 - *-
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.data.config import BOT_VERSION, PATH_LOGS, PATH_DATABASE
from tgbot.data.loader import dp
from tgbot.keyboards.reply_main import payments_frep, settings_frep, functions_frep, items_frep, req_frep
from tgbot.services.api_sqlite import get_storage_props
from tgbot.utils.const_functions import get_date
from tgbot.utils.misc.bot_filters import IsAdmin
from tgbot.utils.misc_functions import get_statistics


# Платежные системы
@dp.message_handler(IsAdmin(), text="🔑 Платежные системы", state="*")
async def admin_payment(message: Message, state: FSMContext):
    await state.finish()

    await message.answer("<b>🔑 Настройка платежных системы.</b>", reply_markup=payments_frep())


# Настройки бота
@dp.message_handler(IsAdmin(), text="⚙ Настройки", state="*")
async def admin_settings(message: Message, state: FSMContext):
    await state.finish()

    await message.answer("<b>⚙ Основные настройки бота.</b>", reply_markup=settings_frep())


# Общие функции
@dp.message_handler(IsAdmin(), text="🔆 Общие функции", state="*")
async def admin_functions(message: Message, state: FSMContext):
    await state.finish()

    await message.answer("<b>🔆 Выберите нужную функцию.</b>", reply_markup=functions_frep(message.from_user.id))


# Управление товарами
@dp.message_handler(IsAdmin(), text="🎁 Управление товарами", state="*")
async def admin_products(message: Message, state: FSMContext):
    await state.finish()

    await message.answer("<b>🎁 Редактирование товаров.</b>", reply_markup=items_frep())

# Управление реквезитов
@dp.message_handler(IsAdmin(), text="🏦 Реквезиты", state="*")
async def admin_props(message: Message, state: FSMContext):
    await state.finish()
    req_text = get_storage_props()
    props = req_text[0]


    await message.answer(f"Ваши текущие реквезиты:\n{props['name']}")
    await message.answer(f"<b>Редактирование реквезитов.</b>", reply_markup=req_frep())


# Cтатистики бота
@dp.message_handler(IsAdmin(), text="📊 Статистика", state="*")
async def admin_statistics(message: Message, state: FSMContext):
    await state.finish()

    await message.answer(get_statistics())


# Получение БД
@dp.message_handler(IsAdmin(), commands=['db', 'database'], state="*")
async def admin_database(message: Message, state: FSMContext):
    await state.finish()

    with open(PATH_DATABASE, "rb") as document:
        await message.answer_document(
            document,
            caption=f"<b>📦 BACKUP\n"
                    f"🕰 <code>{get_date()}</code></b>",
        )


# Получение Логов
@dp.message_handler(IsAdmin(), commands=['log', 'logs'], state="*")
async def admin_log(message: Message, state: FSMContext):
    await state.finish()

    with open(PATH_LOGS, "rb") as document:
        await message.answer_document(
            document,
            caption=f"<b>🖨 LOGS\n"
                    f"🕰 <code>{get_date()}</code></b>",
        )


# Получение версии бота
@dp.message_handler(commands=['version'], state="*")
async def admin_version(message: Message, state: FSMContext):
    await state.finish()

    await message.answer(f"<b>❇ Текущая версия бота: <code>{BOT_VERSION}</code></b>")
