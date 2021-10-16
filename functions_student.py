import telebot
from config import TOKEN
from database import database_insert
from database import database_checking
from database import database_update

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

    if database_checking(name, task, variant) != None:
        database_insert(name, group, task, variant, git)
    else:
        database_update(name, group, task, variant, git)
    return bot.send_message(message.chat.id,
                            f'{message.from_user.first_name}, задание принято, идет проверка...')
