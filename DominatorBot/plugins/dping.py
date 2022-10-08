import asyncio
import datetime
import os
import re
import time

from random import choice
from telethon import functions
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.channels import LeaveChannelRequest

from ..sql.gvar_sql import gvarstat
from . import *

ping_txt = """█████████\n█▄█████▄█\n█▼▼▼▼▼\n█Ꭰօʍìղąէօɾβօէ įʂ ටղƑìɾҽ\n█▲▲▲▲▲\n█████████\n██ ██\n
    ⚘  <i>ʂ℘ɛɛɖ :</i> <code>{}</code>
    ⚘  <i>ų℘ɬıɱɛ :</i> <code>{}</code>
    ⚘  <i>ơῳŋɛཞ :</i> {}
"""


@dominator_cmd(pattern="dping$")
async def pong(dominator):
    start = datetime.datetime.now()
    a = gvarstat("PING_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = choice(pic_list)
    else:
        PIC = None
    event = await eor(dominator, "`❝❄ᑭ♨ɳց…!❄❞´")
    cid = await client_id(event)
    ForGo10God, DOMINATOR_USER = cid[0], cid[1]
    dominator_mention = f"<a href='tg://user?id={ForGo10God}'>{DOMINATOR_USER}</a>"
    uptime = await get_time((time.time() - StartTime))
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    if PIC:
        await event.client.send_file(event.chat_id,
                                     file=PIC,
                                     caption=ping_txt.format(ms, uptime, dominator_mention),
                                     parse_mode="HTML",
                                 )
        await event.delete()
    else:
        await event.edit(ping_txt.format(ms, uptime, dominator_mention), parse_mode="HTML")
