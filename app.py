import asyncio
from pyrogram import Client,filters
from credentials import bot_token, bot_user_name,API_HASH,APP_ID,TOOLSDIR,WDIR,igu,igp,channelID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,InputMediaPhoto, InputMediaVideo
# import requests
import os
import time

app = Client(
    "BulkigBOT",
    bot_token=bot_token,
    api_id=APP_ID,
    api_hash=API_HASH,

)
channelID=int(channelID)
# async def exec(username):
#
#     return


@app.on_message(filters.command(["start"]))
def start(client, message):
    client.send_message(chat_id=channelID,
                        text="Hi")

@app.on_message(filters.command(["some"]))
async def start(client, message):
    client.send_message(chat_id=channelID,
                        text="Hi")
    arr = os.listdir("./incessantloops")
    await client.send_document(
        chat_id=message.chat.id,
        document="./incessantloops/"+arr[2]
    )


@app.on_message(filters.text)
async def getUname(client,message):
    uname=message.text
    direc="./{}".format(uname)

    print(message.chat.id,":",type(message.chat.id),"\n",channelID,":",type(channelID))
    command_to_exec = [
        "python","scrap.py",
        uname, "-u", igu, "-p", igp
    ]
    print(os.listdir())
    print(" ".join(command_to_exec))
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,

        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()

    s = open("{}.txt".format(uname), "r")
    media_group = []

    while True:

        # Get next line from file
        line = s.readline()
        if '.jpg?' in line:
            if len(media_group)>10:
                media_group.clear()

            else:
                media_group.append(InputMediaPhoto(line))

        elif '.mp4' in line:
            try:
                await client.send_video(message.chat.id, list)
            except:
                await client.send_document(message.chat.id, list)
            time.sleep(1)


        if len(media_group)>0:
            await client.send_media_group(
                message.chat.id,

                media_group
            )

            time.sleep(20)
        # if line is empty
        # end of file is reached

        if not line:
            break
        print(line)
    os.remove("{}.txt".format(uname))
    print("ALL DONE")


def sortType(direc,arr):
    re_arr=[]
    for media in arr:
        if media.split(".")[-1]=='jpg':
            re_arr.append(InputMediaPhoto("{}/{}".format(direc,media)))

        # elif media.split(".")[-1] == 'mp4':
        #     re_arr.append(InputMediaVideo("{}/{}".format(direc, media)))
    return re_arr

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]






if __name__ == "__main__":
    app.run()

