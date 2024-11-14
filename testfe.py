import os
from telethon.sync import TelegramClient
from telethon import events
import cv2
import easyocr
import numpy as np


api_id = 20506752
api_hash = '449c2333789c50ce129cca19cea2d815'
phone_number = '+6281360877482'

source = -1002139945414
dest = -1001947440269


client = TelegramClient('gr', api_id, api_hash)
print('скрипт запущен')




trigger_words = ['@Crypto_Sliv_Alliance','@Crypto_Sliv_','@Crypto_Sliv_All','Sliv_Alliance', 'Sliv' , 'Alliance','@Crypto','T.ME/CRYPTOSHAURMA','CRYPTOSHAURMA']


async def send_to_all(channel, message, media):
    await client.send_file(channel, media, caption=message)
    print('§')


def censor_and_replace_text(image_path, trigger_words):
    image = cv2.imread(image_path)
    result = [] # Assume result is a list of detected words, rectangles, and scores
    closure_image = cv2.imread('watermark.jpg', cv2.IMREAD_UNCHANGED) # Read image with alpha channel

    # Declare rectangle_coords before the for loop
    rectangle_coords = None

    for detection in result:
        for word in trigger_words:
            if word in detection[1]:
                rectangle_coords = detection[0]
                print('нужный текст найден!')
                break
        if rectangle_coords is not None:
            break

    if rectangle_coords is not None:
        # Crop the image using the rectangle coordinates
        cropped_image = image[rectangle_coords[0][1]:rectangle_coords[2][1], rectangle_coords[0][0]:rectangle_coords[2][0]]

        # Convert the cropped image to RGBA format
        cropped_rgba = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2BGRA)

        # Create a mask for the cropped image (255 for pixels where we want to keep the original image)
        mask = np.ones(cropped_rgba.shape, dtype=np.uint8) * 255

        # Resize the watermark to the size of the cropped image
        resize_closing_image = cv2.resize(closure_image, (cropped_rgba.shape[1], cropped_rgba.shape[0]))

        # Overlay the watermark onto the cropped image using the alpha channel
        alpha_s = resize_closing_image[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s
        for c in range(3):
            cropped_rgba[..., c] = (alpha_s * resize_closing_image[:, :, c] + alpha_l * cropped_rgba[..., c])

        # Overwrite the original image with the cropped, watermarked image
        image[rectangle_coords[0][1]:rectangle_coords[2][1], rectangle_coords[0][0]:rectangle_coords[2][0]] = cropped_rgba

    cv2.imwrite('censored_' + image_path, image)
    return 'censored_' + image_path


"""Функции с пересылкой RU"""
@client.on(events.NewMessage(chats=source))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words)
        await send_to_all(dest, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
       # os.remove(media)
       # os.remove(censored_media)
    elif event.text:
        await client.send_message(dest, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=source))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media,trigger_words)
        media_list.append(censored_media)
        await send_to_all(dest, ctext, media_list)
        print('сообщение с альбомом отправлено')
    #for media in media_list:
     #   os.remove(media)



with client:
    client.start()
    client.run_until_disconnected()