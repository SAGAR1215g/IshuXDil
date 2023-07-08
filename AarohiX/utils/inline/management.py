from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AarohiX import app
from config import SUPPORT_GROUP


def management_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="☹️ᴀᴅᴍɪɴ☹️",
                    callback_data="management_callback hb1",
                ),
                InlineKeyboardButton(
                    text="🥰ᴀᴜᴛʜ🥰",
                    callback_data="management_callback hb2",
                ),
                InlineKeyboardButton(
                    text="🚫ʙʟᴀᴄᴋʟɪsᴛ🚫",
                    callback_data="management_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔍ʙʀᴏᴀᴅᴄᴀsᴛ🔎",
                    callback_data="management_callback hb4",
                ),
                InlineKeyboardButton(
                    text="📵ɢʙᴀɴ📵",
                    callback_data="management_callback hb12",
                ),
                InlineKeyboardButton(
                    text="📃ʟʏʀɪᴄs📃",
                    callback_data="management_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🍁ᴩɪɴɢ🍁",
                    callback_data="management_callback hb7",
                ),
                InlineKeyboardButton(
                    text="📱ᴩʟᴀʏ📲",
                    callback_data="management_callback hb8",
                ),
                InlineKeyboardButton(
                    text="💾ᴩʟᴀʏʟɪsᴛ💾",
                    callback_data="management_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🖥ᴠɪᴅᴇᴏᴄʜᴀᴛs🖥",
                    callback_data="management_callback hb10",
                ),
                InlineKeyboardButton(
                    text="🔍sᴛᴀʀᴛ🔎",
                    callback_data="management_callback hb11",
                ),
                InlineKeyboardButton(
                    text="😪sᴜᴅᴏ😪",
                    callback_data="management_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔻ᴍᴇɴᴛɪᴏɴ ᴄᴏᴍᴍᴀɴᴅs🔻",
                    callback_data="management_callback hb13",
                ),
            ],
            mark,
        ]
    )
    return upl


def management_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_managementer",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="• sᴜᴩᴩᴏʀᴛ •", url=SUPPORT_GROUP
                ),
            ]
        ]
    )
    return upl


def private_management_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=management",
            ),
        ],
    ]
    return buttons
