import io

import pyttsx3


class FileDriver:
    def __init__(self, voice=None, rate=None, volume=None, output_file=None):
        super().__init__()
        self._voice = voice
        self._rate = rate
        self._volume = volume
        self._output_file = output_file

    def connect(self):
        engine = pyttsx3.init()
        engine.setProperty('voice', self._voice)
        engine.setProperty('rate', self._rate)
        engine.setProperty('volume', self._volume)
        engine.save_to_file(text, output_file)
        return engine


def text_to_speech(text, voice=None, rate=None, volume=None, output_file=None):
    with io.BytesIO() as output_stream:
        driver = FileDriver(voice, rate, volume, output_stream)
        engine = driver.connect()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        engine.disconnect({"topic": 1})

        if output_file:
            with open(output_file, 'wb') as f:
                f.write(output_stream.getvalue())
        else:
            return output_stream.getvalue()

text = "Hello, world! 我们都是中国人 世界需要我们"
output_file = "hello_world.wav"

text_to_speech(text, output_file=output_file)
