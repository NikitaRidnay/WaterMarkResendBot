import os
from telethon.sync import TelegramClient
from telethon import events


api_id = 26287867
api_hash = '4cfb484a98155db1c4aa4219a902fef1'
phone_number = '+66633748702'


client = TelegramClient('resender_bot', api_id, api_hash)
print('resend start')

"""_______________________CSA RU 6 IDs________________________"""

CSA_Pursuit4million = -1001428567201
CSA_SLEZI = -1001622950490
CSA_sytyiHomyak = -1001820914075
CSA_Pentagon = -1002137790695
CSA_UpTrade = -1001622700441
CSA_MMArket = -1001383621606

"""________________________NAPR RU 6 IDs________________________"""

NAPR_Pursuit4million = -1002034632023
NAPR_SLEZI = -1002146721711
NAPR_sytyiHomyak = -1002051274016
NAPR_Pentagon = -1002018651424
NAPR_UpTrade = -1002104178548
NAPR_MMArket = -1002037341427

"""__________________________CSA ENG 8 IDs_______________________"""

CSA_ALEXFRIDMAN = -1001564901166
CSA_ALANMASTERS = -1001174157412
CSA_ROSEPREMIUM = -1001160434165
CSA_FINWHALE = -1001561496039
CSA_ALWAYSWINTRADES = -1001451568767
CSA_GREEN_CRYPTO = -1001968388327
CSA_KLONDIKE = -1001315751749
CSA_125X_OUTLOOK = -1001756807263

"""__________________________NAPR ENG 8 IDs_______________________"""

NAPR_ALEFFRIDMAN = -1002027397880
NAPR_ALANMASTERS = -1002067861525
NAPR_ROSEPREMIUM = -1001958728765
NAPR_FINWHALE = -1001441974157
NAPR_ALWAYSWINTRADES = -1002107528667
NAPR_GREEN_CRYPTO = -1002140948929
NAPR_KLONDIKE = -1002142083804
NAPR_125X_OUTLOOK = -1002092871612






async def send_to_all(channel, message, media):
    await client.send_file(channel, media, caption=message)
    print('§')





"""Функции с пересылкой RU"""





    

@client.on(events.NewMessage(chats=CSA_MMArket))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_MMArket, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_MMArket, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_MMArket))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_MMArket, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_Pentagon))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_Pentagon, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif client.send_message:
        await send_to_all(NAPR_Pentagon, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_Pentagon))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_Pentagon, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


@client.on(events.NewMessage(chats=CSA_Pursuit4million))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_Pursuit4million, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)

    elif event.text:
        await client.send_message(NAPR_Pursuit4million, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_Pursuit4million))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_Pursuit4million, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)



@client.on(events.NewMessage(chats=CSA_sytyiHomyak))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_sytyiHomyak, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_sytyiHomyak, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_sytyiHomyak))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_sytyiHomyak, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_UpTrade))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_UpTrade, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_UpTrade, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_UpTrade))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_UpTrade, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)




@client.on(events.NewMessage(chats=CSA_SLEZI))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_SLEZI, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_SLEZI, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_SLEZI))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_SLEZI, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)



"""Функции с пересылкой ENG"""




@client.on(events.NewMessage(chats=CSA_ALEXFRIDMAN))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_ALEFFRIDMAN, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_ALEFFRIDMAN, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_ALEXFRIDMAN))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_ALEFFRIDMAN, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)



@client.on(events.NewMessage(chats=CSA_ALANMASTERS))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_ALANMASTERS, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_ALANMASTERS, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_ALANMASTERS))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_ALANMASTERS, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_ROSEPREMIUM))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_ROSEPREMIUM, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_ROSEPREMIUM, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_ROSEPREMIUM))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_ROSEPREMIUM, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)




@client.on(events.NewMessage(chats=CSA_FINWHALE))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_FINWHALE, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_FINWHALE, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_FINWHALE))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_FINWHALE, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

@client.on(events.NewMessage(chats=CSA_ALWAYSWINTRADES))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_ALWAYSWINTRADES, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_ALWAYSWINTRADES, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_ALWAYSWINTRADES))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_ALWAYSWINTRADES, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)




@client.on(events.NewMessage(chats=CSA_GREEN_CRYPTO))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_GREEN_CRYPTO, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_GREEN_CRYPTO, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_GREEN_CRYPTO))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_GREEN_CRYPTO, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)


@client.on(events.NewMessage(chats=CSA_KLONDIKE))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_KLONDIKE, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_KLONDIKE, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_KLONDIKE))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_KLONDIKE, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)





@client.on(events.NewMessage(chats=CSA_125X_OUTLOOK))
async def handler(event):
    if event.message.media and not event.grouped_id:
        media = await event.message.download_media()
        await send_to_all(NAPR_125X_OUTLOOK, event.message.text, media)
        print('сообщение с медиа отправлено')
        os.remove(media)
    elif event.text:
        await client.send_message(NAPR_125X_OUTLOOK, event.text)
        print('сообщение с текстом отправлено')

@client.on(events.Album(chats=CSA_125X_OUTLOOK))
async def handler(event):
    media_list = []
    ctext = event.text
    for photo in event.messages:
        media = await photo.download_media()
        media_list.append(media)
        await send_to_all(NAPR_125X_OUTLOOK, ctext, media_list)
        print('сообщение с альбомом отправлено')
    for media in media_list:
        os.remove(media)

with client:
    client.start()
    client.run_until_disconnected()