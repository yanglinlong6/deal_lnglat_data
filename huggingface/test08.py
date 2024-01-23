import torch
from torch.nn import Linear


class SubModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # 有时候会传入一个config，下面的Linear就变成：
        # self.a = Linear(config.hidden_size, config.hidden_size)
        self.a = Linear(4, 4)


class Module(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.sub = SubModule()


module = Module()

state_dict = module.state_dict()  # 实际上是一个key value对

# OrderedDict([('sub.a.weight', tensor([[-0.4148, -0.2303, -0.3650, -0.4019],
#        [-0.2495,  0.1113,  0.3846,  0.3645],
#        [ 0.0395, -0.0490, -0.1738,  0.0820],
#        [ 0.4187,  0.4697, -0.4100, -0.4685]])), ('sub.a.bias', tensor([ 0.4756, -0.4298, -0.4380,  0.3344]))])

# 如果我想把SubModule替换为别的结构能不能做呢？
setattr(module, "sub", Linear(4, 4))
# 这样模型的结构就被动态的改变了
# 这个就是轻量调优生效的基本原理：新增或改变原有的模型结构，具体可以查看选型或训练章节
