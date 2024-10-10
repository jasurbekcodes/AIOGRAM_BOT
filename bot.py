import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils import get_list, calculate

TOKEN = "8125936730:AAFtw79qXQT8dQiFGruDamFlYt_LzyO2Duw"

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")

@dp.message(F.text == "test")
async def test_command_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")


@dp.message(F.text == "Tabriknomalar")
async def greeting_cards_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Bayramlar"), KeyboardButton(text="Tug'ilgan kun")],
            [KeyboardButton(text="To'y"), KeyboardButton(text="Yubiley")]
        ],
        resize_keyboard=True
    )
    await message.answer("Nima bilan tabriklamoqchisiz?", reply_markup=keyboard)

# "Bayramlar" tugmasi tanlanganda bayramlar ro'yxati chiqariladi
@dp.message(F.text == "Bayramlar")
async def holidays_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Yangi Yil"), KeyboardButton(text="Xotira va Qadrlash kuni")],
            [KeyboardButton(text="Mustaqillik kuni"), KeyboardButton(text="Mustaqillik kuni")],
            [KeyboardButton(text="O'qituvchi va Murabbiylar kuni"), KeyboardButton(text="Konstitutsiya kuni")],
            [KeyboardButton(text="Ramazon Hayiti"), KeyboardButton(text="Qurbon Hayiti")],
            [KeyboardButton(text="Xalqaro xotin-qizlar kuni"), KeyboardButton(text="Navro'z bayrami")],
            [KeyboardButton(text="Vatan himoyachilari kuni"), KeyboardButton(text="Orqaga")],
        ],
        resize_keyboard=True
    )
    await message.answer("Qaysi bayram bilan tabriklamoqchisiz?", reply_markup=keyboard)


@dp.message(F.text == "Tug'ilgan kun")
async def happy_birthday_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Erkak"), KeyboardButton(text="Ayol")],
            [KeyboardButton(text="Bolakay"), KeyboardButton(text="Qizaloq")],
            [KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
    )
    await message.answer("Kimni tabriklamoqchisiz?", reply_markup=keyboard)


@dp.message(F.text == "To'y")
async def wedding_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Erkak"), KeyboardButton(text="Ayol")],
            [KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
    )
    await message.answer("Kimni tabriklamoqchisiz?", reply_markup=keyboard)



@dp.message(F.text == "Yubiley")
async def anniversary_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Erkak"), KeyboardButton(text="Ayol")],
            [KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
    )
    await message.answer("Kimni tabriklamoqchisiz?", reply_markup=keyboard)



@dp.message(F.text == "Orqaga")
async def back_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Bayramlar"), KeyboardButton(text="Tug'ilgan kun")],
            [KeyboardButton(text="To'y"), KeyboardButton(text="Yubiley")]
        ],
        resize_keyboard=True
    )
    await message.answer("Nima bilan tabriklamoqchisiz?", reply_markup=keyboard)

# Boshqa barcha xabarlar uchun handler
@dp.message()
async def generic_message_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Tabriknomalar")]],
        resize_keyboard=True
    )
    await message.answer("Assalomu alaykum.\nQuyidagi kerakli bo‘limni tanlang!", reply_markup=keyboard)

# Botni ishga tushirish funksiyasi
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
