import subprocess

text = "Hello, world!"

command = f'echo "{text}" | festival --tts'
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
output, error = process.communicate()

with open('hello.wav', 'wb') as f:
    f.write(output)

subprocess.call(['afplay', 'hello.wav'])  # 在 macOS 上播放音频文件
