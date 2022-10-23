import requests
import telebot
from telebot import types
import json

#Ввод токена бота из BotFather
bot = telebot.TeleBot(token)


#Объявление приветствия и кнопок Главного меню
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    fun = types.KeyboardButton('Веселье')
    help = types.KeyboardButton('Тех.поддержка')
    markup.add(fun, help)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!\n Добро пожаловать и веселого время препровождения!', reply_markup=markup)


#Объявление команд бота при ответах пользователя при нажатии определённых кнопок
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Главное меню": #кнопки вылезающие при вызове Главного меню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        fun = types.KeyboardButton("Веселье")
        help = types.KeyboardButton("Тех.поддержка")
        markup.add(fun, help)
        bot.send_message(message.chat.id, text="Вы в главном меню", reply_markup=markup)

    elif message.text == "Тех.поддержка": #информация вылезающая при вызове Тех.поддержки
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Автор: Лихачев Леонид\nГруппа: 2-МВ-4\nVK: https://vk.com/majorrainbow\nTelegram: @MajorRainbow", reply_markup=markup)

    elif message.text == "Веселье": #кнопки вылезающие при вызове вкладки Веселье, доступ к трём различным видам картинок
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cats = types.KeyboardButton("Котик\U0001F431")
        dogs = types.KeyboardButton("Собака\U0001F436")
        anime = types.KeyboardButton("Аниме тян\U0001F497")
        back = types.KeyboardButton("Главное меню")
        markup.add(cats, dogs, anime, back)
        bot.send_message(message.chat.id, text="Развлечения", reply_markup=markup)

    elif message.text == "Котик\U0001F431": #картинки с котиками
        r = requests.get('http://thecatapi.com/api/images/get?format=src')
        url = r.url
        bot.send_photo(message.from_user.id, url)

    elif message.text == "Собака\U0001F436": #картинки с собачками
        r = requests.get('http://thedogapi.com/api/images/get?format=src')
        url = r.url
        bot.send_photo(message.from_user.id, url)

    elif message.text == "Аниме тян\U0001F497": #картинки с девочками из аниме
        bot.send_photo(message.from_user.id, photo=tyan())

#Функция для вывода картинки с девочкой через формат JSON
def tyan():
    url = 'https://api.waifu.pics/sfw/waifu'
    page = requests.get(url)
    if page.status_code == 200:
        str = page.text
        anime = json.loads(str)
        return anime["url"]


#Бот постоянно работает, пока запущена программа
bot.polling(none_stop=True)






