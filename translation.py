class Translation(object):


#This will be appeared when anyone use start command

      START = """Hello {0}

I am a converter clone of [Convert Ns Bot](https://telegram.dog/convert_Ns_bot) by {1}

I can convert file to video or video to file with custom thumbnail support.
"""


#This will be appeared when anyone use help command

      HELP = """**Apakah Kamu Membutuhkan Bantuan?**

1. Kirimkan File atau Video yang ingin Kamu Convert.

2. Kirimkan Sebuah Thumbnail (Optional).

3. Reply di Video dan ketik /converttofile untuk Convert Menjadi File.

4. Reply to File dan Ketik /converttovideo untuk Convert Menjadi Video.

**SUPPORT BOT:** [KITGBOTZ SUPPORT BOT](https://telegram.dog/kitgbotzsupport_bot)
"""


      ABOUT = """
**📝 Language:** Python 3

**🧰 Framework:** Pyrogram

**👨‍💻 Developer:** [Kevin Arifandi](https://t.me/kepinnaripp)

**📮 Channel:** [KITGBOTZ](https://t.me/kitgbotz)

**👥 Support:** [KITGBOTZ SUPPORT](https://t.me/kitgbotzsupport_bot)

**💻 Source Code:**[Tekan Disini](https://github.com/HariyonoRizki2/TG-CONVERT-BOT)

"""

####################################################################################################################################################
####################################################################################################################################################



#If you set the password for the bot if anyone use the bot without logging in this text will appear

      NOT_LOGGED_TEXT = """Ini Merupakan Bot Private, Kamu Harus Login Menggunakan Password untuk Menggunakan Bot Ini.
Untuk Login, Gunakan Command <code>/login BotPassword</code>. Lalu Gunakan Botnya 🥰"""


#This will be sent to the user when the user logged successfully

      SUCESS_LOGIN = """Kamu Berhasil Masuk! Kamu Sudah dapat Menggunakanku Sekarang.
Aksesmu Akan Kadaluarsa Besok, Kamu Harus Login Ulang Untuk Dapat Menggunakanku."""


# This will be show when an user send wrong password

      WRONG_PWD = """Maaf, Password Yang Anda masukan SALAH ⛔ , Coba Kembali dengan Password yang Benar."""


# This will appear if the user is already logged

      EXISTING_USER = "Kamu Telah Masuk, Silahkan Langsung Menggunakanku"

####################################################################################################################################################
####################################################################################################################################################


#DON'T CHANGE THE NUMBERS IN THE FLOWER BRACKETS AND THE ORDER OF PERCENTAGE, DONE, TOTAL, SPEED, ETA ONLY CHANGE THE THEME 

      PROGRESS = """
Persen : {0}%
Selesai ✅: {1}
Total 🌀: {2}
Kecepatan 🚀: {3}/s
Perkiraan Selesai 🕰: {4}
"""
       
      DOWNLOAD_PROGRESS = "▪️"
      UPLOAD_PROGRESS = "▫️"

####################################################################################################################################################
####################################################################################################################################################



      DOWNLOAD_START = "Sedang Mengunduh File 📥"
      DOWNLOAD_COMPLETE = "✅ File Telah Terunduh\nBersiap Mengunggah File"
      UPLOAD_START = "Sedang Mengunggah File 📤"
      UPLOAD_COMPLETE = "File Berhasil Diconvert, Terima Kasih"
      SAVED_CUSTOM_THUMB_NAIL = "Thumbnail Berhasil Disimpan, Thumbnail Otomatis Dihapus 24Jam Kemudian"
      BANNED_TEXT = "MAAF, KAMU TELAH TERBLOKIR. KAMU TIDAK DAPAT MENGGUNAKANKU LAGI"
      REPLY_TEXT = "Silahkan Reply Media yang Ingin Kamu Convert."
      DEL_ETED_CUSTOM_THUMB_NAIL = "Thumbnail Berhasil dihapus"
