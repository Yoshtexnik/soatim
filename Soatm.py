from telethon.sync import TelegramClient, events
from config import *
from tqdm import tqdm
from telethon.tl.functions.account import UpdateProfileRequest 
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
import os, random
from time import *

client = TelegramClient("Soat", api_id, api_hash)
client.start()

with client:    
    messages = client.get_messages('t.me/belial_black_foto', limit=1000)
    for msg in tqdm(messages):
        msg.download_media(file=os.path.join('media', f'{random.randint(1, 8000)}'))
    print('started')
    while True:    
        n = random.choice(os.listdir('media'))
        file = client.upload_file(f'media/{n}')
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        client(UploadProfilePhotoRequest(file))
        sleep(10)

input()
