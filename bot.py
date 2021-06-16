
import config
import telebot

bot = telebot.TeleBot('1855568832:AAFxk0I2fT9EG4US1FfB_eeJ4odUs8udD-0')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
