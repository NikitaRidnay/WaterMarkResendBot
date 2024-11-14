import asyncio
import os
from telethon.sync import TelegramClient
from telethon import events
from telethon.tl.types import InputMessagesFilterPhotos
import cv2
import easyocr

api_id = 26287867
api_hash = '4cfb484a98155db1c4aa4219a902fef1'
phone_number = '+66633748702'
#source_channels = [-1001428567201, -1001622950490, -1001628242370, -1001510029302, -1001580655606]
#destination_channels = [-1002034632023, -1002146721711,-1002044661397, -1001998771649, -1002027549221]
csa_pursuit4 = -1001428567201
napr_pursuit4 = -1002034632023
csa_slezi = -1001622950490
napr_slezi = -1002146721711
csa_koztrade = -1001628242370
napr_koztrade = -1002044661397
csa_angel = -1001510029302
napr_angel = -1001998771649
csa_shaurma = -1001580655606
napr_shaurma = -1002027549221

client = TelegramClient('resender_bot', api_id, api_hash)
print('resend start')

def censor_and_replace_text(image_path, text_to_replace, replacement_text):
    reader = easyocr.Reader(['en'])
    replacement_text='@dragonroes'
    text_to_replace='@Crypto_Sliv_Alliance'
    result = reader.readtext(image_path)
    image = cv2.imread(image_path)
    rectangle_coords = None
    text_width, text_height = cv2.getTextSize(replacement_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

    for detection in result:
        if text_to_replace in detection[1]:
            rectangle_coords = detection[0]
            break

    if rectangle_coords is not None:
        cv2.rectangle(image, rectangle_coords[0], rectangle_coords[2], (0, 0, 0), -1)
        cv2.putText(image, replacement_text, (rectangle_coords[0][0], rectangle_coords[0][1] + text_height), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imwrite('censored_' + image_path, image)



@client.on(events.NewMessage(chats=csa_pursuit4))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await client.send_file(napr_pursuit4, media, caption=event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(napr_pursuit4, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=csa_pursuit4))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await client.send_file(napr_pursuit4, media_list, caption=ctext)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=csa_slezi))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await client.send_file(napr_slezi, media, caption=event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(napr_slezi, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=csa_slezi))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await client.send_file(napr_slezi, media_list, caption=ctext)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=csa_koztrade))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await client.send_file(napr_koztrade, media, caption=event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(napr_koztrade, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=csa_koztrade))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await client.send_file(napr_koztrade, media_list, caption=ctext)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=csa_angel))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await client.send_file(napr_angel, media, caption=event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(napr_angel, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=csa_angel))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await client.send_file(napr_angel, media_list, caption=ctext)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=csa_shaurma))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await client.send_file(napr_shaurma, media, caption=event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(napr_shaurma, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=csa_shaurma))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await client.send_file(napr_shaurma, media_list, caption=ctext)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


with client:
    client.start()
    client.run_until_disconnected()