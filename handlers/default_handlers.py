from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

import config

router = Router()


@router.message(Command('start'))
async def greeting(message: Message) -> None:
	await message.answer(config.GREETING_MESSAGE.format(first_name=message.from_user.first_name,
	                                                    last_name=message.from_user.last_name)
	                     )


@router.message(F.text)
async def other_text(message: Message):
	await message.answer('Чтобы отобразить список учебников, введите /list')
