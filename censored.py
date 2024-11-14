import os
from telethon.sync import TelegramClient
from telethon import events
import cv2
import easyocr


api_id = 20506752
api_hash = '449c2333789c50ce129cca19cea2d815'
phone_number = '+6281360877482'


client = TelegramClient('easyOcr_bot', api_id, api_hash)
print('resend start')

"""_______________________CSA RU 6 with easyOCR IDs________________________"""

CSA_koztrade = -1001628242370
CSA_Crypto_angel = -1001387647574
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
CSA_FINWHALE = -1001561496039
CSA_GREENCRYPTO = -1001968388327
CSA_ALEX_FRIEDMAN = -1001564901166
CSA_ROSE_PREMUIM = -1001160434165

"""__________________________NAPR ENG 5 IDs_______________________"""

NAPR_BITCOINMASTER = -1002085199265
NAPR_BBBVIP = -1002029579482
NAPR_125XFUTURES = -1002096242258
NAPR_FEDRUSSIANS = -1002121535491
NAPR_KIM = -1001881845269
NAPR_FINWHALE = -1001441974157
NAPR_GREENCRYPTO = -1002140948929
NAPR_ALEX_FRIEDMAN = -1002027397880
NAPR_ROSE_PREMUIM = -1001958728765

#CSA’s
CSA_BEEF_TREND = -1001822321947
CSA_BulletPremuim = -1001422684746
CSA_GreenCryptoIndicator = -1002013564333
CSA_DENMARKSNIPERS = -1002074852942
CSA_UPTRADE = -1001622700441
CSA_ALWAYSWIN = -1001451568767
CSA_CryptoCove = -1001281659816
CSA_MMarket = -1001383621606
CSA_125xOutlook = -1001756807263
CSA_KLONDIKE = -1001315751749
CSA_CryptoInnerCircle = -1001869920869
CSA_BULLSFAMILY = -1001618031235
CSA_ALANMASTERS = -1001174157412
CSA_PURSUIT4million = -1001174157412

#Naprs’s

NAPR_BEEFTREND = -1002004736781
NAPR_BulletPremuim = -1001998771649
NAPR_GreenCryptoindicator = -1002051274016
NAPR_DenmarkSnipers = -1002073520039
NAPR_UPTRADE = -1002104178548
NAPR_ALWAYSWIN = -1002107528667
NAPR_CryptoCove = -1002027549221
NAPR_MMarker = -1002037341427
NAPR_125xOutlook = -1002092871612
NAPR_Klondike = -1002142083804
NAPR_CryptoInner = -1002018651424
NAPR_BullsFamily = -1002001000081
NAPR_ALANMASTERS = -1002067861525
NAPR_Pursuit4million = -1002034632023





trigger_words = ['@Crypto_Sliv_Alliance','@Crypto_Sliv_','@Crypto_Sliv_All','Sliv_Alliance', 'Sliv' , 'Alliance','@Crypto','T.ME/CRYPTOSHAURMA','CRYPTOSHAURMA']
replacement_text = '@dragonroes'



def censor_and_replace_text(image_path, trigger_words, replacement_text):
    reader = easyocr.Reader(['en'])
    replacement_text = '@dragonroes'

    result = reader.readtext(image_path)

    image = cv2.imread(image_path)
    
    rectangle_coords = None

    text_width, text_height = cv2.getTextSize(replacement_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

    for detection in result:
        for word in trigger_words:
            if word in detection[1]:
                rectangle_coords = detection[0]
                print('нужный текст найден!')
                break
        if rectangle_coords is not None:
            break

    if rectangle_coords is not None:
        cv2.rectangle(image, rectangle_coords[0], (rectangle_coords[2][0] + 90, rectangle_coords[2][1]), (0, 0, 0), -1)
        cv2.putText(image, replacement_text, (rectangle_coords[0][0] - 50, rectangle_coords[1][1] + text_height), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imwrite('censored_image_' + image_path, image)
    return 'censored_image_' + image_path








@client.on(events.NewMessage(chats=CSA_Chin3coin))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_Chin3coin,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_Chin3coin, event.text)
        print('сообщение с текстом отправлено')


@client.on(events.NewMessage(chats=CSA_BITCIONMASTER))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_BITCOINMASTER,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_BITCOINMASTER, event.text)
        print('сообщение с текстом отправлено')


@client.on(events.NewMessage(chats=CSA_FINWHALE))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_FINWHALE,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_FINWHALE, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_GREENCRYPTO))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_GREENCRYPTO,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_GREENCRYPTO, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_BBBVIP))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_BBBVIP,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_BBBVIP, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_ALEX_FRIEDMAN))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_ALEX_FRIEDMAN,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(CSA_ALEX_FRIEDMAN, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_ROSE_PREMUIM))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_ROSE_PREMUIM,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_ROSE_PREMUIM, event.text)
        print('сообщение с текстом отправлено')


@client.on(events.NewMessage(chats=CSA_BEEF_TREND))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_BEEFTREND,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_BEEFTREND, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_BulletPremuim))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_BulletPremuim,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_BulletPremuim, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_GreenCryptoIndicator))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_GreenCryptoindicator,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_GreenCryptoindicator, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_DENMARKSNIPERS))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_DenmarkSnipers,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_DenmarkSnipers, event.text)
        print('сообщение с текстом отправлено')


@client.on(events.NewMessage(chats=CSA_UPTRADE))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_UPTRADE,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_UPTRADE, event.text)
        print('сообщение с текстом отправлено')


@client.on(events.NewMessage(chats=CSA_ALWAYSWIN))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_ALWAYSWIN,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_ALWAYSWIN, event.text)
        print('сообщение с текстом отправлено')


@client.on(events.NewMessage(chats=CSA_CryptoCove))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_CryptoCove,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_CryptoCove, event.text)
        print('сообщение с текстом отправлено')


@client.on(events.NewMessage(chats=CSA_MMarket))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_MMarker,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_MMarker, event.text)
        print('сообщение с текстом отправлено')


@client.on(events.NewMessage(chats=CSA_125xOutlook))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_125xOutlook,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_125xOutlook, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_KLONDIKE))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_Klondike,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_Klondike, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_CryptoInnerCircle))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_CryptoInner,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_CryptoInner, event.text)
        print('сообщение с текстом отправлено')


@client.on(events.NewMessage(chats=CSA_BULLSFAMILY))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_BullsFamily,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_BullsFamily, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_ALANMASTERS))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_ALANMASTERS,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_ALANMASTERS, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_PURSUIT4million))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_Pursuit4million,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_Pursuit4million, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_FEDRUSSIANS))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_FEDRUSSIANS,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_FEDRUSSIANS, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.NewMessage(chats=CSA_Crypto_angel))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        censored_media = censor_and_replace_text(media,trigger_words,replacement_text)

        await client.send_file(NAPR_Crypto_angel,censored_media,caption = event.message.text)
        print('сообщение с медиа отправлено')
        os.remove(media)
        os.remove(censored_media)
    elif event.text:
        await client.send_message(NAPR_Crypto_angel, event.text)
        print('сообщение с текстом отправлено')

with client:
    client.start()
    client.run_until_disconnected()