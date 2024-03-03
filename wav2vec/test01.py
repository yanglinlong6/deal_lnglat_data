import soundfile as sf
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")   # 用于ASR等，32维

audio_input, sample_rate = sf.read(path_audio)  # (31129,)
input_values = processor(audio_input, sampling_rate=sample_rate, return_tensors="pt").input_values  # torch.Size([1, 31129])

logits = model(input_values).logits     # torch.Size([1, 97, 32])
predicted_ids = torch.argmax(logits, dim=-1)    # torch.Size([1, 97])

transcription = processor.decode(predicted_ids[0])  # ASR的解码结果

from transformers import Wav2Vec2Model
model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base-960h")    # 用于提取通用特征，768维
wav2vec2 = model(input_values)['last_hidden_state']     # torch.Size([1, 97, 768])，模型出来是一个BaseModelOutput的结构体。
