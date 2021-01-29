from telethon import TelegramClient, events, sync

# Remember to use your own values from my.telegram.org!
api_id = 2052818
api_hash = '4ca6f6edbe3d52c96538f26d1f335fd5'
client = TelegramClient('bruno pizol', api_id, api_hash)
def get_messages():
    #for message in client.iter_messages('teste 1'):
    teste = client.iter_messages('teste 1',limit=1,reverse=True)
    #photos = client.get_messages('teste 1', 0)
    print(teste.text)
    #print(message.sender.username, message.text)
    if not teste.media == False:
        print("receive image")
        #client.iter_messages('teste 1')[-1].download_media(client.iter_messages('teste 1')[-1].media, "E:\TelegramBOT\Tips")



@client.on(events.NewMessage(chats='teste 1'))
async def my_event_handler(event):
    async for message in client.iter_messages('teste 1',reverse=False):
        if event.photo:
            #await client.send_message("teste 2", "", message)
            await client.send_file('teste 2', message.photo)
            print("receive photo")
        await client.send_message('teste 2', message.text)
        print(message.text)
        break




client.start()
client.run_until_disconnected()