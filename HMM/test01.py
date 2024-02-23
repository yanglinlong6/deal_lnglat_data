import numpy as np
from hmmlearn import hmm

# 假设我们有一个简单的HMM，有两个状态和三个可能的观测值
n_states = 2
n_observations = 3

# 初始化HMM模型
model = hmm.MultinomialHMM(n_components=n_states)

# 随机生成模型参数
model.startprob_ = np.array([0.6, 0.4])
model.transmat_ = np.array([[0.7, 0.3],
                            [0.4, 0.6]])
model.emissionprob_ = np.array([[0.1, 0.4, 0.5],
                                [0.6, 0.3, 0.1]])

# 生成一些观测数据
观测序列 = np.array([[0], [1], [2], [1]])

# 使用模型解码，找到最可能的状态序列
logprob, 状态序列 = model.decode(观测序列, algorithm="viterbi")

print("最可能的状态序列:", 状态序列)
