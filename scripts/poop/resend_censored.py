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

csa_koztrade = -1001628242370
napr_koztrade = -1002044661397
    


client = TelegramClient('MyGrab', api_id, api_hash)
print('resend start')



async def send_to_all(channel, message):
    await client.send_message(channel, message)
    print('§')


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

@client.on(events.NewMessage(chats=csa_koztrade))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await client.send_file(napr_koztrade, media, caption=event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await send_to_all(napr_koztrade, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=csa_koztrade))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(media)
        await client.send_file(napr_koztrade, media_list, caption=ctext)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)






with client:
    client.start()
    client.run_until_disconnected()