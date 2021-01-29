from telethon import TelegramClient, events, sync

# Remember to use your own values from my.telegram.org!
api_id = 2052818
api_hash = '4ca6f6edbe3d52c96538f26d1f335fd5'
client = TelegramClient('bruno pizol', api_id, api_hash)

@client.on(events.NewMessage(chats='teste 1'))
async def my_event_handler(event):
    print(event.raw_text)


client.start()
client.run_until_disconnected()
