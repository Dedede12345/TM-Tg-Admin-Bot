from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from utils import start_flask_container, stop_flask_container

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет ! Я бот-админ EC2 инстанса без какой-либо архитектуры безопасности.\nДоступные комманды: /start_flask, /stop_flask")

@router.message(Command("start_flask"))
async def start_flask(msg: Message):
    result = await start_flask_container()
    await msg.answer(f"Response: {result}")

@router.message(Command("stop_flask"))
async def stop_flask(msg: Message):
    result = await stop_flask_container()
    await msg.answer(f"Response: {result}")

@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")



