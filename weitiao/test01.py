import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models

# 加载预训练模型
model = models.resnet18(pretrained=True)

# 修改模型的输出层
num_classes = 10  # 替换为目标任务的类别数
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, num_classes)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# 加载数据集并进行训练
train_loader = ""  # 替换为训练集的数据加载器
num_epochs = 10  # 迭代次数

for epoch in range(num_epochs):
    for images, labels in train_loader:
        optimizer.zero_grad()

        # 前向传播
        outputs = model(images)
        loss = criterion(outputs, labels)

        # 反向传播和优化
        loss.backward()
        optimizer.step()

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}")

# 模型微调完成，保存模型
torch.save(model.state_dict(), "fine_tuned_model.pth")
