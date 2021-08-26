from instabot import Bot
import os
import glob
import cred

files = glob.glob('config/olagmerie_uuid_and_cookie.json')
for f1 in files:
    os.remove(f1)

config = cred.load()

bot = Bot()
bot.login(username = config['login'],  password = config['password'])
use_cookie = False


# Modul
twony_last_medias_modul = bot.get_user_medias("wearemodul", filtration = None)

media_id_modul = twony_last_medias_modul[0]
media_info_modul = bot.get_media_info(media_id_modul)[0]

location_modul = media_info_modul["location"].get('short_name')

caption_modul = media_info_modul["caption"].get('text')


modul = "Место: " +str(location_modul)+   "\n\nОписание: " +str(caption_modul)


# Hide
twony_last_medias_hide = bot.get_user_medias("minskhide", filtration = None)

media_id_hide = twony_last_medias_hide[0]
media_info_hide = bot.get_media_info(media_id_hide)[0]

location_hide = 'Hide'

caption_hide = media_info_hide["caption"].get('text')


hide = "Место: " +str(location_hide)+   "\n\nОписание: " +str(caption_hide)


# lo-fi
twony_last_medias_lo_fi = bot.get_user_medias("lofisocialclub", filtration = None)

media_id_lo_fi = twony_last_medias_lo_fi[0]
media_info_lo_fi = bot.get_media_info(media_id_lo_fi)[0]

location_lo_fi = media_info_lo_fi["location"].get('short_name')

caption_lo_fi = media_info_lo_fi["caption"].get('text')


lo_fi = "Место: " +str(location_lo_fi)+   "\n\nОписание: " +str(caption_lo_fi)


# Emotion
twony_last_medias_Emotion = bot.get_user_medias("emotionfactory.minsk", filtration = None)

media_id_Emotion = twony_last_medias_Emotion[0]
media_info_Emotion = bot.get_media_info(media_id_Emotion)[0]

location_Emotion = 'EMOTION FACTORY'

caption_Emotion = media_info_Emotion["caption"].get('text')


Emotion = "Место: " +str(location_Emotion)+   "\n\nОписание: " +str(caption_Emotion)
