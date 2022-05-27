import telebot
import time

# token
bot = telebot.TeleBot("5577968369:AAF9fFDTSIWXfY_oWdf3iVBzSgSeZyUFcBw")

# link to the channel
CHANNEL_NAME = "@lablablab23"

# загрузка списка шуток
f = open("data/fun.txt", "r", encoding="UTF-8")
jokes = f.read().split("\n")
f.close()

# пока не закончатся шутки, посылаем их в канал
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    # пауза в один час
    time.sleep(10)

bot.send_message(CHANNEL_NAME, "анекдоты закончились (и слава богу)")


# ---------------------------------------------------------------------------------

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, я бот, который отправляет анекдоты за 300')


# Запускаем бота
bot.polling(none_stop=True, interval=0)
