from pyrogram import Client
from pyrogram.raw import functions
from time import sleep

api_id = '10356241' #my.telegram.org,dan olgan api_id yozing.

api_hash = "fbea11b5323c324387089425cda209b9" # my.telegram.org,dan olgan api_hash yozing.

a =  Client("test",api_id,api_hash)
a.start()
@a.on_message()
def _(c,m):
 a.read_history(m.chat.id)
while True:
 a.send(functions.account.UpdateStatus(offline=False))
 sleep(0.1)
