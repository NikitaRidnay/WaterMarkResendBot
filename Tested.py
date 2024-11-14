import os
from telethon.sync import TelegramClient
from telethon import events
import cv2
import easyocr


api_id = 26287867
api_hash = '4cfb484a98155db1c4aa4219a902fef1'
phone_number = '+66633748702'


client = TelegramClient('gr', api_id, api_hash)
print('resend start')

"""_______________________CSA RU 6 with easyOCR IDs________________________"""

CSA_koztrade = -1001628242370
CSA_Crypto_angel = -1001510029302
CSA_Shaurma = -1001580655606
CSA_Chin3coin = -1001849567983
CSA_Covcheg = -1001867502579
CSA_BOOBA = -1001721294728

"""________________________NAPR RU 6 with easyOCR IDs________________________"""

NAPR_koztrade = -1002044661397
NAPR_Crypto_angel = -1001998771649
NAPR_Shaurma = -1002027549221
NAPR_Chin3coin = -1002073520039
NAPR_Covcheg = -1002125889781
NAPR_BOOBA = -1002004736781

"""__________________________CSA ENG 5 IDs_______________________"""

CSA_BITCIONMASTER = -1001507784071
CSA_BBBVIP = -1001706928301
CSA_125XFUTURES = -1001613936165
CSA_FEDRUSSIANS = -1001544399714
CSA_KIM = -1001705049019

"""__________________________NAPR ENG 5 IDs_______________________"""

NAPR_BITCOINMASTER = -1002085199265
NAPR_BBBVIP = -1002029579482
NAPR_125XFUTURES = -1002096242258
NAPR_FEDRUSSIANS = -1002121535491
NAPR_KIM = -1001881845269

"""test"""

ch1 = -1002139945414
ch2 = -1001947440269




trigger_words = ['@Crypto_Sliv_Alliance','@Crypto_Sliv_','@Crypto_Sliv_All','Sliv_Alliance', 'Sliv' , 'Alliance','@Crypto','T.ME/CRYPTOSHAURMA','CRYPTOSHAURMA']
replacement_text = '@dragonroes'

async def send_to_all(channel, message, media):
    await client.send_file(channel, 'censored_image_'+ media, caption=message)
    print('§')


def censor_and_replace_text(image_path, trigger_words, replacement_text):
    # инициализация OCR с помощью доступных языковых моделей
    reader = easyocr.Reader(['en'])
    replacement_text = '@dragonroes'

    # чтение изображения с помощью OCR
    result = reader.readtext(image_path)

    # инициализация cv2
    image = cv2.imread(image_path)
    
    # определение координат для прямоугольника
    rectangle_coords = None

    # получение размера и высоты альтернативного текста
    text_width, text_height = cv2.getTextSize(replacement_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

    # проход по результатам распознавания текста
    for detection in result:
        for word in trigger_words:
            if word in detection[1]:
                rectangle_coords = detection[0]
                print('нужный текст найден!')
                break
        if rectangle_coords is not None:
            break

    # рисование черного прямоугольника для закрытия текста и написание альтернативного текста на нем
    if rectangle_coords is not None:
        # увеличение длины прямоугольника
        cv2.rectangle(image, rectangle_coords[0], (rectangle_coords[2][0] + 90, rectangle_coords[2][1]), (0, 0, 0), -1)
        cv2.putText(image, replacement_text, (rectangle_coords[2][0] - 50, rectangle_coords[1][1] + text_height), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # сохранение изображения с изменениями
    cv2.imwrite('censored_image_' + image_path, image)
    return 'censored_image_' + image_path




"""Функции с пересылкой RU"""
@client.on(events.NewMessage(chats=ch1))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)
        await client.send_file(ch2, censored_media, caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        #os.remove(censored_media)
    elif event.text:
        await client.send_message(ch2, event.text)
        print('сообщение с текстом отправлено')









with client:
    client.start()
    client.run_until_disconnected()