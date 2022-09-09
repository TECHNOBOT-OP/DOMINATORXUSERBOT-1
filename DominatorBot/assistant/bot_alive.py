from telethon import Button

from Dominatorbot import Config, legend, legendversion

from ..core.logger import logging
from ..helpers import reply_id
from ..plugins import mention
from ..sql_helper.bot_blacklists import check_is_black_list
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

menu_category = "bot"
botusername = Config.BOT_USERNAME


PM_IMG = "https://telegra.ph/file/93f5cc37e28743aeef809.mp4"
pm_caption = f"⚜『Ꭰօʍìղąէօɾβօէ』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『Ꭰօʍìղąէօɾ』~ `{legendversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/dominator_bot_official)\n"
pm_caption += f"┣**License** ~ [License](github.com/dominator454/DOMINATORXBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『Ꭰօʍìղąէօɾ』 ](https://t.me/N1xDOMINATOR)\n"
pm_caption += f"┣Assistant ~ By [『Ꭰօʍìղąէօɾ』 ](https://t.me/N1xDOMINATOR)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『Ꭰօʍìղąէօɾβօէ』](https://t.me/LegendBot_XD) «««"


@dominator.bot_cmd(
    pattern=f"^/alive({botusername})?([\s]+)?$",
    incoming=True,
)
async def bot_start(event):
    chat = await event.get_chat()
    await legend.get_me()
    if check_is_black_list(chat.id):
        return
    reply_to = await reply_id(event)
    buttons = [
        (Button.url("🔱 Repo 🔱", "https://github.com/dominator454/DOMINATORXBOT"),),
    ]
    try:
        await event.client.send_file(
            chat.id,
            PM_IMG,
            caption=pm_caption,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Error**\nThere was a error while using **alive**. `{e}`",
            )
