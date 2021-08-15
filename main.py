import markovify
import telebot
from telebot import types
from config import botToken

bot = telebot.TeleBot(botToken)

def makePrediction():
    text = open('horoscope.txt', encoding='utf8').read()
    text_model = markovify.Text(text)
    for i in range(1):
        #print(text_model.make_sentence(tries=100))
        return text_model.make_sentence(tries=100)
    
def actions_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    prediction = types.KeyboardButton(text="предскажи")
    keyboard.add(prediction)
    return keyboard

def sendPrediction(message):
    answer = makePrediction()
    bot.send_message(message.from_user.id, answer, reply_markup=actions_keyboard())


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'привет! я бот, который предсказывает будущее, если хочешь узнать, что тебя ждет, то напиши \"предскажи\"')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'предсказание' or 'предскажи':
        sendPrediction(message)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

def main():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()