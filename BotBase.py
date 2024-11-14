import asyncio
import os
from telethon.sync import TelegramClient
from telethon import events
from telethon.tl.types import InputMessagesFilterPhotos

api_id = 20506752
api_hash = '449c2333789c50ce129cca19cea2d815'
phone_number = '+6281360877482'
source_channels = -1002136163571
destination_channels = -1002124978488

client = TelegramClient('testovyi', api_id, api_hash)
print('resend start')

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await client.send_file(destination_channels, media, caption=event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
            
    elif event.text:
        await client.send_message(destination_channels, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=source_channels))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
    
    await send_to_all(destination_channels, ctext, media_list)
    print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

async def send_to_all(channel, message, media):
    await client.send_file(channel, media, caption=message)
    print('§')

with client:
    client.start()
    client.run_until_disconnected()