from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

ocr_detection = pipeline(
    Tasks.ocr_detection, model="damo/cv_resnet18_ocr-detection-line-level_damo"
)
result = ocr_detection(
    "https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/ocr_detection.jpg"
)
print(result)
