import os
import asyncio
from telethon import TelegramClient, events

# =======================
# ⚡ تنظیمات خودتان
API_ID = 23716374
API_HASH = 'bca725880cba29c5dff697d093410ad5'
PHONE = '+989213013798'  # شماره تلگرام شما با +98
SESSION_NAME = 'relay_session'

CHANNEL_SRC = 'dana_news'           # کانال مبدا بدون t.me/
CHANNEL_DEST = 'dastavalkhabar'    # کانال مقصد بدون t.me/

REMOVE_TEXT = "🆔 @Dana_News"
ADD_TEXT = "💢@Dastavalkhabar"
# =======================

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    # خواندن کد تایید از متغیر محیطی
    code = os.getenv('TELEGRAM_CODE')

    if not code:
        print("کد تایید از متغیر محیطی در دسترس نیست.")
        return
    
    # شروع ارتباط با تلگرام
    await client.start(PHONE, code_callback=lambda: code)
    print("✅ ربات متصل شد و آماده دریافت پیام‌هاست.")

    @client.on(events.NewMessage(chats=CHANNEL_SRC))
    async def handler(event):
        message = event.message
        text = message.message or ""

        # حذف متن مبدا و اضافه کردن متن مقصد
        if REMOVE_TEXT in text:
            text = text.replace(REMOVE_TEXT, "")
        if ADD_TEXT not in text:
            text += f"\n\n{ADD_TEXT}"

        try:
            if message.media:
                await client.send_file(CHANNEL_DEST, message.media, caption=text)
            else:
                await client.send_message(CHANNEL_DEST, text)
            print(f"📨 پیام منتقل شد: {text[:30]}...")
        except Exception as e:
            print(f"❌ خطا در ارسال پیام: {e}")

    await client.run_until_disconnected()

# اجرا
asyncio.run(main())
