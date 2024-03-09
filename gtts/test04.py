import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120)  # 设置语速
engine.setProperty('volume', 1.0)  # 设置音量

text = "Hello, world!"
engine.say(text)
engine.runAndWait()
