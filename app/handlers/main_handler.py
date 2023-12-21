from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from .english import router_english
from .russian import router_russian, FormRussian
from ..keyboards.keyboards import book_selection_kb, EnglishKeyboards
from .math import router_math, FormMath

router = Router()
router.include_routers(
	router_english,
	router_russian,
	router_math
	)

english_kb = EnglishKeyboards()


class MainForm(StatesGroup):
	book = State()  # Отдельный учебник какого-то автора


@router.message(Command('list'))
async def book_selection(message: Message, state: FSMContext) -> None:
	await state.set_state(MainForm.book)

	await message.answer('Выбери учебник 📐📓📊📘', reply_markup=book_selection_kb())


@router.message(MainForm.book)
async def numbering_selection(message: Message, state: FSMContext) -> None:
	subject = message.text.split(' ', 1)[0].lower()

	if subject == 'английский':
		await state.update_data(book=message.text)
		await message.answer('Теперь выбери раздел', reply_markup=english_kb.section_selection_kb(message.text))
	elif subject == 'русский':
		await state.update_data(book=message.text)
		await state.set_state(FormRussian.exercise)

		await message.answer('Теперь введи упражнение 📃 _(от 1 до 396 включительно)_',
		                     reply_markup=ReplyKeyboardRemove())
	elif subject == 'алгебра-задачник':
		await state.update_data(book=message.text)
		await state.set_state(FormMath.number)

		await message.answer('Теперь введи номер задания 📖 _(от 1.1 до 60.19 включительно)_',
		                     reply_markup=ReplyKeyboardRemove())
	else:
		await message.reply('Не найдено 😕', reply_markup=ReplyKeyboardRemove())
		await state.clear()

# @router.message(FormBook.numbering)
# async def get_solve(message: Message, state: FSMContext) -> None:
# 	if check_numbering(message.text):
# 		await state.update_data(numbering=message.text)
# 		data = await state.get_data()
#
# 		book = data.get('book', '')
# 		numbering = data.get('numbering', '')
#
# 		parser = Parser(book, numbering)
# 		result = await parser.get_solution_data()
#
# 		if result:
# 			solution = result.get('solution')
# 			title = result.get('title')
#
# 			await send_solution(message, solution, title)
# 		else:
# 			await message.answer('Не найдено 😕', reply_markup=ReplyKeyboardRemove())
# 	else:
# 		await message.answer('Не найдено 😕', reply_markup=ReplyKeyboardRemove())
# 	await state.clear()
