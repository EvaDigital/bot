from instabot import Bot
import os
import glob
import cred
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

files = glob.glob('config/*.json')
for f1 in files:
    os.remove(f1)

config = cred.load()

bot = Bot()
bot.login(username = config['login'],  password = config['password'])
use_cookie = False



try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="root7656",
                                  host="127.0.0.1",
                                  port="8000",
                                  database="bot_db")
    
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()

    twony_last_medias_modul = bot.get_user_medias("wearemodul", filtration = None)

    media_id_modul = twony_last_medias_modul[0]
    media_info_modul = bot.get_media_info(media_id_modul)[0]

    location_modul = media_info_modul["location"].get('short_name')

    caption_modul = media_info_modul["caption"].get('text')


    # modul = "Место: " +str(location_modul)+   "\n\nОписание: " +str(caption_modul)
        
    # info_modul = """ INSERT INTO clubs (ID, PLASE, INFO)  VALUES (1, '{location_modul}', '{caption_modul}')"""
    cursor.execute("UPDATE clubs SET PLASE = %s, INFO = %s WHERE ID = 1", (location_modul, caption_modul))
    connection.commit()
    print("1 запись успешно вставлена")   
        


    # Hide
    twony_last_medias_hide = bot.get_user_medias("minskhide", filtration = None)

    media_id_hide = twony_last_medias_hide[0]
    media_info_hide = bot.get_media_info(media_id_hide)[0]

    location_hide = 'Hide'

    caption_hide = media_info_hide["caption"].get('text')


    # hide = "Место: " +str(location_hide)+   "\n\nОписание: " +str(caption_hide)

    cursor.execute("UPDATE clubs SET PLASE = %s, INFO = %s WHERE ID = 2", (location_hide, caption_hide))
    connection.commit()
    print("2 запись успешно вставлена")


    # lo-fi
    twony_last_medias_lo_fi = bot.get_user_medias("lofisocialclub", filtration = None)

    media_id_lo_fi = twony_last_medias_lo_fi[0]
    media_info_lo_fi = bot.get_media_info(media_id_lo_fi)[0]

    location_lo_fi = media_info_lo_fi["location"].get('short_name')

    caption_lo_fi = media_info_lo_fi["caption"].get('text')


    # lo_fi = "Место: " +str(location_lo_fi)+   "\n\nОписание: " +str(caption_lo_fi)

    cursor.execute("UPDATE clubs SET PLASE = %s, INFO = %s WHERE ID = 3", (location_lo_fi, caption_lo_fi))
    connection.commit()
    print("3 запись успешно вставлена")


    # Emotion
    twony_last_medias_Emotion = bot.get_user_medias("emotionfactory.minsk", filtration = None)

    media_id_Emotion = twony_last_medias_Emotion[0]
    media_info_Emotion = bot.get_media_info(media_id_Emotion)[0]

    location_Emotion = 'EMOTION FACTORY'

    caption_Emotion = media_info_Emotion["caption"].get('text')


    # Emotion = "Место: " +str(location_Emotion)+   "\n\nОписание: " +str(caption_Emotion)

    cursor.execute("UPDATE clubs SET PLASE = %s, INFO = %s WHERE ID = 4", (location_Emotion, caption_Emotion))
    connection.commit()
    print("4 запись успешно вставлена")
   
    # Выполнение SQL-запроса

    cursor.execute("SELECT * from clubs")
    record = cursor.fetchall()
    print("Результат", record)
    
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

if connection:
    cursor.close()
    connection.close()       
    print("Соединение с PostgreSQL закрыто")





# Modul

