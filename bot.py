import telebot
import config # Импорт config.py
import urllib.request # request нужен для загрузки файлов от пользователя

bot = telebot.TeleBot(config.token) # Передаём токен из файла config.py

# Тут работаем с командой start
@bot.message_handler(commands=['start'])
def welcome_start(message):
    bot.send_message(message.chat.id, 'Приветствую тебя user')
 
# Тут работаем с командой help
@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Чем я могу тебе помочь')
    
@bot.message_handler(content_types=["text"])
def text(message):
    print(message.text)
    
@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'И тебе hello')
        
        bot.polling(none_stop=True, interval=0)
