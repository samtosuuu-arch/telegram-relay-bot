import asyncio
import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# =======================
# ⚡ گرفتن مقادیر از Secrets
API_ID = int(os.environ.get("TELEGRAM_API_ID"))
API_HASH = os.environ.get("TELEGRAM_API_HASH")
SESSION_STRING = os.environ.get("TELEGRAM_SESSION_STRING")

# کانال مبدا
CHANNEL_SRC = 'dana_news'

# لیست کانال‌های مقصد (شناسه و لینک)
channel_ids = [
    '-1001293990413', '-1002303168889', '-1002016974877',
    '-1002295560799', '-1002104900802', '-1002005207697',
    '-1002120965536', '-1002135081737', '-1002176340230',
    '-1002384702556', '-1002442815941', '-1003164391143'
]

channel_links = [
    '💢@Dastavalkhabar', '💢@Ravayatno_ir', '✅@Sobheiranian',
    '✅@Rrouydadnu', '🆔@Tabriztopkhabar', '🆔@Sobhe_mashhad',
    '🆔@Nesfeh_jahaan', '🆔@Asre_shiraz', '✅@Reisjomhor',
    '✅@Asriranno', '✅@Akhbarjanjaly', '🅾️@eghtesadedovom'
]

REMOVE_TEXT = "🆔 @Dana_News"

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    await client.start()
    print("✅ ربات متصل شد و آماده انتقال پیام‌هاست.")

    @client.on(events.NewMessage(chats=CHANNEL_SRC))
    async def handler(event):
        message = event.message
        text = message.message or ""

        # حذف متن مبدا
        if REMOVE_TEXT in text:
            text = text.replace(REMOVE_TEXT, "")

        # ارسال پیام به همه کانال‌های مقصد
        for dest_id, dest_link in zip(channel_ids, channel_links):
            final_text = text
            if dest_link not in final_text:
                final_text += f"\n\n{dest_link}"

            try:
                if message.media:
                    await client.send_file(dest_id, message.media, caption=final_text)
                else:
                    await client.send_message(dest_id, final_text)
                print(f"📨 پیام منتقل شد به {dest_link}: {final_text[:30]}...")
            except Exception as e:
                print(f"❌ خطا در ارسال پیام به {dest_link}: {e}")

    await client.run_until_disconnected()

# اجرا
asyncio.run(main())
