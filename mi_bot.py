import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

TOKEN = '524933887:AAHIqjshtzzDu5hWmeTb7H_b-HoBnjSsSYA'

mi_bot = telegram.Bot(token=TOKEN)
mi_bot_updater = Updater(mi_bot.token)

def start(bot=mi_bot, update=mi_bot_updater):
    print ("Iniciada conversación: ")
    print (update.message.chat_id)
    bot.sendMessage(chat_id=update.message.chat_id, text="Hola, soy un bot")

# Handle para saludo
def hola(bot=mi_bot, update=mi_bot_updater):
    print ("Solicito saludo")
    bot.sendMessage(chat_id=update.message.chat_id, text="Holi :3")

def img(bot=mi_bot, update=mi_bot_updater):
    print("Solicito imagen")
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('8.jpeg', 'rb'))

def pose(bot=mi_bot, update=mi_bot_updater):
    print("Solicito una pose")
    bot.sendVoice(chat_id=update.message.chat_id, voice=open('jojo.mp3', 'rb'))


#Definimos para cada comando la función que atendera la peticion
start_handler = CommandHandler('start', start)
hola_handler = CommandHandler('hola', hola)
img_handler = CommandHandler('img', img)
pose_handler = CommandHandler('pose', pose)
dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(hola_handler)
dispatcher.add_handler(img_handler)
dispatcher.add_handler(pose_handler)

mi_bot_updater.start_polling()

while True: #Ejecutamos nuestro programa por siempre
    pass
