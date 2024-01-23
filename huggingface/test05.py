import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
os.environ["HF_HOME"] = "G:\huggingface"
os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"
os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

from modelscope.utils.hub import read_config
from modelscope.msdatasets import MsDataset
from modelscope.trainers import build_trainer

train_dataset = MsDataset.load("clue", subset_name="afqmc", split="train")
eval_dataset = MsDataset.load("clue", subset_name="afqmc", split="validation")
model_id = "damo/nlp_structbert_sentence-similarity_chinese-base"
# 读取model中的cfg文件
cfg = read_config(model_id)
# 直接更新其中的参数
cfg.train.max_epochs = 5
cfg.preprocessor.train["label2id"] = {"0": 0, "1": 1}
cfg.preprocessor.val["label2id"] = {"0": 0, "1": 1}
cfg.train.work_dir = "/tmp"
cfg_file = os.path.join("/tmp", "config.json")
# 将参数写入新的配置文件并传入trainer
cfg.dump(cfg_file)
kwargs = dict(
    model=model_id,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    cfg_file=cfg_file,
)
trainer = build_trainer(default_args=kwargs)
trainer.train()
