import asyncio
import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# گرفتن مقادیر از Secrets
API_ID = int(os.environ.get("TELEGRAM_API_ID"))
API_HASH = os.environ.get("TELEGRAM_API_HASH"))
SESSION_STRING = os.environ.get("TELEGRAM_SESSION_STRING"))

CHANNEL_SRC = 'dana_news'           # کانال مبدا بدون t.me/
CHANNEL_DEST = 'dastavalkhabar'    # کانال مقصد بدون t.me/

REMOVE_TEXT = "🆔 @Dana_News"
ADD_TEXT = "💢@Dastavalkhabar"

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    await client.start()
    print("✅ ربات متصل شد و آماده انتقال پیام‌هاست.")

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

asyncio.run(main())
