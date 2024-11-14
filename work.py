import asyncio
import os
import re
from telethon.sync import TelegramClient
from telethon import events
from telethon.tl.types import InputMessagesFilterPhotos


api_id = 20506752
api_hash = '449c2333789c50ce129cca19cea2d815'
phone_number = '+6281360877482'
source_channel = -1001736456026
destination_channel = -1001559500009_59





client = TelegramClient('anon', api_id, api_hash)
print('resend start')


def remove_hashtags(text):
    return re.sub(r'\#\w*', '', text)
    

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    if event.message.media and not event.grouped_id:
        async for message in client.iter_messages(source_channel, limit=1):
            media = await message.download_media()
            text = remove_hashtags(message.text)
            await client.send_file(destination_channel, media, caption=text)
            os.remove(media)
    elif event.text:
        async for message in client.iter_messages(source_channel, limit=1):
            mess = remove_hashtags(message.text)
            await client.send_message(destination_channel, mess)

@client.on(events.Album(chats=source_channel))
async def handler(event):
    album = await client.get_messages(source_channel, ids=event.messages)
    media_list = []
    ctext = remove_hashtags(event.text)
    for photo in album:
        media = await photo.download_media()
        media_list.append(media)
        await client.send_file(destination_channel, media_list, caption=ctext)
    for media in media_list:
        os.remove(media)

with client:
    client.start()
    client.run_until_disconnected()


