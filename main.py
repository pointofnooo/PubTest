import telebot
from cfg import keys, TOKEN
from utils import ConversionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = '''Чтобы начать работу, введите команду боту в следующем формате: \n
- <имя валюты>\n
- <в какую валюту перевести> \n
- <количество переводимой валюты>\n
- Увидеть список всех доступных валют: /values'''
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n' .join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConversionException('Слишком много параметров. ')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
#=======================================================================
# Мой костыль. Без него при любом количестве конвертирует только единицу
        conv_out = float(total_base)*float(amount)
#=======================================================================
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя, \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {conv_out}' #conv_out, вместо total_base
        bot.send_message(message.chat.id, text)


bot.polling()