import os

from dotenv import load_dotenv

load_dotenv()

TOKEN: str = os.environ.get('BOT_TOKEN')
DATABASE_PATH: str = os.environ.get('DATABASE_PATH')

# Предмет -> Серия учебника -> Класс -> Авторы
BOOKS: dict[str: str] = {
    'английский': 'Английский Spotlight 10 Класс В. Эванс, Д. Дули',
    'русский': 'Русский 10-11 Класс А.И. Власенков, Л.М. Рыбченкова',
    'алгебра-задачник': 'Алгебра-Задачник 10-11 Класс А.Г. Мордкович, П. В. Семенов',
    'геометрия': 'Геометрия 10-11 Класс Л.С. Атанасян, В.Ф Бутузов',
    'обществознание': 'Обществознание 10 Класс О.Б. Соболева, В.В. Барабанов',
}

HEADERS: dict[str: str] = {
    'User-Agent': 'Mozilla/5.0',
}

ERROR_MESSAGE_404: str = '{} не найден{}'
ERROR_MESSAGE_500: str = 'Ой, у меня ошибка. Прошу написать ему >>> [Leo Proger](https://t.me/Leo_Proger)'

GREETING_MESSAGE: str = ('Привет, ***{first_name} {last_name}***!\n\nЧтобы посмотреть доступные учебники введи /list, '
                         'чтобы получить информацию введи /help')
GET_HELP_MESSAGE: str = '''Я - бот, созданный для облегчения поиска решения заданий с сайта gdz.ru. 
Моя основная функция - предоставление готовых решений задач по вашему запросу.

Вот как я работаю:
1. Вы выбираете нужный учебник, введя команду /list.
2. Вводите страницу/упражнение/номер/параграф в соответствии с выбранным учебником.
3. Я ищу решение этого задания на сайте gdz.ru.
4. Если решение найдено, то я отправляю вам его.

‼ Если вы найдете баги, возникнут вопросы или появятся идеи для продвижения бота, то настоятельно прошу обращаться к 
этому человеку >>> [Leo Proger](https://t.me/Leo_Proger)'''

SLEEP_TIME: int = 120

MESSAGE_DELAY = 0.3

NUMBER_PATTERN: str = r'^([1-9]|[1-3][0-9]|4[0-9]|49)\.\d+$'
