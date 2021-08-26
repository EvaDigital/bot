import telebot
from telebot import types

import parser

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да")
    item2 = types.KeyboardButton("Нет")

    markup.add(item1, item2)

    bot.send_message(message.from_user.id, "Дарова, на рейв хош?", reply_markup=markup)

    


@bot.message_handler(content_types=['text'])
def start(message):
    list_hello = ["Привет", "привет", "хай", "Хай"]
    if message.text in list_hello:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Да")
        item2 = types.KeyboardButton("Нет")

        markup.add(item1, item2)

        bot.send_message(message.chat.id, "Дарова, на рейв хош?", reply_markup=markup)

        
    elif message.chat.type == 'private':
        list = ["Да", "хочу", "Хочу", "да", "конечно", "Конечно"]
        list2 = ["нет", "не хочу", "Не хочу", "Нет"]
        if message.text in list:
            markdown = types.InlineKeyboardMarkup(row_width=4)
            item1 = types.InlineKeyboardButton("Modul Art Platform", callback_data='Modul')
            item2 = types.InlineKeyboardButton("Hide", callback_data='Hide')
            item3 = types.InlineKeyboardButton("Lo-Fi Social Club", callback_data='Lo-Fi')
            item4 = types.InlineKeyboardButton("Emotion Factory", callback_data='Emotion')

            markdown.add(item1, item2, item3, item4)

            bot.send_message(message.from_user.id, "Выбери клуб)", reply_markup=markdown)

        elif message.text in list2:
            bot.send_message(message.from_user.id, "Жаль... Такое упускаешь") 

        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

    
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'привет'")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Modul':
                bot.send_message(call.message.chat.id, parser.modul)

            elif call.data == 'Hide':
                bot.send_message(call.message.chat.id, parser.hide)

            elif call.data == 'Lo-Fi':
                bot.send_message(call.message.chat.id, parser.lo_fi)
                
            elif call.data == 'Emotion':
                bot.send_message(call.message.chat.id, parser.Emotion)


        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message.id, text="А спать хочешь?",
            reply_markup=None)			
    
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True, interval=0)