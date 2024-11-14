import asyncio
import os
from telethon.sync import TelegramClient
from telethon import events
from telethon.tl.types import InputMessagesFilterPhotos

api_id = 26287867
api_hash = '4cfb484a98155db1c4aa4219a902fef1'
phone_number = '+66633748702'
source_channels = [-1001428567201, -1001622950490, -1001628242370, -1001510029302, -1001580655606]
destination_channels = [-1002034632023, -1002146721711,-1002044661397, -1001998771649, -1002027549221]

client = TelegramClient('resender_bot', api_id, api_hash)
print('resend start')


for source_channel, destination_channel in zip(source_channels, destination_channels):
    @client.on(events.NewMessage(chats=source_channel))
    async def handler(event):
        if event.message.media and not event.grouped_id:
            media = await event.message.download_media()
            await client.send_file(destination_channel, media, caption=event.message.text)
            print('сообщение с медиа отправлено')
            os.remove(media)
        elif event.text:
            await client.send_message(destination_channel, event.text)
            print('сообщение с текстом отправлено')

    @client.on(events.Album(chats=source_channel))
    async def handler(event):
        media_list = []
        ctext = event.text
        for photo in event.messages:
            media = await photo.download_media()
            media_list.append(media)
            await client.send_file(destination_channel, media_list, caption=ctext)
            print('сообщение с альбомом отправлено')
        for media in media_list:
            os.remove(media)
with client:
    client.start()
    client.run_until_disconnected()