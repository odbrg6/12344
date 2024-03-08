import os
import asyncio
import logging
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from HackSessionBot.Helpers.data import LOG_TEXT,ART
from pyromod import listen 

#getting variables
API_ID = 22877012
API_HASH = "6d59bf3287c22f491e291a8a366c997c"
TOKEN = "6971545809:AAHPark1t-daGM_pXqqzohvxZ3r5cSQUyOs"
START_PIC = "https://graph.org/file/9ffcff556e24e0c37e444.jpg"
CHAT = "-1002134604531"


if not START_PIC:
    START_PIC = "https://graph.org/file/9ffcff556e24e0c37e444.jpg"

#rich
LOG = Console()

#logger
logging.basicConfig(level=logging.INFO)

#client
app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    


async def HackSessionBot():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]{ART}")
    LOG.print("[bold yellow]تم عزيزي المواطن")
    await app.start()    
    


loop = asyncio.get_event_loop()
loop.run_until_complete(HackSessionBot())    



    
    

    
    



