import telebot
from extensions import APIException
from extensions import CryptoConvector
from config import TOKEN, keys


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Для работы бота введите запрос в следующем формате <ваша валюта> \
<в какую валюту выполнить перевод> <количество валюты>.  \
Чтобы увидеть список доступных валюты введите /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Список доступных валют:'
    for key in keys:
        text += f'\n{key}:  {keys[key]}'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) < 3:
            raise APIException('Ой. ошибочка, чего-то не хватает')

        if len(values) > 3:
            raise APIException('Ой. ошибочка, что-то лишнее')

        base, quote, amount = values
        total = CryptoConvector.get_price(base, quote, amount)
        bot.reply_to(message, round(total, 4))
    except APIException as e:
        bot.reply_to(message, e)


bot.polling()
