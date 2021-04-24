import asyncio
from pyrogram import Client,filters
from credentials import bot_token, bot_user_name,API_HASH,APP_ID,TOOLSDIR,WDIR,igu,igp,channelID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,InputMediaPhoto, InputMediaVideo
# import requests
import os

app = Client(
    "BulkigBOT",
    bot_token=bot_token,
    api_id=APP_ID,
    api_hash=API_HASH,

)
async def exec(username):
    command_to_exec = [
        "instagram-scraper",
        username,"-u",igu,"-p",igp
    ]
    print(" ".join(command_to_exec))
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,

        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    # logger.info(e_response)
    t_response = stdout.decode().strip()
    return


@app.on_message(filters.command(["start"]))
def start(client, message):
    client.send_message(chat_id=channelID,
                        text="Hi")


@app.on_message(filters.text)
async def getUname(client,message):
    uname=message.text
    direc="./{}".format(uname)
    await (exec(uname))
    arr = os.listdir(direc)
    print(arr)
    media_arr=sortType(direc,arr)
    for medialist in media_arr:
        await client.send_media_group(
            channelID,
            medialist
        )


def sortType(direc,arr):
    re_arr=[]
    for media in arr:
        if media.split(".")[-1]=='jpg':
            re_arr.append(InputMediaPhoto("{}/{}".format(direc,media)))

        elif media.split(".")[-1] == 'mp4':
            re_arr.append(InputMediaVideo("{}/{}".format(direc, media)))
    return list(chunks(re_arr,10))

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == "__main__":
    app.run()

