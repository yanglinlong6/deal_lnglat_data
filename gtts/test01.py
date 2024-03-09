from gtts import gTTS
import os


# text = "Hello, world!"
# lang = 'en'

text = "你好,杨林龙"
lang = 'zh-cn'

tts = gTTS(text=text, lang=lang, slow=False)
tts.save("hello.mp3")

os.system("start hello.mp3")  # 在 Windows 上播放音频文件
