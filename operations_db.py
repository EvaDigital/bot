import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import cred

config = cred.load()

def get_place(clubs_id):
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user= config['user_db'],
                                password= config['password_db'],
                                host= config['host_db'],
                                port= config['potr_db'],
                                database= config['name_db'])
        
    cursor = connection.cursor()
    postgresql_select_query = "select * from clubs where id = %s"

    cursor.execute(postgresql_select_query, (clubs_id,))
    place = cursor.fetchall()
    for row in place: 
        return row[1]


def get_info(clubs_id):
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                password="root7656",
                                host="127.0.0.1",
                                port="8000",
                                database="bot_db")
        
    cursor = connection.cursor()
    postgresql_select_query = "select * from clubs where id = %s"

    cursor.execute(postgresql_select_query, (clubs_id,))
    info = cursor.fetchall()
    for row in info:      
        return row[2]

    if connection:
        cursor.close()
        connection.close()       
        print("Соединение с PostgreSQL закрыто")

    


place_modul = get_place(1)
place_hide = get_place(2)
place_lofi = get_place(3)
place_emotion = get_place(4)

info_modul = get_info(1)
info_hide = get_info(2)
info_lofi = get_info(3)
info_emotion = get_info(4)

# print(place_modul)
# print(place_hide, info_hide)
# print(place_lofi, info_lofi)
# print(place_emotion, info_emotion)

