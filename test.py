import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="nazim080",
                              host="127.0.0.1",
                              port="5432",
                              database="students")
cursor = connection.cursor()
cursor.execute('select * from students')


def print_res():
    for row in cursor.fetchall():
        row = list(row)
        for j in range(len(row)):
            row[j] = str(row[j]).strip()
        print(row)


print_res()

print(connection.get_dsn_parameters(), "\n")
