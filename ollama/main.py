#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/9/26 10:55
# @Author : Jim
# @File : config.py
# @Software: PyCharm
import pyaudio
import sys
import uuid
import requests
import wave
import base64
import json
import hashlib

from importlib  import reload
import time
from urllib import parse

from zhipuai import ZhipuAI
client = ZhipuAI(api_key="ac92c959bb3b9092c6f2e0da45cb3acf.kSuemdoJcPgFxieY") # 填写您自己的APIKey

reload(sys)

#有道语音识别
YOUDAO_URL = 'https://openapi.youdao.com/asrapi'
YOUDAO_URL_TTS = 'https://openapi.youdao.com/ttsapi'
APP_KEY = '28d5d96858e3caee'
APP_SECRET = '3FXrws2dDX3Gq0p1GGc0Ek8bMoDGBl6d'
WAVE_OUTPUT_FILENAME = "D:/python_project/emotiVoice/output.wav"

def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size-10:size]

def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()

def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)

def encrypt_tts(signStr):
    hash_algorithm = hashlib.md5()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()

def do_request_tts(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL_TTS, data=data, headers=headers)

def wav_to_text(audio_file_path):
    lang_type = 'zh-CHS'
    extension = audio_file_path[audio_file_path.rindex('.')+1:]
    if extension != 'wav':
        print('不支持的音频类型')
        sys.exit(1)
    wav_info = wave.open(audio_file_path, 'rb')
    sample_rate = wav_info.getframerate()
    nchannels = wav_info.getnchannels()
    wav_info.close()
    with open(audio_file_path, 'rb') as file_wav:
        q = base64.b64encode(file_wav.read()).decode('utf-8')

    data = {}
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    data['signType'] = "v2"
    data['langType'] = lang_type
    data['rate'] = sample_rate
    data['format'] = 'wav'
    data['channel'] = nchannels
    data['type'] = 1

    response = do_request(data)
    # print(response.content.decode('utf-8'))
    jdata = json.loads(response.content.decode('utf-8'))
    print(jdata["result"][0])
    return jdata["result"][0]

def text_to_wav(text):
    data = {}
    data['langType'] = 'zh-CHS'
    salt = str(uuid.uuid1())
    signStr = APP_KEY + text + salt + APP_SECRET
    sign = encrypt_tts(signStr)
    data['appKey'] = APP_KEY
    data['q'] = text
    data['salt'] = salt
    data['sign'] = sign
    data['voiceName'] = "youxiaozhi"

    response = do_request_tts(data)
    contentType = response.headers['Content-Type']
    if contentType == "audio/mp3":
        millis = int(round(time.time() * 1000))
        filePath = "D:/python_project/emotiVoice/" + str(millis) + ".mp3"
        fo = open(filePath, 'wb')
        fo.write(response.content)
        fo.close()
        return filePath
    else:
        print(response.content)
    return ""

#播放mp3
from pydub import AudioSegment
#这里filepath填的是.mp3文件的名字（也可加上路径）
def trans_mp3_to_wav(filepath):
    song = AudioSegment.from_mp3(filepath)
    song.export(filepath.replace("mp3","wav"), format="wav")
    return filepath.replace("mp3","wav")

    
# 设置音频参数
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000 #44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = WAVE_OUTPUT_FILENAME #"output.wav"

# 初始化PyAudio
audio = pyaudio.PyAudio()

# 打开音频流
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("录音开始...")
# 开始录音
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("录音结束...")

# 关闭音频流
stream.stop_stream()
stream.close()
audio.terminate()

# 将录音数据保存为.wav文件
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
# 语音文件转写
text = wav_to_text(WAVE_OUTPUT_FILENAME)
# 语言大模型生成
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "user", "content": f"{text}"}
    ]
)
print(response.choices[0].message.content)
print(response.usage.total_tokens)
# 语音合成
output = text_to_wav(response.choices[0].message.content)
print(output)
# 播放语音
# output = trans_mp3_to_wav(output)
from playsound import playsound
playsound(output)
