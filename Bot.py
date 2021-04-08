import requests
import telebot

bot = telebot.TeleBot("1709338871:AAFO1IJ-aix0_s7fQBYMNHONmuBLMPq2MKA", parse_mode="HTML") # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Selamat datang di bot tiktok downloader by sandroputraa")


@bot.message_handler(regexp=r"/download (.*)")
def handle_message(m):
    text = m.text
    chat_uid = m.chat.id
    slice = text.split(" ")

    Url = "http://sandroputraa.my.id/API/Tiktok.php"
    Payload = {"link":""+str(slice[1])+""}
    Header = {
        "Content-Type": "application/json",
        "Auth": "sandrocods"
    }

    response = requests.request("POST", Url, json=Payload, headers=Header)
    JsonResponse = response.json()

    if 'Error Parameter link must be tiktok url' == JsonResponse['Message']:
        bot.reply_to(m, "Gagal Mengambil Video. Link Harus dari Tiktok")

    elif 'Error To many Request / Video Not Found' == JsonResponse['Message']:
        bot.reply_to(m, "Video Tidak Ditemukan")

    else:
        bot.reply_to(m, "Video Ditemukan")
        download = requests.request("GET", JsonResponse['No_Watermark'], verify=False)
        with open('ok.mp4', 'wb') as f:
            f.write(download.content)

        Vid = open('ok.mp4', 'rb')
        bot.send_video(chat_uid, Vid)





bot.polling()