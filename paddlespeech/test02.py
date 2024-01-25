from paddlespeech.cli.tts import TTSExecutor

tts_executor = TTSExecutor()
tts_executor(text="你好，世界！", output="output.wav")


from paddlespeech.cli.audio import AudioExecutor

audio_executor = AudioExecutor()
audio_executor(input="output.wav", output="output01.wav", effect="pitch")
