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
                text="↻ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ↻",
                url=f"https://t.me/MERA_X_PYAR_BOT?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ғᴇᴀᴛᴜʀᴇ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢ", callback_data="settings_helper"
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
                text="↻ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ↻",
                url=f"https://t.me/MERA_X_PYAR_BOT?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="ᴍᴏʀᴇ", url=f"https://t.me/ANGEL_K_WORLD",
            ),
        
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ", url=f"https://t.me/IND_PAWAN",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ғᴇᴀᴛᴜʀᴇs", callback_data="settings_back_helper"
            )
        ],
     ]
    return buttons
