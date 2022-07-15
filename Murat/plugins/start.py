from Murat import Murat
from telethon import events, Button

@Murat.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello! Welcome To Music Bot Based On Telethon,credit- Boo",
                    buttons=[
                        [Button.url("⚙️Support", url="https://t.me/kaalxsupport")],
                        [Button.url("🤖Repo", url="https://github.com/kaal0408/Telethon-Music")],
                    ])
