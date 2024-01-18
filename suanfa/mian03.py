from paddleocr import PaddleOCR, draw_ocr
from PIL import Image


# load model
# Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改 lang参数进行切换
# lang参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`
ocr = PaddleOCR(
    lang="ch",
    # use_gpu=False,
    use_gpu=True,
    det_model_dir="../paddleORC_model/ch_ppocr_server_v2.0_det_infer/",
    cls_model_dir="ch_ppocr_mobile_v2.0_cls_infer/",
    rec_model_dir="ch_ppocr_server_v2.0_rec_infer/",
)

# load dataset
# img_path = "./08631508_2.jpg"
img_path = "./image/baidu_image/test7.jpg"
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)
    print(line[0][1][0])

# 注：
# result是一个list，每个item包含了文本框，文字和识别置信度
# line的格式为：
# [[[3.0, 149.0], [43.0, 149.0], [43.0, 163.0], [3.0, 163.0]], ('人心安', 0.6762619018554688)]
# 文字框 boxes = line[0]，包含文字框的四个角的(x,y)坐标
# 文字 txts = line[1][0]
# 识别置信度 scores = line[1][1]

# visual
# image = Image.open(img_path).convert("RGB")
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores)
# im_show = Image.fromarray(im_show)
# im_show.save("result.jpg")
