from io import BytesIO

from aip import AipSpeech
from pydub import AudioSegment
from pydub.utils import which

import config


# 百度语音免费申请应用即可获取这三个key
APP_ID = config.baidu_yuyin_app_id
API_KEY = config.baidu_yuyin_api_key
SECRET_KEY = config.baidu_yuyin_secret_key

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

AudioSegment.converter = which("ffmpeg")


def voice_to_text(msg):
    """语言转文字"""
    print('进来了吗')
    vo_file = msg.get_file('./ttt.mp3')

    # vo_file_type = type(vo_file)
    audio = AudioSegment.from_mp3(vo_file)
    export = audio.export(format="wav")
    response = client.asr(export.read(), 'wav', 16000, {'dev_pid': 1537})
    if response and response['err_no'] == 0:
        return response['result'][0]
    return None


if __name__ == '__main__':
    """
        测试百度语音转文字接口
        需要在common.cfg中配置了你免费申请的百度语音key才可以测试
        百度语音免费申请地址：http://yuyin.baidu.com/
    """
    file_io = None
    with open('baidu-yuyin-test.wav', 'rb') as fp:
        file_io = fp.read()
    response_json = client.asr(file_io, 'wav', 16000, {'dev_pid': 1537})
    print('m4a：' + response_json['result'][0])

    audio = AudioSegment.from_mp3('baidu-yuyin-test.mp3')
    export = audio.export(out_f='baidu-yuyin-test.wav', format="wav")






