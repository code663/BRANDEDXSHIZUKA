from typing import Union
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config



def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•",
                url=f"https://t.me/MERA_X_PYAR_BOT?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋𝐅𝐄𝐀𝐓𝐔𝐑𝐄🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️𝐒𝐄𝐓𝐓𝐈𝐍𝐆⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons

#extra shit
BOT_USERNAME = ("MERA_X_PYAR_BOT")

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    global GROUP_USERNAME
    global CHANNEL_USERNAME
    buttons = [
        [
            InlineKeyboardButton(
                text="•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•",
                url=f"https://t.me/MERA_X_PYAR_BOT?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="𝐌ᴏʀᴇ🥀", url=f"https://t.me/ANGEL_K_WORLD",
            ),
        
            InlineKeyboardButton(
                text="𝐆𝚁𝙾𝚄𝙿✨", url=f"https://t.me/IND_PAWAN",
            ),
        ],
        [
            InlineKeyboardButton(
                text="۞ 𝐅𝙴𝙰𝚃𝚄𝚁𝙴𝚂 ۞", callback_data="settings_back_helper"
            )
        ],
     ]
    return buttons
