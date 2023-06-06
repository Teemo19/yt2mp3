import telebot
import time

from src.music_downloader.info_search import info_search
from src.music_downloader.downloader import Youtube
from src.music_downloader.directory import directory

TIMEOUT = 120

telebot.apihelper.READ_TIMEOUT = TIMEOUT
telebot.apihelper.RETRY_TIMEOUT = TIMEOUT
telebot.apihelper.LONG_POLLING_TIMEOUT = TIMEOUT

token = open("token.txt","r").read()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["help","start"])
def enviar(message):
    bot.reply_to(message,"descargar cancion: /mp3 nombre_de_la_cancion")


@bot.message_handler(commands=["mp3"])
def mp3(message):
    text = " ".join(message.text.split()[1:])
    data = info_search.song_info(text)
    link = info_search.get_link(data)
    title = info_search.get_title(data)
    artist = info_search.get_artist(data)
    yt = Youtube()

    if not directory.verifyDirectoryExist(f"music/{title}.mp3"):
        yt.download_mp3(link,title)
    audio = open(f"music/{title}.mp3",'rb')
    try:
        bot.reply_to(message,f"enviando {title}")
        time.sleep(0.1)
        bot.send_audio(message.chat.id,audio,performer=artist,timeout=800)
    except Exception as e:
        print(e)
        bot.reply_to(message,"No se pudo enviar, el archivo es demasiado pesado")


if __name__ == "__main__":
    print("Programa iniciado [READY]")
    bot.infinity_polling()