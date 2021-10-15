import telebot
from config import TOKEN
import psycopg2
from psycopg2 import Error

bot = telebot.TeleBot(TOKEN)


def registration(message):
    lst = message.text.split(',')
    if len(lst) != 5:
        return bot.send_message(message.chat.id,
                                f'{message.from_user.first_name}, не правильный формат сообщения')

    name = lst[0].strip()
    group = lst[1].strip()
    task = lst[2].strip()
    variant = lst[3].strip()
    git = lst[4].strip()

    group_lst = ('212Б', '221Б', '214Б')
    if group not in group_lst:
        return bot.send_message(message.chat.id,
                                f'{message.from_user.first_name}, неправильный номер группы\n '
                                f'Список проверяемых групп: 212Б, 221Б, 214Б')

    if int(task) < 1 or int(task) > 5:
        return bot.send_message(message.chat.id,
                                f'{message.from_user.first_name}, неправильный номер задания\n '
                                f'Возможный номер задания от 1 до 5')

    if int(variant) < 1 or int(variant) > 5:
        return bot.send_message(message.chat.id,
                                f'{message.from_user.first_name}, неправильный номер варианта\n '
                                f'Возможный номер варианта от 1 до 5')

    if 'github.com/' not in git:
        return bot.send_message(message.chat.id,
                                f'{message.from_user.first_name}, некорректная ссылка')

    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="nazim080",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="students")
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        sql_insert = f"insert into students(name, group_num, task_num, var_num, git) " \
                     f"values('{name}', '{group}', {task}, {variant}, '{git}');"
        cursor.execute(sql_insert)
        connection.commit()
        cursor.execute('select * from students')
        print(cursor.fetchall())
        print(connection.get_dsn_parameters(), "\n")
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
    return bot.send_message(message.chat.id,
                            f'{message.from_user.first_name}, задание принято, идет проверка...')
