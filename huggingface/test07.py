import torch

# 两个tensor，可以累计梯度信息
a = torch.tensor([1.0], requires_grad=True)
b = torch.tensor([2.0], requires_grad=True)
c = a * b
# 计算梯度
c.backward()
print(a.grad, b.grad)
# tensor([2.]) tensor([1.])
