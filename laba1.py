import telebot
bot = telebot.TeleBot('6723324891:AAE2Z6X8q_eYn73d-pCaxG4BB0rTW_6gN8g')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, как дела?")
    elif message.text == "/hi":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /hi.")
bot.polling(none_stop=True, interval=0)