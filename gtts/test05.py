import json
import subprocess
import requests

text = "Hello, world!"

url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/<instance_id>/v1/synthesize"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <access_token>"
}

data = {"text": text, "voice": "en-US_AllisonVoice", "accept": "audio/wav"}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    with open("output.wav", "wb") as f:
        f.write(response.content)
    # 播放音频文件
    subprocess.run(['aplay', 'output.wav'])
else:
    print("Error:", response.text)
