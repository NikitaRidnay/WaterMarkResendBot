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


client = TelegramClient('resender_bot', api_id, api_hash)
print('resend start')

"""_______________________CSA RU 12 IDs________________________"""

CSA_Pursuit4million = -1001428567201
CSA_SLEZI = -1001622950490
CSA_koztrade = -1001628242370
CSA_Crypto_angel = -1001510029302
CSA_Shaurma = -1001580655606
CSA_sytyiHomyak = -1001820914075
CSA_Pentagon = -1002137790695
CSA_UpTrade = -1001622700441
CSA_Chin3coin = -1001849567983
CSA_Covcheg = -1001867502579
CSA_BOOBA = -1001721294728
CSA_MMArket = -1001383621606

"""________________________NAPR RU 12 IDs________________________"""

NAPR_Pursuit4million = -1002034632023
NAPR_SLEZI = -1002146721711
NAPR_koztrade = -1002044661397
NAPR_Crypto_angel = -1001998771649
NAPR_Shaurma = -1002027549221
NAPR_sytyiHomyak = -1002051274016
NAPR_Pentagon = -1002018651424
NAPR_UpTrade = -1002104178548
NAPR_Chin3coin = -1002073520039
NAPR_Covcheg = -1002125889781
NAPR_BOOBA = -1002004736781
NAPR_MMArket = -1002037341427

"""__________________________CSA ENG 13 IDs_______________________"""

CSA_BITCIONMASTER = -1001507784071
CSA_ALEXFRIDMAN = -1001564901166
CSA_BBBVIP = -1001706928301
CSA_ALANMASTERS = -1001174157412
CSA_ROSEPREMIUM = -1001160434165
CSA_125XFUTURES = -1001613936165
CSA_FINWHALE = -1001561496039
CSA_ALWAYSWINTRADES = -1001451568767
CSA_FEDRUSSIANS = -1001544399714
CSA_GREEN_CRYPTO = -1001968388327
CSA_KLONDIKE = -1001315751749
CSA_KIM = -1001705049019
CSA_125X_OUTLOOK = -1001756807263

"""__________________________NAPR ENG 13 IDs_______________________"""

NAPR_BITCOINMASTER = -1002085199265
NAPR_ALEFFRIDMAN = -1002027397880
NAPR_BBBVIP = -1002029579482
NAPR_ALANMASTERS = -1002067861525
NAPR_ROSEPREMIUM = -1001958728765
NAPR_125XFUTURES = -1002096242258
NAPR_FINWHALE = -1001441974157
NAPR_ALWAYSWINTRADES = -1002107528667
NAPR_FEDRUSSIANS = -1002121535491
NAPR_GREEN_CRYPTO = -1002140948929
NAPR_KLONDIKE = -1002142083804
NAPR_KIM = -1001881845269
NAPR_125X_OUTLOOK = -1002092871612






async def send_to_all(channel, message, media):
    await client.send_file(channel, media, caption=message)
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
    return 'censored_' + image_path


"""Функции с пересылкой RU"""
@client.on(events.NewMessage(chats=CSA_koztrade))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_koztrade, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_koztrade, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_koztrade))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_koztrade, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_Chin3coin))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_Chin3coin, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_Chin3coin, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_Chin3coin))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_Chin3coin, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_Covcheg))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_Covcheg, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_Covcheg, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_Covcheg))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_Covcheg, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)
    
@client.on(events.NewMessage(chats=CSA_Crypto_angel))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_Crypto_angel, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_Crypto_angel, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_Crypto_angel))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_Crypto_angel, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)
@client.on(events.NewMessage(chats=CSA_MMArket))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_MMArket, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_MMArket, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_MMArket))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_MMArket, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_Pentagon))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_Pentagon, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_Pentagon, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_Pentagon))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_Pentagon, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


@client.on(events.NewMessage(chats=CSA_Pursuit4million))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_Pursuit4million, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_Pursuit4million, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_Pursuit4million))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_Pursuit4million, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_Shaurma))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_Shaurma, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_Shaurma, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_Shaurma))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_Shaurma, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


@client.on(events.NewMessage(chats=CSA_sytyiHomyak))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_sytyiHomyak, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_sytyiHomyak, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_sytyiHomyak))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_sytyiHomyak, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_UpTrade))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_UpTrade, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_UpTrade, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_UpTrade))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_UpTrade, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_BOOBA))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_BOOBA, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_BOOBA, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_BOOBA))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_BOOBA, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


@client.on(events.NewMessage(chats=CSA_SLEZI))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_SLEZI, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_SLEZI, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_SLEZI))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_SLEZI, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)



"""Функции с пересылкой ENG"""


@client.on(events.NewMessage(chats=CSA_BITCIONMASTER))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_BITCOINMASTER, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_BITCOINMASTER, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_BITCIONMASTER))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_BITCOINMASTER, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_ALEXFRIDMAN))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_ALEFFRIDMAN, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_ALEFFRIDMAN, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_ALEXFRIDMAN))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_ALEFFRIDMAN, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_BBBVIP))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_BBBVIP, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_BBBVIP, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_BBBVIP))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_BBBVIP, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_ALANMASTERS))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_ALANMASTERS, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_ALANMASTERS, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_ALANMASTERS))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_ALANMASTERS, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_ROSEPREMIUM))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_ROSEPREMIUM, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_ROSEPREMIUM, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_ROSEPREMIUM))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_ROSEPREMIUM, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


@client.on(events.NewMessage(chats=CSA_125XFUTURES))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_125XFUTURES, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_125XFUTURES, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_125XFUTURES))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_125XFUTURES, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_FINWHALE))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_FINWHALE, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_FINWHALE, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_FINWHALE))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_FINWHALE, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_ALWAYSWINTRADES))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_ALWAYSWINTRADES, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_ALWAYSWINTRADES, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_ALWAYSWINTRADES))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_ALWAYSWINTRADES, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_FEDRUSSIANS))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_FEDRUSSIANS, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_FEDRUSSIANS, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_FEDRUSSIANS))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_FEDRUSSIANS, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


@client.on(events.NewMessage(chats=CSA_GREEN_CRYPTO))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_GREEN_CRYPTO, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_GREEN_CRYPTO, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_GREEN_CRYPTO))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_GREEN_CRYPTO, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


@client.on(events.NewMessage(chats=CSA_KLONDIKE))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_KLONDIKE, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_KLONDIKE, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_KLONDIKE))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_KLONDIKE, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


@client.on(events.NewMessage(chats=CSA_KIM))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_KIM, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_KIM, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_KIM))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_KIM, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


@client.on(events.NewMessage(chats=CSA_125X_OUTLOOK))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        await send_to_all(NAPR_125X_OUTLOOK, event.message.text, censored_media)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await send_to_all(NAPR_125X_OUTLOOK, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_125X_OUTLOOK))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        censored_media = censor_and_replace_text(media, '@Crypto_Sliv_Alliance', '@dragonroes')
        media_list.append(censored_media)
        await send_to_all(NAPR_125X_OUTLOOK, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

with client:
    client.start()
    client.run_until_disconnected()