import telebot
import g4f

def ask(ss):
    response=g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=[
            {"role":"user",'content':ss}
        ])
    return response


BOT_TOKEN = '6494467416:AAHHlruM-FKKyAyiWpPNviKsrfZuw0K3ECQ'
id_adm='1589821395'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, ask(message.text))

bot.infinity_polling()
