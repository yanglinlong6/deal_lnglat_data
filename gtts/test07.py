# obtain path to "english.wav" in the same folder as this script
from os import path
from pprint import pprint

import speech_recognition as sr

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx language="zh-CN",
try:
    print("Sphinx thinks you said ")
    print(r.recognize_sphinx(audio))
    # pprint(r.recognize_google(audio, show_all=True))
    audio_info = r.recognize_google(audio, language="zh-CN", show_all=True)
    # pprint(audio_info)
    # text = audio_info["alternative"][0]["transcript"]
    # print(text)
    # # 提取时间戳和文本
    timestamped_text = audio_info["alternative"][0]["transcript"]
    timestamped_text = timestamped_text.replace("<silence.>", "").replace("**/", "")
    timestamped_text = timestamped_text.strip()
    print(timestamped_text)
    # for i, word_info in enumerate(audio_info["alternative"][0]["segments"]):
    #     word = word_info["word"]
    #     start_time = word_info["start"]
    #     end_time = word_info["end"]
    #     print({"word": word, "start_time": start_time, "end_time": end_time})
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
