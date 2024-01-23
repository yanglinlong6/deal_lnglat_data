import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
os.environ["HF_HOME"] = "G:\huggingface"
os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"
os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

import random

import numpy as np
import torch
from torch.optim import AdamW
from torch.optim.lr_scheduler import StepLR
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.dataloader import default_collate
from torch.nn import CrossEntropyLoss

seed = 42
# 随机种子，影响训练的随机数逻辑，如果随机种子确定，每次训练的结果是一样的
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)

# 确定化cuda、cublas、cudnn的底层随机逻辑
# 否则CUDA会提前优化一些算子，产生不确定性
# 这些处理在训练时也可以不使用
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
torch.use_deterministic_algorithms(True)
# Enable CUDNN deterministic mode
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False


# torch模型都继承于torch.nn.Module
class MyModule(torch.nn.Module):
    def __init__(self, n_classes=2):
        # 优先调用基类构造
        super().__init__()
        # 单个神经元，一个linear加上一个relu激活
        self.linear = torch.nn.Linear(16, n_classes)
        self.relu = torch.nn.ReLU()

    def forward(self, tensor, label):
        # 前向过程
        output = {"logits": self.relu(self.linear(tensor))}
        if label is not None:
            # 交叉熵loss
            loss_fct = CrossEntropyLoss()
            output["loss"] = loss_fct(output["logits"], label)
        return output


# 构造一个数据集
class MyDataset(Dataset):
    # 长度是5
    def __len__(self):
        return 5

    # 如何根据index取得数据集的数据
    def __getitem__(self, index):
        return {"tensor": torch.rand(16), "label": torch.tensor(1)}


# 构造模型
model = MyModule()
# 构造数据集
dataset = MyDataset()
# 构造dataloader， dataloader会负责从数据集中按照batch_size批量取数，这个batch_size参数就是设置给它的
# collate_fn会负责将batch中单行的数据进行padding
dataloader = DataLoader(dataset, batch_size=4, collate_fn=default_collate)
# optimizer，负责将梯度累加回原来的parameters
# lr就是设置到这里的
optimizer = AdamW(model.parameters(), lr=5e-4)
# lr_scheduler， 负责对learning_rate进行调整
lr_scheduler = StepLR(optimizer, 2)

# 3个epoch，表示对数据集训练三次
for i in range(3):
    # 从dataloader取数
    for batch in dataloader:
        # 进行模型forward和loss计算
        output = model(**batch)
        # backward过程会对每个可训练的parameters产生梯度
        output["loss"].backward()
        # 建议此时看下model中linear的grad值
        # 也就是model.linear.weight.grad

        # 将梯度累加回parameters
        optimizer.step()
        # 清理使用完的grad
        optimizer.zero_grad()
        # 调整lr
        lr_scheduler.step()
