import os

from .states import FormEnglish, FormRussian, FormMath, FormGeometry, FormSociology, FormPhysics

HEADERS = {
	'User-Agent': 'Mozilla/5.0',
	}

TOKEN = os.environ.get('BOT_TOKEN')

MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')

FLOAT_NUMBER_PATTERN = r'\d+\.\d+'
# TODO: Добавить выбор сайта для парсинга решений
PARSER_ENGINE = 'gdz.ru'

# Предмет -> Серия учебника -> Класс -> Авторы
BOOKS = {
	'английский': ['Английский Spotlight 10 Класс В. Эванс, Д. Дули', 'english1', FormEnglish.section],
	'русский': ['Русский 10-11 Класс А.И. Власенков, Л.М. Рыбченкова', 'russian1', FormRussian.exercise],
	'алгебра-задачник': ['Алгебра-Задачник 10-11 Класс А.Г. Мордкович, П. В. Семенов', 'math1', FormMath.number],
	'геометрия': ['Геометрия 10-11 Класс Л.С. Атанасян, В.Ф Бутузов', 'geometry1', FormGeometry.section],
	'обществознание': ['Обществознание 10 Класс О.Б. Соболева, В.В. Барабанов', 'sociology1', FormSociology.paragraph],
	'физика': ['Физика 10 класс Г.Я. Мякишев, Б.Б. Буховцев', 'physics1', FormPhysics.paragraph],
	}

SECTIONS = {
	'английский spotlight 10 класс в. эванс, д. дули': [
		'Spotlight on Russia',
		'Song sheets',
		'Страницы учебника'
		],
	'геометрия 10-11 класс л.с. атанасян, в.ф бутузов': [
		'Вопросы к главе',
		'Задачи для подготовки ЕГЭ',
		'Задачи с мат. содержанием',
		'Исследоват. задачи',
		'Номера'
		],
	'физика 10 класс г.я. мякишев, б.б. буховцев': [
		'Образцы заданий ЕГЭ',
		'Вопросы'
		]
	}

GET_HELP_MESSAGE = '''Я - бот, созданный для облегчения поиска решения заданий с сайтов gdz.ru | reshak.ru | resheba.me. 
Моя основная функция - предоставление готовых решений задач по вашему запросу.

Вот как я работаю:
1. Вводите команду /list.
2. Выбираете нужный учебник.
3. Выбираете нужный раздел учебника, если они доступны.
4. Вводите номер страницы | упражнения | параграфа | задания в соответствии с выбранным учебником.
5. Я ищу решение на одном из этих сайтов gdz.ru | reshak.ru | resheba.me.
6. Если решение найдено, то я отправляю вам его.

‼ Если вы найдете баги, возникнут вопросы или появятся идеи для продвижения бота, то настоятельно прошу обращаться к 
этому человеку >>> [Leo Proger](https://t.me/Leo_Proger)
'''

GREETING_MESSAGE = '''
Привет, ***{first_name} {last_name}***!

Доступные команды:
/start - Запуск и приветствие бота
/list - Отображает список учебников
/help - Информация о боте
'''

SLEEP_TIME = 120
MESSAGE_DELAY = 0.3
