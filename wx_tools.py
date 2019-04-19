from wxpy import *
import baidu_yuyin


def recording_2_text(msg):
    """微信语音消息转换为文字消息"""
    text = baidu_yuyin.voice_to_text(msg)
    print('666')
    msg.text = baidu_yuyin.voice_to_text(msg)
    msg.type = TEXT
