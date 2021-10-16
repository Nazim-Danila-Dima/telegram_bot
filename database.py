import psycopg2
from psycopg2 import Error

from github import download_rep



# Проверка на наличе в базе ученика
def database_checking(name, task, variant):
    try:
        # # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="nazim080",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="students")
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        sql_checking = f"SELECT COUNT(name) FROM students WHERE name = '{name}' and " \
                       f"task_num = {task} and var_num = {variant}"

        cursor.execute(sql_checking)
        print(cursor.execute(sql_checking))
        print(name)
        print(task)
        print(variant)
        return cursor.execute(sql_checking)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def database_update(name, group, task, variant, git):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="nazim080",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="students")
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        sql_update = f"update students set progress = '{download_rep(git)}'" \
                     f"where name = '{name}' and group_num = '{group}' and " \
                     f"task_num = {task} and var_num = {variant} and git = '{git}';"
        cursor.execute(sql_update)
        connection.commit()
        cursor.execute('select * from students')
        print(cursor.fetchall())
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def database_insert(name, group, task, variant, git):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="nazim080",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="students")
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        sql_insert = f"insert into students(name, group_num, task_num, var_num, git, progress) " \
                     f"values('{name}', '{group}', {task}, {variant}, '{git}', '{download_rep(git)}');"
        cursor.execute(sql_insert)
        connection.commit()
        cursor.execute('select * from students')
        print(cursor.fetchall())
        print('1')
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def print_res():
    connection = psycopg2.connect(user="postgres",
                                  password="nazim080",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="students")
    cursor = connection.cursor()
    cursor.execute('select name, group_num, task_num, var_num, git, progress from students')
    res = ''
    for row in cursor.fetchall():
        row = list(row)
        for j in range(len(row)):
            row[j] = str(row[j]).strip()
        res += ' | '.join(row) + '\n'
    return res
    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто")


# print(database_checking('Иванов Петр Иванович', 2, 3))