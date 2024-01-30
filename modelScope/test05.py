import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
# os.environ["HF_HOME"] = "G:\huggingface"
# os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
# os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"


# os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
# os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

from modelscope.models import Model
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

model = "ZhipuAI/CodeGeeX-Code-Generation-13B"
pipe = pipeline(
    task=Tasks.code_generation,
    model=model,
)
inputs = {
    "prompt": 'from typing import List\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    """ Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    """\n    return",',
    "language": "Python",
}

result = pipe(inputs)
print(result)
