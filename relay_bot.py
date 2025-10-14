import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# =======================
API_ID = 23716374
API_HASH = 'bca725880cba29c5dff697d093410ad5'

# جایگزین با رشته Session که گرفتیم
SESSION_STRING = '1BJWap1sBuzAJNsjALm2JUy7QJPAf5fd4QPyetxZyh5wxAsxbAWa5BlxIdJdFL0FKTmsCoVpvRLR4nj3N9hfBJFkv8I1d-p79bcGVjHgEkThDq036EXeW8dqd2J7z_BFUgmaa4_mF8r5SVHtatQnAd1vOK7HT-OXP2_f7H0wEZ5060EFxloHSl8H4RwGU-VxfhiX7YuwwGJPd4lCJyW7bmoDC8ZufHZLzKj9LPW-BlgUUtENUiqlpiaMlgSKXfP6tmPqvZ-Dzn4LMNTgxmia19i3hAvYAtYaxcttPWQnN3RDN9nhPfHMTUvSQa_dmqWCCZ1OBT0XCfSZWSzsT1q0jPzSPW_ZmKQw='

# کانال‌ها
CHANNEL_SRC = 'dana_news'
CHANNEL_DEST = 'dastavalkhabar'

REMOVE_TEXT = "🆔 @Dana_News"
ADD_TEXT = "💢@Dastavalkhabar"
# =======================

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    await client.start()
    print("✅ Bot is connected and ready.")

    @client.on(events.NewMessage(chats=CHANNEL_SRC))
    async def handler(event):
        message = event.message
        text = message.message or ""

        if REMOVE_TEXT in text:
            text = text.replace(REMOVE_TEXT, "")
        if ADD_TEXT not in text:
            text += f"\n\n{ADD_TEXT}"

        try:
            if message.media:
                await client.send_file(CHANNEL_DEST, message.media, caption=text)
            else:
                await client.send_message(CHANNEL_DEST, text)
            print(f"📨 Message forwarded: {text[:30]}...")
        except Exception as e:
            print(f"❌ Error sending message: {e}")

    await client.run_until_disconnected()

asyncio.run(main())
