from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import yt_dlp
import os

TOKEN = "7169247074:AAFHNBYpysU9WroZVHFTK4nYz7UTt81BW3A"
async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    await update.message.reply_text("جاري التحميل...")

    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'video.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await update.message.reply_video(video=open(filename, 'rb'))

        os.remove(filename)

    except Exception as e:
        await update.message.reply_text(str(e))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

print("Bot Started")

app.run_polling(timeout=60)
TOKEN = "7169247074:AAFHNBYpysU9WroZVHFTK4nYz7UTt81BW3A"