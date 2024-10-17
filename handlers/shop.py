from aiogram import Bot, Dispatcher, html, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram import Router
from aiogram.fsm.context import FSMContext
from sessions import get_customer, register_customer
from states.shop import Shop
from utils import get_word

shop_router = Router()


@shop_router.message(F.text.in_(['Tabriknomalar', 'Открытки', 'Devor uchun', 'Для стены']))
async def company_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Shop.product_type)
    customer, _ = await get_customer(message.from_user.id)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=await get_word('Bayram', customer['lang'])),
                   KeyboardButton(text=await get_word('Tugulgan kun', customer['lang']))],
                  [KeyboardButton(text=await get_word('Toy', customer['lang'])),
                   KeyboardButton(text=await get_word('Yubiley', customer['lang'])),]],
        resize_keyboard=True)

    await message.answer(await get_word('choose-event', customer['lang']), reply_markup=keyboard)


@shop_router.message(F.text.in_(['Bayram']))
async def event_handler(message: Message, state: FSMContext) -> None:

    customer, _ = await get_customer(message.from_user.id)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Yangi yil"),
             KeyboardButton(text="Mustaqillik kuni")],
            [KeyboardButton(text="Konstitutsiya kuni"),
            KeyboardButton(text="Xotira va Qadrlash kuni")],
            [KeyboardButton(text="O'qituvchi va Murabbiylar kuni"),
            KeyboardButton(text="Ramazon Hayiti")],
            [KeyboardButton(text="Qurbon Hayiti"),
             KeyboardButton(text="Xalqaro Xotin-Qizlar kuni")],
            [KeyboardButton(text="Navro'z bayrami"),
             KeyboardButton(text="VAtan himoyachilar kuni")],
        ],
        resize_keyboard=True
    )

    await message.answer("Iltimos, bayram turini tanlang:", reply_markup=keyboard)


@shop_router.message(F.text.in_(['Tugulgan kun']))
async def birthday_handler(message: Message, state: FSMContext) -> None:

    customer, _ = await get_customer(message.from_user.id)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Erkak"),
             KeyboardButton(text="Ayol")],
            [KeyboardButton(text="Qizaloq"),
            KeyboardButton(text="Bolakay")],
        ],
        resize_keyboard=True
    )

    await message.answer("Iltimos, bayram turini tanlang:", reply_markup=keyboard)


@shop_router.message(F.text.in_(['Toy']))
async def wedding_handler(message: Message, state: FSMContext) -> None:

    customer, _ = await get_customer(message.from_user.id)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Erkak"),
             KeyboardButton(text="Ayol")],
        ],
        resize_keyboard=True
    )

    await message.answer("Iltimos, bayram turini tanlang:", reply_markup=keyboard)


@shop_router.message(F.text.in_(['Yubiley']))
async def anniversary_handler(message: Message, state: FSMContext) -> None:

    customer, _ = await get_customer(message.from_user.id)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Erkak"),
             KeyboardButton(text="Ayol")],
        ],
        resize_keyboard=True
    )

    await message.answer("Iltimos, bayram turini tanlang:", reply_markup=keyboard)


