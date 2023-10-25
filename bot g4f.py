import telebot

# Вставьте ваш токен бота
TOKEN = '6494467416:AAHHlruM-FKKyAyiWpPNviKsrfZuw0K3ECQ'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для отправки сообщений.')

# Обработчик команды /hello
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, 'Helloo!')

# Запускаем бота
bot.polling()
