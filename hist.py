import itertools
import sys
from telethon import errors
from telethon.sync import TelegramClient
from telethon.tl.patched import MessageService
import logging

api_id = 20617044
api_hash = 'a20ad77c843d5e8b03e9b0e2a1bbbe6c'

client = TelegramClient('resendqw213', api_id, api_hash)

client.start()

dialogs = client.get_dialogs()

source_chat_id = -1001432477212#источник
target_chat_id = 6191584137#куда пересылать

for dialog in dialogs:
    if dialog.id == source_chat_id:
        messages = client.get_messages(dialog, limit=None)
        for message in messages:
            if isinstance(message, MessageService):
                continue
            try:
                client.forward_messages(target_chat_id, message)
                print('Сообщение отправлено')
            except errors.FloodWaitError as e:
                print('Flood for',e.seconds)
                
client.disconnect()
