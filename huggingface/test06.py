import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
# os.environ["HF_HOME"] = "G:\huggingface"
# os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
# os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"
# os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
# os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

import tempfile

from modelscope.metainfo import Trainers
from modelscope.trainers import build_trainer


def main():
    # 准备数据集
    from datasets import load_dataset

    dataset_dict = load_dataset("luozhouyang/dureader", "robust")

    def concat_answer_context(dataset):
        dataset["src_txt"] = (
            dataset["answers"]["text"][0] + "[SEP]" + dataset["context"]
        )
        return dataset

    train_dataset = dataset_dict["train"].map(concat_answer_context)
    eval_dataset = dataset_dict["validation"].map(concat_answer_context)

    train_dataset = (
        train_dataset.rename_columns({"question": "tgt_txt"})
        .remove_columns("context")
        .remove_columns("id")
        .remove_columns("answers")
    )
    eval_dataset = (
        eval_dataset.rename_columns({"question": "tgt_txt"})
        .remove_columns("context")
        .remove_columns("id")
        .remove_columns("answers")
    )

    # 准备work目录，用以存放log和finetune后的checkpoint文件
    tmp_dir = "plug_work_dir/rank" + os.environ["RANK"]
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    model_id = "damo/nlp_plug_text-generation_27B"

    # 使用plug_trainer进行训练
    kwargs = dict(
        model=model_id,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        work_dir=tmp_dir,
    )

    trainer = build_trainer(name=Trainers.nlp_plug_trainer, default_args=kwargs)
    trainer.train()


if __name__ == "__main__":
    main()
