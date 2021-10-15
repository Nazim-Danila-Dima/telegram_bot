import telebot
from functions_student import registration
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, отправь свое задание.\n'
                                      f'Формат сообщения должен быть вида: "ФИО, номер группы, '
                                      f'номер задания, номер варианта, гит репозиторий"\n'
                                      f'Пример: "Иванов Иван Иванович, 212Б, 2, 3, '
                                      f'github.com/ivanov/task"')


@bot.message_handler(content_types=['text'])
def student_register(message):
    bot.register_next_step_handler(registration(message), student_register)


if __name__ == '__main__':
    bot.polling(none_stop=True)
