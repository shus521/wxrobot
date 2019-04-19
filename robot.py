from wxpy import *

import wx_friend
import wx_tools


# 微信机器人，缓存登录信息
bot = Bot(cache_path=True)


@bot.register(chats=Friend)
def auto_reply(msg):
    """自动回复"""
    if msg.type == TEXT:
        wx_friend.auto_reply(msg)
    elif msg.type == RECORDING:
        wx_tools.recording_2_text(msg)
        wx_friend.auto_reply(msg)



embed()

