from aiogram.fsm.state import StatesGroup, State


# main_handler.py
class MainForm(StatesGroup):
	book = State()  # Отдельный учебник какого-то автора


# Для админки
class AdminForm(StatesGroup):
	admin = State()


# english.py
class FormEnglish(StatesGroup):
	section = State()
	page = State()
	spotlight_on_russia_page = State()
	module = State()
	module_exercise = State()


# russian.py
class FormRussian(StatesGroup):
	exercise = State()


# math.py
class FormMath(StatesGroup):
	number = State()


# geometry.py
class FormGeometry(StatesGroup):
	section = State()
	# Вопросы к главам
	chapter = State()
	# Страница задач для подготовки к ЕГЭ
	page_for_exam_preparation_exercises = State()
	# Задача для подготовки к ЕГЭ
	exam_preparation_exercise = State()
	# Задача с математическим содержанием
	math_exercise = State()
	# Исследовательская задача
	research_exercise = State()
	# Обычный номер задания
	number = State()


# sociology.py
class FormSociology(StatesGroup):
	paragraph = State()


# physics.py
class FormPhysics(StatesGroup):
	section = State()
	book = State()
	paragraph = State()
	question = State()
	exercise = State()
